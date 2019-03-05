from lib import action


class ConsulCatalogServicesAction(action.ConsulBaseAction):
    def run(
        self,
        index=None,
        wait=None,
        consistency=None,
        dc=None,
        token=None,
        node_meta=None,
        consul_profile=None
    ):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None
        if node_meta == {}:
            node_meta = None
        return (
            True,
            self.consul.catalog.services(
                index=index,
                wait=wait,
                consistency=consistency,
                dc=dc,
                token=token,
                node_meta=node_meta
            )
        )
