from lib import action


class ConsulSessionListAction(action.ConsulBaseAction):
    def run(
        self,
        index=None,
        wait=None,
        consistency=None,
        dc=None,
        consul_profile=None,
    ):
        self._create_client(consul_profile)

        return (
            True,
            self.consul.session.list(
                index=index,
                wait=wait,
                consistency=consistency,
                dc=dc
            )
        )
