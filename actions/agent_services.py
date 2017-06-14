from lib import action


class ConsulAgentServicesAction(action.ConsulBaseAction):
    def run(self):
        return self.consul.agent.services()
