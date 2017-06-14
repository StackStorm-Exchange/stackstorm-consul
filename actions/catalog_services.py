from lib import action


class ConsulCatalogServicesAction(action.ConsulBaseAction):
    def run(self,
            service,
            index=None,
            wait=None,
            tag=None,
            consistency=None,
            dc=None,
            near=None,
            token=None):

        index, service = self.consul.catalog.service(
            service,
            index=index,
            wait=wait,
            tag=tag,
            consistency=consistency,
            dc=dc,
            near=near,
            token=token)
        return {"index": index, "service": service}
