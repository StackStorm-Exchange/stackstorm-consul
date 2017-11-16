from lib import action


class ConsulKVDeleteAction(action.ConsulBaseAction):
    def run(self, key, recurse=None, cas=None, token=None, dc=None):
        return (True, self.consul.kv.delete(
            key,
            recurse=recurse,
            cas=cas,
            token=token,
            dc=dc
        ))
