from lib import action


class ConsulSessionRenewAction(action.ConsulBaseAction):
    def run(self, session_id, dc=None):
        session = self.consul.session.renew(session_id, dc=dc)
        return (True, session)
