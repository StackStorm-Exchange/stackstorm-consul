from lib import action


class ConsulSessionListAction(action.ConsulBaseAction):
    def run(self, index=None, wait=None, consistency=None, dc=None):

        return (True, self.consul.session.list(
            index=index,
            wait=wait,
            consistency=consistency,
            dc=dc))
