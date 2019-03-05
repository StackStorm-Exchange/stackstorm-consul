from lib import action


class ConsulServiceMaintenanceAction(action.ConsulBaseAction):
    def run(self, service_id, enable, reason=None, consul_profile=None):
        self._create_client(consul_profile)
        return (True, self.consul.agent.service.maintenance(
            service_id=service_id,
            enable=enable,
            reason=reason
        ))
