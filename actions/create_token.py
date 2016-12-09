from lib import action

class ConsulAclCreateAction(action.ConsulBaseAction):
    def run(self, name=None, acl_type='client', rules=None):

        rules = rules.encode('ascii','ignore')
        acl_id = self.consul.acl.create(name=name, type=acl_type, rules=rules)
        return acl_id
