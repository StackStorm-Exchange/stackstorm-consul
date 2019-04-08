from lib import action


class ConsulSessionRenewAction(action.ConsulBaseAction):
    def run(self, session_id, dc=None, consul_profile=None):
        self._create_client(consul_profile)

        return (
            True,
            self.consul.session.renew(
                session_id,
                dc=dc
            )
        )
