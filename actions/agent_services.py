from lib import action


class ConsulAgentServicesAction(action.ConsulBaseAction):
    def run(self):
        return (True, self.consul.agent.services())
