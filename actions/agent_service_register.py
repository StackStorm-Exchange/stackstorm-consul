from lib import action


class ConsulServiceRegisterAction(action.ConsulBaseAction):
    def run(self,
            name,
            service_id=None,
            address=None,
            port=None,
            tags=None,
            check=None,
            token=None,
            enable_tag_override=False,
            consul_profile=None):
        self._create_client(consul_profile)
        return (True, self.consul.agent.service.register(
            name=name,
            service_id=service_id,
            address=address,
            port=port,
            tags=tags,
            check=check,
            token=token,
            enable_tag_override=enable_tag_override
        ))
