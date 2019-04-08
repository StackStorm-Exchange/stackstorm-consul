from lib import action


class ConsulAclInfoAction(action.ConsulBaseAction):
    def run(self, acl_id, consul_profile=None, token=None):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None
        return (True, self.consul.acl.info(acl_id, token=token))
