from st2common import log as logging
from st2common.runners.base_action import Action

# http://python-consul.readthedocs.org/en/latest/#
import consul
import json


class ConsulBaseAction(Action):

    def __init__(self, config):
        super(ConsulBaseAction, self).__init__(config)
        self.consul = self._get_client()
        self.logger = logging.getLogger(__name__)

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
        except ValueError as ignore_exception:
            pass
        return value
