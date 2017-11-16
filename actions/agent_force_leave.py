from lib import action


class ConsulAgentForceLeaveAction(action.ConsulBaseAction):
    def run(self, node):
        return (True, self.consul.agent.force_leave(node))
