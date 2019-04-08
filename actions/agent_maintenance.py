from lib import action


class ConsulAgentMaintenanceAction(action.ConsulBaseAction):
    def run(self, enable=True, reason=None, consul_profile=None):
        self._create_client(consul_profile)

        return (True, self.consul.agent.maintenance(enable, reason))
