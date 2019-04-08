from lib import action


class ConsulCatalogNodeAction(action.ConsulBaseAction):
    def run(
        self,
        node,
        index=None,
        wait=None,
        consistency=None,
        dc=None,
        token=None,
        consul_profile=None
    ):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None

        return (
            True,
            self.consul.catalog.node(
                node,
                index=index,
                wait=wait,
                consistency=consistency,
                dc=dc,
                token=token
            )
        )
