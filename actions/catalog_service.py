from lib import action


class ConsulCatalogServiceAction(action.ConsulBaseAction):
    def run(
        self,
        service,
        index=None,
        wait=None,
        tag=None,
        consistency=None,
        dc=None,
        near=None,
        token=None
    ):

        return (True, self.consul.catalog.service(
            service=service,
            index=index,
            wait=wait,
            tag=tag,
            consistency=consistency,
            dc=dc,
            near=near,
            token=token
        ))
