from lib import action


class ConsulAgentChecksAction(action.ConsulBaseAction):
    def run(self):
        return (True, self.consul.agent.checks())
