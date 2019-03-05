from lib import action


class ConsulEventListAction(action.ConsulBaseAction):
    def run(self, name=None, index=None, wait=None, consul_profile=None):

        self._create_client(consul_profile)

        if name == "":
            name = None

        return (True, self.consul.event.list(name=name, index=index, wait=wait))
