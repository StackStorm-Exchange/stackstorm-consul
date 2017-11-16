from lib import action


class ConsulServiceMaintenanceAction(action.ConsulBaseAction):
    def run(self, service_id, enable, reason=None):
        return (True, self.consul.service.maintenance(
            service_id=service_id,
            enable=enable,
            reason=reason
        ))
