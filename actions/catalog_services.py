from lib import action


class ConsulCatalogServicesAction(action.ConsulBaseAction):
    def run(
        self,
        index=None,
        wait=None,
        consistency=None,
        dc=None,
        token=None
    ):

        return (True, self.consul.catalog.services(
            index=index,
            wait=wait,
            consistency=consistency,
            dc=dc,
            token=token))
