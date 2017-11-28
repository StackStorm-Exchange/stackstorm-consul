from lib import action


class ConsulServiceMaintenanceAction(action.ConsulBaseAction):
    def run(self, service_id, enable, reason=None):
        return (True, self.consul.agent.service.maintenance(
            service_id=service_id,
            enable=enable,
            reason=reason
        ))
