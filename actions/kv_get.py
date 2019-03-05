from __future__ import absolute_import
from lib import action


class ConsulKVGetAction(action.ConsulBaseAction):
    def run(
        self,
        key,
        index=None,
        recurse=False,
        wait=None,
        token=None,
        consistency=None,
        keys=False,
        separator=None,
        dc=None,
        from_json=False,
        consul_profile=None
    ):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None
        idx, res = self.consul.kv.get(
            key,
            index=index,
            recurse=recurse,
            wait=wait,
            token=token,
            consistency=consistency,
            keys=keys,
            separator=separator,
            dc=dc
        )

        if from_json and not keys:
            if isinstance(res, dict):
                res["Value"] = self.from_json(res["Value"])
            if isinstance(res, list):
                for item in res:
                    item["Value"] = self.from_json(item["Value"])

        return (True, [idx, res])
