from lib import action


class ConsulHealthStateAction(action.ConsulBaseAction):
    def run(self,
            name,
            index=None,
            wait=None,
            dc=None,
            near=None,
            token=None):

        index, state = self.consul.health.state(name,
                                                index=index,
                                                wait=wait,
                                                dc=dc,
                                                near=near,
                                                token=token)
        return state
