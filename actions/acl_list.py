from lib import action


class ConsulAclListAction(action.ConsulBaseAction):
    def run(self):
        return (True, self.consul.acl.list())
