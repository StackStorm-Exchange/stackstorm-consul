# Change Log

## [2.0.0] 03 Nov 2021
### Changed
* Changed underlying consul library from `python-consul` which is no longer maintained to `python-consul2` which is maintained.
* Certain Python3 libraries return byte strings.  We need to decode them in order to correctly json-ify them.

## [1.0.0] 05 Feb 2021

* Drop Python 2.7 support

## [0.6.7] 18 Jun 2019

### Added
  - Add README documentation
  - Properly increment pack.yaml version

## [0.6.6] 16 Feb 2019

### Added
  - Pack supports client key/certificate and CA certificate parameters. issue #22
  - Pack supports consul profiles.  issue #23
  - New Actions
    - ACLInfo
    - ACLUpdate
    - ACLClone

### Changed
  - Fixed destory_session method to return the result.
  - Updated all actions to support ACL Tokens.
  - Require python-consul v1.1.0
  - Changed Actions
    - All actions take a consul_profile parameter.  If no profile is provided the action uses consul_default as defined in the pack configuration.
    - CatalogDeregister takes check_id and token.
    - CatalogServices takes node_meta.
    - CatalogNodes takes node_meta.
    
## [0.6.5] 16 Jul 2018

### Changed
  - Update agent_service_register `tags` to be an array.

## [0.6.4] 16 Jul 2018

### Changed
  - Update agent_service_register `check` to be an object.

## [0.6.3] 25 Jan 2018

### Added
  - Implementation for basic locking using consul key store/session.

### Changed
  - Make acl_list return a list instead of a string.

## [0.6.2]  8 Jan 2018

### Added
  - Support for consul consistency mode.

### Changed
  - Fixed enable/disable for SSL certification verification.

## [0.6.1] 27 Nov 2017

- Linting fixes

## [0.6.0] 16 Nov 2017

### Added the following API calls. (See https://python-consul.readthedocs.io for documentation)
    - AgentChecks
    - AgentForce
    - AgentJoin
    - AgentMaintenance
    - AgentMembers
    - AgentServices
    - EventFire
    - EventList
    - HealthNode
    - HealthState
    - ServiceDeregister
    - ServiceMaintenance
    - ServiceRegister
    - SessionCreate
    - SessionDestroy
    - SessionInfo
    - SessionList
    - SessionNode
    - SessionRenew

### Changed
 - Renamed existing action names to be aligned with the consul API.  This helps logically group
   operations by the subsystem they will apply to.
 - Returned unmodified data from Consul API from some existing actions.  Some of the existing actions
   were masking the metadata returned by the consul API.  This metadata is useful in certain cases.

## 0.5.0

- Updated action `runner_type` from `run-python` to `python-script`

## 0.4.0

 - Added consul.health_service action to query a services status and group the result by hostname
 - Added consul.health_check action to query a services status and group the result by check

## 0.3.0

 - Added consul.list action to get a list of Keys from consul under a given <root> key
 - Added Recursive lookup for consul.get action.
 - Both list and get use the same python runner with additional `recurse`, and `keys`
   parameters with appropriate defaults.

## 0.2.0

 - Added ability to register and deregister a remote service with consul
 - Added ports parameter to consul.query_service. When true, include ports in node list <ip:port>.

## 0.1.0

 - Initial Release
