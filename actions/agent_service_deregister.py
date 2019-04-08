from lib import action


class ConsulServiceDeregisterAction(action.ConsulBaseAction):
    def run(self, service_id, consul_profile=None):
        self._create_client(consul_profile)
        return (True, self.consul.agent.service.deregister(service_id=service_id))
