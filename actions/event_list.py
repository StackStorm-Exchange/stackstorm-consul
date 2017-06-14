from lib import action


class ConsulEventListAction(action.ConsulBaseAction):
    def run(self,
        name=None,
        index=None,
        wait=None):

        if name == "":
            name = None

        return self.consul.event.list(
            name=name,
            index=index,
            node=node,
            wait=wait)
