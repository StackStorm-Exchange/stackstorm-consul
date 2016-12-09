from lib import action

class ConsulAclDestroyAction(action.ConsulBaseAction):
    def run(self, acl_id):

        resp = self.consul.acl.destroy(acl_id)
        return resp
