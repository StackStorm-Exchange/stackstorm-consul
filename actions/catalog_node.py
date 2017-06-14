from lib import action


class ConsulCatalogNodeAction(action.ConsulBaseAction):
    def run(self, node):
        index, node = self.consul.catalog.node(node)
        return node
