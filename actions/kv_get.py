from lib import action
import json


class ConsulKVGetAction(action.ConsulBaseAction):
    def run(self,
            key,
            index=None,
            recurse=False,
            wait=None,
            token=None,
            consistency=None,
            keys=False,
            separator=None,
            dc=None,
            from_json=False):

        idx, res = self.consul.kv.get(key,
                                      index=index,
                                      recurse=recurse,
                                      wait=wait,
                                      token=token,
                                      consistency=consistency,
                                      keys=keys,
                                      separator=separator,
                                      dc=dc)

        if from_json and not keys:
            if isinstance(res, dict):
                    res["Value"] = self.from_json(res["Value"])
            if isinstance(res, list):
                for item in res:
                    item["Value"] = self.from_json(item["Value"])

        return (True, [idx, res])
