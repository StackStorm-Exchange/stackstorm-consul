from lib import action


class ConsulAgentForceLeaveAction(action.ConsulBaseAction):
    def run(self, node, consul_profile=None):
        self._create_client(consul_profile)

        return (True, self.consul.agent.force_leave(node))
