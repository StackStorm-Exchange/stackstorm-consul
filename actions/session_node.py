from lib import action


class ConsulSessionNodeAction(action.ConsulBaseAction):
    def run(self, node, index=None, wait=None, consistency=None, dc=None):

        index, services = self.consul.session.node(node,
                                                   index=index,
                                                   wait=wait,
                                                   consistency=consistency,
                                                   dc=dc)
        return {'index': index, 'services': services}
