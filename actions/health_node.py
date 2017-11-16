from lib import action


class ConsulHealthNodeAction(action.ConsulBaseAction):
    def run(self,
            node,
            index=None,
            wait=None,
            dc=None,
            token=None):

        return (True, self.consul.health.node(
            node,
            index=index,
            wait=wait,
            dc=dc,
            token=token))
