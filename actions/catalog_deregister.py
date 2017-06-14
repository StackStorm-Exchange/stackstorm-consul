from lib import action


class ConsulCatalogDeregisterAction(action.ConsulBaseAction):
    def run(self, node, service, dc):

        result = self.consul.catalog.deregister(node, service, dc=dc)
        return (result, "")
