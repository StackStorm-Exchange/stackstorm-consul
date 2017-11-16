from lib import action


class ConsulSessionCreateAction(action.ConsulBaseAction):
    def run(self,
            name=None,
            node=None,
            checks=None,
            lock_delay=15,
            behavior='release',
            ttl=None,
            dc=None):

        return (True, self.consul.session.create(
            name=name,
            node=node,
            checks=checks,
            lock_delay=lock_delay,
            behavior=behavior,
            ttl=ttl,
            dc=dc))
