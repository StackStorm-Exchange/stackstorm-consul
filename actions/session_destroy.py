from lib import action


class ConsulSessionDestroyAction(action.ConsulBaseAction):
    def run(self, session_id, dc=None):
        return (True, self.consul.session.destroy(session_id, dc=dc))
