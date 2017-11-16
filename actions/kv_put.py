from lib import action


class ConsulKVPutAction(action.ConsulBaseAction):
    def run(self,
            key,
            value,
            cas=None,
            flags=None,
            acquire=None,
            release=None,
            token=None,
            dc=None,
            to_json=False):

        if to_json:
            value = self.to_json(value)

        return (True, self.consul.kv.put(
            key,
            value,
            cas=cas,
            flags=flags,
            acquire=acquire,
            release=release,
            token=token,
            dc=dc
        ))
