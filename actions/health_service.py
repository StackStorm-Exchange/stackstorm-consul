from lib import action


class ConsulHealthServiceAction(action.ConsulBaseAction):
    def run(self,
            service,
            index=None,
            wait=None,
            passing=None,
            tag=None,
            dc=None,
            near=None,
            token=None):

        return (True, self.consul.health.service(
            service,
            index=index,
            wait=wait,
            passing=passing,
            tag=tag,
            dc=dc,
            near=near,
            token=token))
