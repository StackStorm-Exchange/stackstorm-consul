from lib import action


class ConsulCustomLockAction(action.ConsulBaseAction):
    """
    :key_prefix: (string) Prefix the lock name which is the path in consul's kvstore.
    :max_locks: (integer) Maximum number of concurrent lock holders.
    :name: (string) Name of the key that will hold the locking information.
    """
    def run(
        self,
        key_prefix,
        max_locks=1,
        acquire_timeout=10,
        name="CustomLock",
        node=None,
        checks=None,
        behavior="release",
        ttl=None,
        token=None,
        dc=None,
        consul_profile=None
    ):
        self._create_client(consul_profile)
        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None
        self.lock_manager = action.LockManager(self.consul, key_prefix, name, node, token, dc)
        return self.lock_manager.lock(max_locks, acquire_timeout, checks, behavior, ttl)
