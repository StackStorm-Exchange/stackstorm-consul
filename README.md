[![Build Status](https://circleci.com/gh/StackStorm-Exchange/stackstorm-consul.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/StackStorm-Exchange/stackstorm-consul) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# consul integration pack v0.6.7

> consul
jfryman <james@fryman.io>

[HashiCorp Consul](https://www.consul.io/)

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


## Configuration

The following options are required to be configured for the pack to work correctly.

| Option | Type | Required | Secret | Description |
|---|---|---|---|---|
| `default_profile` | string | True |  | The default consul profile to use in actions when none is given. |
| `consul_profiles` | array | True |  | Consul cluster profiles |


## Actions


The pack provides the following actions:

### acl_clone
_Clones the ACL token 'acl_id'._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `acl_id` | string | True | default | _'acl_id' to clone._ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### catalog_node
_Returns all services provided by *node*._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _Node to query in Consul_ |
| `index` | string | False | default | _The current Consul index, suitable for making subsequent calls to wait for changes since this query was last run._ |
| `wait` | string | False | default | _The maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `consistency` | string | False | default | _Can be either 'default', 'consistent' or 'stale'._ |
| `dc` | string | False | default | _The datacenter to query for nodes._ |
| `token` | string | False | True | _An optional _ACL token_ to apply to this request._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### acl_info
_Returns the token information for 'acl_id'._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `acl_id` | string | True | default | _Fetch information for 'acl_id'._ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### catalog_service
_Returns the nodes providing *service* in the *dc* datacenter._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
| `service` | string | True | default | _The service to query for nodes._ |
| `index` | string | False | default | _The current Consul index, suitable for making subsequent calls to wait for changes since this query was last run._ |
| `wait` | string | False | default | _The maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `tag` | string | False | default | _The list of nodes returned will be filtered by that tag_ |
| `consistency` | string | False | default | _Can be either 'default', 'consistent' or 'stale'._ |
| `dc` | string | False | default | _The datacenter to query for nodes._ |
| `near` | string | False | default | _A node name to sort the resulting list in ascending order based on the estimated round trip time from that node._ |
### acl_list
_Lists all the active ACL tokens._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### agent_checks
_Returns all the checks that are registered with the local agent._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### session_list
_Returns a tuple of (index, sessions) of all active sessions in the datacenter._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `index` | array | False | default | _The current Consul index._ |
| `wait` | string | False | default | _The maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `consistency` | string | False | default | _The consistency mode to use reads._ |
| `dc` | string | False | default | _The datacenter that this agent will communicate with._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### agent_services
_Returns all the services that are registered with the local agent._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### agent_join
_Instructs the agent to attempt to connect to a given address._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `address` | string | True | default | _The ip to connect to._ |
| `wan` | boolean | False | default | _True: causes the agent to attempt to join using the WAN pool._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### service_deregister
_Remove a service from the local agent._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `service_id` | string | False | default | _The id of the service to be removed._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### session_renew
_Extend the expiration by the TTL for sessions that have a TTL._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `session_id` | string | True | default | _The session to renew._ |
| `dc` | string | False | default | _The datacenter that this agent will communicate with._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### event_fire
_Send an event to Consul's gossip protocol._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Key to write in Consul_ |
| `body` | string | True | default | _A Consul-opaque body to be delivered with the event.  Small than 100 bytes!_ |
| `node` | string | False | default | _A Regex which remote agents will filter against to determine if they should store the event._ |
| `service` | string | False | default | _A Regex which remote agents will filter against to determine if they should store the event._ |
| `tag` | string | False | default | _A Regex which remote agents will filter against to determine if they should store the event._ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### health_checks
_Returns the checks of a service_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `service` | string | True | default | _Name of the service to query in Consul._ |
| `index` | integer | False | default | _The current Consul index. Useful to check for changes since last query was run._ |
| `wait` | string | False | default | _Maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `dc` | string | False | default | _The datacenter of the node and defaults to this agents datacenter._ |
| `near` | string | False | default | _A node name to sort the resulting list in ascending order based on the estimated round trip time from that node._ |
| `token` | string | False | True | _An optional ACL token to apply to this request._ |
| `node_meta` | object | False | default | _An optional meta data used for filtering._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### acl_create
_Creates a new ACL token._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Name of token_ |
| `acl_type` | string | True | default | _Type of token_ |
| `rules` | string | False | default | _HCL rules_ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `acl_id` | string | False | default | _Consul Policy ID to apply to the token_ |
### kv_put
_Set value in Consul key/value store._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `key` | string | True | default | _Key to write in Consul_ |
| `value` | string | True | default | _Value of Key to write in Consul_ |
| `cas` | integer | False | default | _An optional flag is used to turn the PUT into a Check-And-Set operation._ |
| `flags` | integer | False | default | _Optional unsigned value between 0 and 2^64-1._ |
| `acquire` | string | False | default | _An optional session_id to attempt the acquisition of a lock._ |
| `release` | string | False | default | _An optional session_id to attempt to release a lock._ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `dc` | string | False | default | _Optional datacenter that you wish to communicate with._ |
| `to_json` | boolean | False | default | _Serialise value to JSON before storing in consul k/v_ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### acl_destroy
_Destroys the ACL token 'acl_id'_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `acl_id` | string | True | default | _Token to destroy_ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### acl_update
_Updates the ACL token 'acl_id'._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Name of token_ |
| `acl_type` | string | True | default | _Type of token_ |
| `rules` | string | False | default | _HCL rules_ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `acl_id` | string | True | default | _Consul Policy ID to update._ |
### agent_maintenance
_Place the agent into 'maintenance mode'._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `enable` | boolean | False | default | _True: enables maintenance mode.  False: disables maintenance mode._ |
| `reason` | string | False | default | _An optional string to aid human operators._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### session_node
_Returns a tuple of (index, session) but filters the sessions returned to only those active for a node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The node to use in the filter when listing active sessions._ |
| `index` | array | False | default | _The current Consul index._ |
| `wait` | string | False | default | _The maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `consistency` | string | False | default | _The consistency mode to use reads._ |
| `dc` | string | False | default | _The datacenter that this agent will communicate with._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### service_maintenance
_Put a given service into _maintenance mode_._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `service_id` | string | True | default | _The id of the service to be removed._ |
| `enable` | boolean | True | default | _True: enable maintenance mode.  False; disable maintenance mode._ |
| `reason` | string | False | default | _An optional string to aid human operators._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### kv_list
_List values from Consul server_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `key` | string | True | default | _Root Key for listing from Consul_ |
| `recurse` | boolean | False | default | _Do a recursive retrieval?_ |
| `keys` | boolean | False | default | _Return a list of keys only_ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### catalog_datacenters
_Real-time query of all known datacenters in Consul_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### catalog_deregister
_Deregister an external service in Consul_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
| `node` | string | True | default | _Node Name/ID_ |
| `service` | string | False | default | _Service Name/ID_ |
| `check_id` | string | False | default | _Check Name/ID_ |
| `dc` | string | default | default | _Optional Data Center ID_ |
### agent_members
_Returns all the members that this agent currently sees._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `wan` | boolean | False | default | _Returns the list of WAN members instead of the LAN members._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### service_register
_Add a new service to the local agent._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _The name of the service._ |
| `service_id` | string | False | default | _The id of the service_ |
| `address` | string | False | default | _IP address. Defaults to the address of the agent._ |
| `port` | string | False | default | _Port._ |
| `tags` | array | False | default | _Tags._ |
| `check` | object | False | default | _An optional health *check* can be created for this service._ |
| `token` | string | False | True | _An optional _ACL token_ to apply to this request._ |
| `enable_tag_override` | boolean | False | default | _An optional bool that enable you to modify a service tags from servers(consul agent role server)_ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### session_destroy
_Destroy an existing session._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `session_id` | string | True | default | _The session id to be destoryed._ |
| `dc` | integer | False | default | _dc is the datacenter that this agent will communicate with._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### test_pack_actions
_Test all actions in the consul pack._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### session_info
_Returns a tuple of (index, session) for the session in the dc datacenter._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `session_id` | string | True | default | _Search for the session which has the id in the datacenter._ |
| `index` | array | False | default | _The current Consul index._ |
| `wait` | string | False | default | _The maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `consistency` | string | False | default | _The consistency mode to use reads._ |
| `dc` | string | False | default | _The datacenter that this agent will communicate with._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### agent_force_leave
_Instructs the agent to force a node into the left state._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The node to change state for._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### event_list
_Fetch events from Consul agent's buffer._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _The type of events to list. An empty string, lists all available._ |
| `index` | integer | False | default | _The current event Consul index_ |
| `wait` | string | False | default | _The maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### session_create
_Create a new session._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | False | default | _An optional human readable name for the session._ |
| `node` | string | False | default | _The node to create the session on_ |
| `checks` | array | False | default | _A list of checks to associate with the session._ |
| `lock_delay` | integer | False | default | _An integer of seconds._ |
| `behavior` | string | False | default | _This controls the behavior when a session is invalidated._ |
| `ttl` | integer | False | default | _Invalidate the session if it is not renewed before the TTL expires._ |
| `dc` | string | False | default | _The datacenter that this agent will communicate with._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### kv_delete
_Deletes a single key or if *recurse* is True, all keys sharing a prefix._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `key` | string | True | default | _Key to Delete from Consul_ |
| `recurse` | boolean | False | default | _Recursively delete keys?_ |
| `cas` | integer | False | default | _An optional flag is used to turn the DELETE into a Check-And-Set operation._ |
| `dc` | string | False | default | _Optional datacenter that you wish to communicate with._ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### health_state
_Returns the checks in a given state_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Name of the supported state (any, unknown, passing, warning, critical)._ |
| `index` | integer | False | default | _The current Consul index. Useful to check for changes since last query was run._ |
| `wait` | string | False | default | _Maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `dc` | string | False | default | _The datacenter of the node and defaults to this agents datacenter._ |
| `near` | string | False | default | _A node name to sort the resulting list in ascending order based on the estimated round trip time from that node._ |
| `token` | string | False | True | _An optional ACL token to apply to this request._ |
| `node_meta` | object | False | default | _An optional meta data used for filtering._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### catalog_services
_Returns all services known about in the *dc* datacenter._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
| `index` | integer | False | default | _The current Consul index. Used to check for changes since last query was run._ |
| `wait` | string | False | default | _Maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `consistency` | string | False | default | _Consul supports 3 different consistency modes for reads. Read Consul's documentation for details._ |
| `dc` | string | False | default | _The datacenter that this agent will communicate with._ |
| `node_meta` | object | False | default | _An optional meta data used for filtering._ |
### custom_lock
_Create a lock or semaphore.  Used for synchronising discret workflows._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `key_prefix` | string | True | default | _KV path to prefix to lock name._ |
| `max_locks` | integer | False | default | _Maximum number of concurrent holders for the lock._ |
| `acquire_timeout` | integer | False | default | _Number of seconds to wait for the lock to be acquired._ |
| `name` | string | False | default | _The name of the lock._ |
| `node` | string | False | default | _The node that will establish and maintain the lock._ |
| `checks` | array | False | default | _A list of the health checks used to determine if the lock should be invalidated._ |
| `behavior` | string | False | default | _The behavior to use when the lock expires (release or delete)._ |
| `ttl` | integer | False | default | _Time to Live before the lock expires (between 10 and 86400 seconds)._ |
| `token` | string | False | True | _An optional ACL token to apply to this request._ |
| `dc` | string | False | default | _Optional datacenter that you wish to communicate with._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### custom_unlock
_Release a lock or semaphore.  Used for synchronising discret workflows._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `session_id` | string | True | default | _The session id that currently holds the lock on the key._ |
| `key_prefix` | string | True | default | _KV path to prefix to lock name._ |
| `name` | string | True | default | _The name of the lock._ |
| `node` | string | False | default | _The node that will establish and maintain the lock._ |
| `token` | string | False | default | _An optional ACL token to apply to this request._ |
| `dc` | string | False | default | _Optional datacenter that you wish to communicate with._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### kv_get
_Get value from Consul key/value store_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `key` | string | True | default | _Key to retrieve from Consul_ |
| `index` | integer | False | default | _The current Consul index, suitable to wait for changes since this query was last run._ |
| `recurse` | boolean | False | default | _Do a recursive retrieval?_ |
| `wait` | string | False | default | _The maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
| `consistency` | string | False | default | _Can be either default, consistent or stale_ |
| `keys` | boolean | False | default | _Return a list of keys only_ |
| `separator` | string | False | default | _Can be used with keys to list keys only up to a given separator character._ |
| `dc` | string | False | default | _Optionally the datacenter to communicate with._ |
| `from_json` | boolean | False | default | _Deserialise retrieved keys as JSON._ |
### health_service
_Returns the nodes and health info of a service_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `service` | string | True | default | _Name of the service to query in Consul._ |
| `index` | integer | False | default | _The current Consul index. Useful to check for changes since last query was run._ |
| `wait` | string | False | default | _Maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `passing` | string | False | default | _Set to True will filter results to only those nodes whose checks are currently passing._ |
| `tag` | string | False | default | _Filter the results by tag._ |
| `dc` | string | False | default | _The datacenter of the node and defaults to this agents datacenter._ |
| `near` | string | False | default | _A node name to sort the resulting list in ascending order based on the estimated round trip time from that node._ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `node_meta` | object | False | default | _An optional meta data used for filtering._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### health_node
_Returns the health info of a node_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The node providing the given service._ |
| `index` | integer | False | default | _The current Consul index. Useful to check for changes since last query was run._ |
| `wait` | string | False | default | _Maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `dc` | string | False | default | _The datacenter of the node and defaults to this agents datacenter._ |
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
### catalog_register
_Register an external service in Consul_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
| `node` | string | True | default | _Node Name/ID_ |
| `address` | string | True | default | _IP Address of the service_ |
| `service` | object | False | default | _An option service Service Name/ID_ |
| `check` | object | False | default | _An optional check to register._ |
| `dc` | string | False | default | _Optional Data Center ID_ |
### catalog_nodes
_Return all nodes known about in the *dc* datacenter._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `token` | string | False | True | _An ACL token to use instead of the agent token._ |
| `consul_profile` | string | False | default | _Consul profile to use to run the action._ |
| `index` | string | False | default | _The current Consul index, suitable for making subsequent calls to wait for changes since this query was last run._ |
| `wait` | string | False | default | _The maximum duration to wait (e.g. '10s') to retrieve a given index._ |
| `consistency` | string | False | default | _Can be either 'default', 'consistent' or 'stale'._ |
| `dc` | string | False | default | _The datacenter to query for nodes._ |
| `near` | string | False | default | _A node name to sort the resulting list in ascending order based on the estimated round trip time from that node._ |
| `node_meta` | object | False | default | _An optional meta data used for filtering._ |



## Sensors

There are no sensors available for this pack.


<sub>Documentation generated using [pack2md](https://github.com/nzlosh/pack2md)</sub>