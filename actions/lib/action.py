import six
import json
import random
import time

from st2common import log as logging
from st2common.runners.base_action import Action

# http://python-consul.readthedocs.org/en/latest/#
import consul

LOG = logging.getLogger(__name__)


class ConsulBaseAction(Action):

    def __init__(self, config):
        super(ConsulBaseAction, self).__init__(config)
        self.consul = self._get_client()

    def _get_client(self):
        dc = self.config.get('dc')
        host = self.config.get('host')
        port = self.config.get('port')
        token = self.config.get('token')
        scheme = self.config.get('scheme')
        verify = self.config.get('verify') or True
        consistency = self.config.get('consistency') or 'default'

        client = consul.Consul(host, port, token, scheme, consistency, dc, verify)
        return client

    def to_json(self, value):
        """
        Unescape StackStorm string and push as a json serialised object into consul.
        """
        return json.dumps(json.loads(value.decode('string_escape')))

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
            result = self.create_lock("/".join([self.key_prefix, self.name, '.lock']))
        return result

    def unlock(self, session_id):
        """
        Method called by the Unlock action.
        """
        key = "/".join([self.key_prefix, self.name, '.lock'])
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
        self.client.session.destroy(session_id, self.dc)

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
