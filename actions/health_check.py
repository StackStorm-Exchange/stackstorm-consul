from lib import action
from collections import defaultdict


class ConsulCheckHealth(action.ConsulBaseAction):
    def run(self, service):
        index, nodes = self.consul.health.checks(service=service)
        s = defaultdict(dict)
        for node in nodes:
            try:
                s[node.get('CheckID')][node.get('Status')].append(node.get('Node'))
            except KeyError:
                s[node.get('CheckID')][node.get('Status')] = []
                s[node.get('CheckID')][node.get('Status')].append(node.get('Node'))
        return s
