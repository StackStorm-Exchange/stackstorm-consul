from lib import action


class ConsulCatalogDataCentersAction(action.ConsulBaseAction):
    def run(self):
        return (True, self.consul.catalog.datacenters())
