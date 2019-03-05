from lib import action


class ConsulAgentJoinAction(action.ConsulBaseAction):
    def run(self, address, wan=False, consul_profile=None):
        self._create_client(consul_profile)

        return (True, self.consul.agent.join(address, wan))
