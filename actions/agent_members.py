from lib import action


class ConsulAgentMembersAction(action.ConsulBaseAction):
    def run(self, wan=False):
        return (True, self.consul.agent.members(wan))
