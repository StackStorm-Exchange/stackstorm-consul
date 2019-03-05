from lib import action


class ConsulSessionInfoAction(action.ConsulBaseAction):
    def run(
        self,
        session_id,
        index=None,
        wait=None,
        consistency=None,
        dc=None,
        consul_profile=None
    ):
        self._create_client(consul_profile)

        return (
            True,
            self.consul.session.info(
                session_id,
                index=index,
                wait=wait,
                consistency=consistency,
                dc=dc
            )
        )
