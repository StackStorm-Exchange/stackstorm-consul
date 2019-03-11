import six
import json
import random
import time
import os

from st2common import log as logging
from st2common.runners.base_action import Action

# http://python-consul.readthedocs.org/en/latest/#
import consul

LOG = logging.getLogger(__name__)


class ConsulBaseAction(Action):

    def __init__(self, config):
        super(ConsulBaseAction, self).__init__(config)
        # Delay the creation of the Consul client to be able to read the consul profile to use.
        self.consul = None

    def _get_pack_configuration(self, profile=None):
        """
        Fetch the variables from the pack configuration.
        """
        if self.config.get("preserve_varenv", True):
            for env_key in os.environ:
                if "CONSUL" in env_key:
                    print("{}={}".format(env_key, os.environ[env_key]))
                    del os.environ[env_key]

        self._get_profile(profile)

    def _get_profile(self, profile=None):
        # Attempt to get the default profile from the config if the action didn't supply one.
        if profile is None:
            profile = self.config.get("default_profile")

        requested_profile = None
        for p in self.config.get("consul_profiles", []):
            if p.get("name", "_") == profile:
                requested_profile = p
                break

        if requested_profile is None:
            raise ValueError(
                "A valid Consul profile must be supplied, '{}' profile.".format(profile)
            )

        self.dc = requested_profile.get("dc")
        self.host = requested_profile.get("host")
        self.port = requested_profile.get("port")
        self.token = requested_profile.get("token")
        self.scheme = requested_profile.get("scheme")
        self.client_cert_path = requested_profile.get("client_cert_path")
        self.client_key_path = requested_profile.get("client_key_path")
        self.cert = (self.client_cert_path, self.client_key_path)
        self.verify = requested_profile.get("verify")
        self.ca_cert_path = requested_profile.get("ca_cert_path", "")
        # Python Requests supports boolean or a file path for the verify agrument, ca_cert_path is
        # used to decide which data type the pack send to the requests module.
        if self.ca_cert_path != "":
            self.verify = self.ca_cert_path
        self.consistency = requested_profile.get("consistency", "default")

    def _create_client(self, profile=None):
        self._get_pack_configuration(profile)

        self.consul = consul.Consul(
            self.host,
            self.port,
            self.token,
            self.scheme,
            self.consistency,
            self.dc,
            self.verify,
            self.cert
        )

    def to_json(self, value):
        """
        Unescape StackStorm string and push as a json serialised object into consul.
        """
        return json.dumps(json.loads(value.decode("string_escape")))

    def from_json(self, value):
        """
        Convert key/value store JSON strings into Python native objects
        to be returned to StackStorm's actionrunner.
        """
        try:
            value = json.loads(value)
        except ValueError:
            pass
        return value


class LockManager(object):
    semaphore = {
        "Limit": 0,
        "Holders": {}
    }

    def __init__(self, client, key_prefix, name, node, token, dc):
        """
        Initialise object with common variables used to create or destroy a lock.
        """
        self.client = client
        self.key_prefix = key_prefix
        self.name = name
        self.node = node
        self.token = token
        self.dc = dc

    def lock(self, max_locks, acquire_timeout, checks, behavior, ttl):
        """
        Method called by the Lock action.
        """
        self.max_locks = max_locks
        self.wait_timeout = acquire_timeout
        self.checks = checks
        self.behavior = behavior
        self.ttl = ttl

        if self.max_locks > 1:
            result = self.create_semaphore()
        else:
            result = self.create_lock("/".join([self.key_prefix, self.name, ".lock"]))
        return result

    def unlock(self, session_id):
        """
        Method called by the Unlock action.
        """
        key = "/".join([self.key_prefix, self.name, ".lock"])
        return self.release_lock(key, session_id)

    def create_semaphore(self):
        raise NotImplementedError

    def release_lock(self, key, session_id):
        """
        Release the lock on the key and destroy the session.
        """
        result = (False, "Failed to release lock.")
        if self.client.kv.put(
            key=key,
            value=None,
            release=session_id,
            token=self.token,
            dc=self.dc
        ) is True:
            if self.destroy_session(session_id) is True:
                result = (True, "Lock released and session destroyed.")
            else:
                result = (True, "Lock released but session could not be destroyed.")
        return result

    def destroy_session(self, session_id):
        return self.client.session.destroy(session_id, self.dc)

    def create_lock(self, key_name):
        result = (False, "")
        session_id = self.create_session()
        if isinstance(session_id, six.string_types) and len(session_id) > 0:
            if self.acquire_lock(session_id, key_name, value=session_id):
                result = (True, session_id)
            else:
                result = (False, "Failed to acquire lock on key.")
                self.destroy_session(session_id)
        else:
            result = (False, "Failed to create a session")
        return result

    def create_session(self):
        """
        https://www.consul.io/docs/internals/sessions.html
        """
        return self.client.session.create(
            name=self.name,
            node=self.node,
            checks=self.checks,
            lock_delay=5,
            behavior=self.behavior,
            ttl=self.ttl,
            dc=self.dc
        )

    def acquire_lock(self, session_id, key, cas=None, value=""):
        """
        wait_timeout is used to determine when to abandon the lock acquisition.
        """
        result = False
        timeout = time.time() + self.wait_timeout
        LOG.info("Acquire lock timeout: {}".format(timeout))
        while time.time() < timeout:
            result = self.client.kv.put(
                key=key,
                value=value,
                cas=cas,
                acquire=session_id,
                token=self.token,
                dc=self.dc
            )
            if result is True:
                break
            time.sleep(random.random())
        return result
