from lib import action


class ConsulHealthServiceAction(action.ConsulBaseAction):
    def run(
        self,
        service,
        index=None,
        wait=None,
        passing=None,
        tag=None,
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
            self.consul.health.service(
                service,
                index=index,
                wait=wait,
                passing=passing,
                tag=tag,
                dc=dc,
                near=near,
                token=token,
                node_meta=node_meta
            )
        )
