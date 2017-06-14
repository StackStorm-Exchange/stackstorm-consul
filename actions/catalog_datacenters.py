from lib import action


class ConsulCatalogDataCentersAction(action.ConsulBaseAction):
    def run(self):
        return self.consul.catalog.datacenters()
