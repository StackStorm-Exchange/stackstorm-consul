from lib import action


class ConsulCatalogNodeAction(action.ConsulBaseAction):
    def run(self, node, index=None, wait=None, consistency=None, dc=None,
            token=None):
        node = self.consul.catalog.node(node, index=index, wait=wait,
                                        consistency=consistency, dc=dc,
                                        token=token)
        return (True, node)
