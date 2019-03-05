from lib import action


class ConsulHealthStateAction(action.ConsulBaseAction):
    def run(
        self,
        name,
        index=None,
        wait=None,
        dc=None,
        near=None,
        token=None,
        node_meta=None,
        consul_profile=None
    ):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None
        return (
            True,
            self.consul.health.state(
                name,
                index=index,
                wait=wait,
                dc=dc,
                near=near,
                token=token,
                node_meta=node_meta
            )
        )
