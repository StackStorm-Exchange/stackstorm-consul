from lib import action


class ConsulHealthNodeAction(action.ConsulBaseAction):
    def run(self,
            node,
            index=None,
            wait=None,
            dc=None,
            token=None):

        index, node = self.consul.health.node(node,
                                              index=index,
                                              wait=wait,
                                              dc=dc,
                                              token=token)
        return node
