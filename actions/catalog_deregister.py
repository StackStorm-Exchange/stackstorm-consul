from lib import action


class ConsulCatalogDeregisterAction(action.ConsulBaseAction):
    def run(self, node, service=None, check_id=None, dc=None, token=None, consul_profile=None):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None
        return (
            True,
            self.consul.catalog.deregister(
                node,
                service_id=service,
                check_id=check_id,
                dc=dc,
                token=token
            )
        )
