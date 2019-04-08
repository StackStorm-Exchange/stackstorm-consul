from lib import action


class ConsulAgentMembersAction(action.ConsulBaseAction):
    def run(self, wan=False, consul_profile=None):
        self._create_client(consul_profile)

        return (True, self.consul.agent.members(wan))
