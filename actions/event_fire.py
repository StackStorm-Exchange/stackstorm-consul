from lib import action


class ConsulEventFireAction(action.ConsulBaseAction):
    def run(self,
            name,
            body="",
            node=None,
            service=None,
            tag=None):

        if len(body) > 100:
            self.logger.warn("Event body being fired exceeds the recommended 100 byte limit!")

        return (True, self.consul.event.fire(
            name=name,
            body=body,
            node=node,
            service=service,
            tag=tag))
