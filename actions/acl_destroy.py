from lib import action


class ConsulAclDestroyAction(action.ConsulBaseAction):
    def run(self, acl_id):
        return (True, self.consul.acl.destroy(acl_id))
