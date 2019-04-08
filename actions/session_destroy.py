from lib import action


class ConsulSessionDestroyAction(action.ConsulBaseAction):
    def run(self, session_id, dc=None, consul_profile=None):
        self._create_client(consul_profile)
        return (True, self.consul.session.destroy(session_id, dc=dc))
