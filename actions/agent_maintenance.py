from lib import action


class ConsulAgentMaintenanceAction(action.ConsulBaseAction):
    def run(self, enable=True, reason=None):
        return (True, self.consul.agent.maintenance(enable, reason))
