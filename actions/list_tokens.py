from lib import action

import json

class ConsulAclListAction(action.ConsulBaseAction):
    def run(self):

        acl_list = self.consul.acl.list()
        print json.dumps(acl_list)
