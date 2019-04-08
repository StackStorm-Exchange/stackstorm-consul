from lib import action


class ConsulCatalogRegisterAction(action.ConsulBaseAction):
    def run(
        self,
        node,
        address,
        service=None,
        check=None,
        dc=None,
        token=None,
        consul_profile=None
    ):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None
        if service == {}:
            service = None
        if check == {}:
            check = None

        return (
            True,
            self.consul.catalog.register(
                node,
                address,
                service=service,
                check=check,
                dc=dc,
                token=token
            )
        )
