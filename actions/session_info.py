from lib import action


class ConsulSessionInfoAction(action.ConsulBaseAction):
    def run(self, session_id, index=None, wait=None, consistency=None, dc=None):

        index, services = self.consul.session.info(session_id,
                                                   index=index,
                                                   wait=wait,
                                                   consistency=consistency,
                                                   dc=dc)
        return {'index': index, 'services': services}
