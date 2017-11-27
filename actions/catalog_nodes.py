from lib import action


class ConsulCatalogNodesAction(action.ConsulBaseAction):
    def run(
        self,
        index=None,
        wait=None,
        consistency=None,
        dc=None,
        near=None,
        token=None
    ):

        return (True, self.consul.catalog.nodes(
            index=index,
            wait=wait,
            consistency=consistency,
            dc=dc,
            near=near,
            token=token
        ))
