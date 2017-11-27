from lib import action


class ConsulSessionInfoAction(action.ConsulBaseAction):
    def run(self, session_id, index=None, wait=None, consistency=None, dc=None):

        return (True, self.consul.session.info(
            session_id,
            index=index,
            wait=wait,
            consistency=consistency,
            dc=dc))
