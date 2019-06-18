[![Build Status](https://circleci.com/gh/StackStorm-Exchange/stackstorm-consul.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/StackStorm-Exchange/stackstorm-consul) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Consul Integration Pack

StackStorm integration pack for [HashiCorp Consul](https://www.consul.io/).

# <a name="QuickStart"></a> Quick Start

Install the pack

``` shell
st2 pack install consul
```

# <a name="Configuration"></a> Configuration
The configuration for this pack is used to specify connection information for all Consul servers you'll be communicating with. The location for the config file is `/opt/stackstorm/configs/consul.yaml`. An example configuration located in the repo named [consul.yaml.example](./consul.yaml.example) can be copied to `/opt/stackstorm/configs/consul.yaml` and edited as required.

It should contain:

* `default_profile` - URL for the Vault server
* `consul_profiles` - Mapping of name to an object containing Consul profile settings
  * `name` - Name of the consul profile
  * `host` - Consul server IP/name.  Default 127.0.0.1
  * `port` - Consul server port. Default 8500
  * `token` - Consul API token
  * `scheme` - Consul scheme to use. Default http
  * `verify` - Verify the SSL certificate for HTTPS requests. Default false (this option is ignored if ca_cert_path is supplied)
  * `ca_cert_path` - CA Certificate path. Defaults to empty string. When path is provided, SSL certificates are verified
  * `client_cert_path` - Client side certificates for HTTPS request
  * `client_key_path` - Client private key for HTTPS request
  * `preserve_varenv` - Enable preservation of environment variables.  If disable, all CONSUL_* environment variables are deleted from the action execution
  * `consistency` - The consistency mode to use by default for all reads that support the consistency option

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## <a name="SchemaExample"></a> Schema Examples

``` yaml
---
consul_profiles:
  -
    name: production
    ca_cert_path: /etc/ssl/certs/ca.pem
    client_cert_path: /etc/ssl/certs/client-cert.pem
    client_key_path: /etc/ssl/private/client-key.pem
    consistency: default
    host: 127.0.0.1
    port: 8500
    scheme: https
    token: 11111111-bbbb-aaaa-cccc-222222222222
    verify: true
    preserve_varenv: false
  -
    name: dev
    ca_cert_path: /etc/ssl/certs/dev-ca.pem
    client_cert_path: /etc/ssl/certs/dev-client-cert.pem
    client_key_path: /etc/ssl/private/dev-client-key.pem
    consistency: default
    host: 10.11.12.13
    port: 8500
    scheme: https
    token: 22222222-bbbb-aaaa-cccc-444444444444
    verify: false
    preserve_varenv: false
default_profile: production
```

# Actions

Below is a list of currently available actions:

* `acl_clone` -  Clones the ACL token 'acl_id'.
* `acl_create` -  Creates a new ACL token.
* `acl_destroy` -  Destroys the ACL token 'acl_id'
* `acl_info` -  Returns the token information for 'acl_id'.
* `acl_list` -  Lists all the active ACL tokens.
* `acl_update` -  Updates the ACL token 'acl_id'.
* `agent_checks` -  Returns all the checks that are registered with the local agent.
* `agent_force_leave` -  Instructs the agent to force a node into the left state.
* `agent_join` -  Instructs the agent to attempt to connect to a given address.
* `agent_maintenance` -  Place the agent into 'maintenance mode'.
* `agent_members` -  Returns all the members that this agent currently sees.
* `service_deregister` -  Remove a service from the local agent.
* `service_maintenance` -  Put a given service into _maintenance mode_.
* `service_register` -  Add a new service to the local agent.
* `agent_services` -  Returns all the services that are registered with the local agent.
* `catalog_datacenters` -  Real-time query of all known datacenters in Consul
* `catalog_deregister` -  Deregister an external service in Consul
* `catalog_node` -  Returns all services provided by *node*.
* `catalog_nodes` -  Return all nodes known about in the *dc* datacenter.
* `catalog_register` -  Register an external service in Consul
* `catalog_service` -  Returns the nodes providing *service* in the *dc* datacenter.
* `catalog_services` -  Returns all services known about in the *dc* datacenter.
* `custom_lock` -  Create a lock or semaphore.  Used for synchronising discret workflows.
* `custom_unlock` -  Release a lock or semaphore.  Used for synchronising discret workflows.
* `event_fire` -  Send an event to Consul's gossip protocol.
* `event_list` -  Fetch events from Consul agent's buffer.
* `health_checks` -  Returns the checks of a service
* `health_node` -  Returns the health info of a node
* `health_service` -  Returns the nodes and health info of a service
* `health_state` -  Returns the checks in a given state
* `kv_delete` -  Deletes a single key or if *recurse* is True, all keys sharing a prefix.
* `kv_get` -  Get value from Consul key/value store
* `kv_list` -  List values from Consul server
* `kv_put` -  Set value in Consul key/value store.
* `session_create` -  Create a new session.
* `session_destroy` -  Destroy an existing session.
* `session_info` -  Returns a tuple of (index, session) for the session in the dc datacenter.
* `session_list` -  Returns a tuple of (index, sessions) of all active sessions in the datacenter.
* `session_node` -  Returns a tuple of (index, session) but filters the sessions returned to only those active for a node.
* `session_renew` -  Extend the expiration by the TTL for sessions that have a TTL.
* `test_pack_actions` -  Test all actions in the consul pack.
