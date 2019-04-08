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
            self.consul.catalog.service(
                service=service,
                index=index,
                wait=wait,
                tag=tag,
                consistency=consistency,
                dc=dc,
                near=near,
                token=token
            )
        )
