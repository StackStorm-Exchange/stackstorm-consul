from lib import action


class ConsulAgentServicesAction(action.ConsulBaseAction):
    def run(self, consul_profile=None):
        self._create_client(consul_profile)
        return (True, self.consul.agent.services())
