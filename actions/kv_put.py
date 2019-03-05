from lib import action


class ConsulKVPutAction(action.ConsulBaseAction):
    def run(
        self,
        key,
        value,
        cas=None,
        flags=None,
        acquire=None,
        release=None,
        token=None,
        dc=None,
        to_json=False,
        consul_profile=None
    ):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None

        if to_json:
            value = self.to_json(value)

        return self.consul.kv.put(
            key,
            value,
            cas=cas,
            flags=flags,
            acquire=acquire,
            release=release,
            token=token,
            dc=dc
        )
