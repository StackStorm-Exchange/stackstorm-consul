from lib import action


class ConsulKVDeleteAction(action.ConsulBaseAction):
    def run(self, key, recurse=None, cas=None, token=None, dc=None, consul_profile=None):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None
        return (
            True,
            self.consul.kv.delete(
                key,
                recurse=recurse,
                cas=cas,
                token=token,
                dc=dc
            )
        )
