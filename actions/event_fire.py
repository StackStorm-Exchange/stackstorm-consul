from lib import action


class ConsulEventFireAction(action.ConsulBaseAction):
    def run(
        self,
        name,
        body="",
        node=None,
        service=None,
        tag=None,
        token=None,
        consul_profile=None
    ):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None

        if len(body) > 100:
            self.logger.warn("Event body being fired exceeds the recommended 100 byte limit!")

        return (
            True,
            self.consul.event.fire(
                name=name,
                body=body,
                node=node,
                service=service,
                tag=tag,
                token=token
            )
        )
