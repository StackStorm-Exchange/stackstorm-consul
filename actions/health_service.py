from lib import action
from collections import defaultdict


class ConsulServiceHealth(action.ConsulBaseAction):
    def run(self, service, tag=None):
        index, nodes = self.consul.health.service(service, tag=tag)
        s = defaultdict(dict)
        for node in nodes:
            for check in node.get('Checks'):
                try:
                    s[check.get('Node')][check.get('Status')].append(check.get('CheckID'))
                except KeyError:
                    s[check.get('Node')][check.get('Status')] = []
                    s[check.get('Node')][check.get('Status')].append(check.get('CheckID'))
        return s
