from lib import action

import json


class ConsulAclListAction(action.ConsulBaseAction):
    def run(self):
        return (True, json.dumps(self.consul.acl.list()))
