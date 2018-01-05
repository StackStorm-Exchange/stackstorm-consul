from lib import action


class ConsulCustomUnLockAction(action.ConsulBaseAction):
    """
    :session_id: (string) the session id that holds the lock to a key.
    :key_prefix: (string) Prefix the lock name which is the path in consul's kvstore.
    :name: (string) Name of the key that will hold the locking information.
    """
    def run(self, session_id, key_prefix, name, node=None, token=None, dc=None):
        self.lock_manager = action.LockManager(self.consul, key_prefix, name, node, token, dc)
        return self.lock_manager.unlock(session_id)
