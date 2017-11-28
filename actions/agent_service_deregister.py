from lib import action


class ConsulServiceDeregisterAction(action.ConsulBaseAction):
    def run(self, service_id):
        return (True, self.consul.agent.service.deregister(service_id=service_id))
