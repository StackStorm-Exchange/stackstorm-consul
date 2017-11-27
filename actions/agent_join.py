from lib import action


class ConsulAgentJoinAction(action.ConsulBaseAction):
    def run(self, address, wan=False):
        return (True, self.consul.agent.join(address, wan))
