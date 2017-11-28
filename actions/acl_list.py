import json

from lib import action


class ConsulAclListAction(action.ConsulBaseAction):
    def run(self):
        return (True, json.dumps(self.consul.acl.list()))
