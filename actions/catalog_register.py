from lib import action


class ConsulCatalogRegisterAction(action.ConsulBaseAction):
    def run(self, node, service, address, port, tags, dc):

        definition = {"Service": service, "Port": port, "Tags": tags}
        return (True, self.consul.catalog.register(node, address, service=definition, dc=dc))
