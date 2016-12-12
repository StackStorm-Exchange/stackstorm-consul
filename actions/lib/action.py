from st2actions.runners.pythonrunner import Action

# http://python-consul.readthedocs.org/en/latest/#
import consul


class ConsulBaseAction(Action):

    def __init__(self, config):
        super(ConsulBaseAction, self).__init__(config)
        self.consul = self._get_client()

    def _get_client(self):
        host = self.config['host']
        port = self.config['port']
        token = self.config['token']
        scheme = self.config['scheme']
        verify = self.config['verify']

        client = consul.Consul(host, port, token, scheme=scheme, verify=verify)
        return client
