.. :changelog:

Release History
===============
2.0.72
++++++
* no changes

2.0.71
++++++
* Added ossrdbmsResourceId to cloud.py.
* properly handle type errors caused by invalid JMESPath queries in core.util.handle_exception
* `--query`: properly handle type errors caused by invalid JMESPath queries.

2.0.70
++++++
* no changes

2.0.69
++++++
* Fixed issue where `--subscription` would appear despite being suppressed on certain commands.

2.0.68
++++++
* extension removal: surface io errors as warnings instead of verbose info

2.0.67
++++++
* BREAKING CHANGE: `min_profile` kwarg is no longer supported. Use `resource_type` instead.

2.0.66
++++++
* output: Fix bug where commands fail if `--output yaml` is used with `--query`

2.0.65
++++++
* auth: polish common AAD service errors with actionables to overcome
* Fixed issue where the CLI would load extensions that were not compatible with its core version.
* Fix issue if clouds.config is corrupt

2.0.64
++++++
* Upgrade to knack 0.6.1

2.0.63
++++++
* Minor fixes

2.0.62
++++++
* Fix issue where some extensions showed a version of "Unknown" and could not be updated.

2.0.61
++++++
* Fix issues with dev extension incompatibility.
* Error handling now points customers to issues page.

2.0.60
++++++
* cloud set: fix a bogus error about subscription not found

2.0.59
++++++
* Fix issue where in some instances using `--subscription NAME` would throw an exception.

2.0.58
++++++
* `az --version` now displays a notification if you have packages that can be updated.
* Fixes regression where `--ids` could no longer be used with JSON output.

2.0.57
++++++
* Hot fix for issue 8399_.

.. _8399: https://github.com/Azure/azure-cli/issues/8399

2.0.56
++++++
* auth: enable tenant level account for managed service identity

2.0.55
++++++
* `--output`: Introduce 'none' as an output format option.

2.0.54
++++++
* Minor fixes

2.0.53
++++++
* Minor fixes

2.0.52
++++++
* core: support cross tenant resource provisioning for multi-tenant service principal
* Fix bug where ids piped from a command with tsv output is improperly parsed.

2.0.51
++++++
* msi login: do not reuse subscription name for identity info

2.0.50
++++++
* auth: support service principal sn+issuer auth

2.0.49
++++++
* Fix issue with `--ids` where `--subscription` would take precedence over the subscription in `--ids`.
  Adding explicit warnings when name parameters would be ignored by use of `--ids`.

2.0.48
++++++
* Fix Homebrew.

2.0.47
++++++
* Introduces generic behavior to handle "Bad Request" errors.

2.0.46
++++++
* Fixed issue where `az vm create --generate-ssh-keys` overwrites private key
  file if public key file is missing. (#4725, #6780)

2.0.45
++++++
* Fix issue of loading empty configuration file.
* Azure Stack: support new profile 2018-03-01-hybrid

2.0.44
++++++
* use knack/0.4.2 with fix towards numeric value display in table output
* Introduce YAML output format
* Overhaul telemetry upload mechanism

2.0.43
++++++
* Consuming mult api azure.mgmt.authorization package for stack support
* Minor fixes

2.0.42
++++++
* login: support browser based login in WSL bash window
* Adds `--force-string` flag to all generic update commands.

2.0.41
++++++
* Minor fixes
* Update PyYAML dependency to 4.2b4

2.0.40
++++++
* authentication: support authorization code flow for interactive login

2.0.39
++++++
* MSI packaging change

2.0.38
++++++
* Add global support for `--subscription` to most commands.

2.0.37
++++++
* Minor fixes

2.0.36	
++++++	
* Minor fixes

2.0.35
++++++
* Added method of registering `show` commands to fail with exit code of 3.

2.0.34
++++++
* core: support cross tenant resource referencing
* Improve telemetry upload reliability
  1. Remove retry. Once failed stop uploading.
  2. Update the process start configuration to prevent upload process from blocking the CLI process.

2.0.33
++++++
* core: ignore FileNotFoundError error on expanding `@`

2.0.32
++++++
* auth: fix a unhandled exception when retrieve secrets from a service principal account with cert
* auth: improve the logic of detecting msi based account
* Added limited support for positional arguments.
* Fix issue where `--query` could not be used with `--ids`. [#5591](https://github.com/Azure/azure-cli/issues/5591)
* Improves piping scenarios from commands when using `--ids`. Supports `-o tsv` with a query specified or `-o json`
  without specifying a query.
* Display command suggestions on error if users have typo in their commands
* More friendly error when users type `az ''`
* Support custom resource types for command modules and extensions

2.0.31
++++++
* Allow other sources to add additional tab completion choices via event hook
* `sdist` is now compatible with wheel 0.31.0

2.0.30
++++++
* Show message for extensions marked as preview on -h.

2.0.29
++++++
* Support Autorest 3.0 based SDKs
* Support mechanism for a command module to suppress the loading of particular extensions.

2.0.28
++++++
* Fix issue that required extension to use `client_arg_name` keyword argument. This is no longer necessary.
* Allow extensions to send telemetry with custom instrumentation key
* Enable HTTP logging with --debug

2.0.27
++++++
* auth: key on both subscription id and name on msi login
* Add events module in core for EVENT_INVOKER_PRE_CMD_TBL_TRUNCATE

2.0.26
++++++
* Support raw token retrival in MSI context
* Remove polling indicator string after finishing LRO on Windows cmd.exe
* Warning that appears when using a configured default has been changed to an INFO level entry. Use --verbose to see.
* Add a progress indicator for wait command

2.0.25
++++++
* Minor fixes

2.0.24
++++++
* Minor fixes

2.0.23
++++++
* Minor fixes

2.0.22
++++++
* Minor fixes
* Modified the AZURE_US_GOV_CLOUD's AAD authority endpoint from login.microsoftonline.com to login.microsoftonline.us.
* Introduce SDKProfile to support azure-mgmt-compute 3.1.0rc1 and integrated profile support.
* Improve telemetry: remove inifinity retry loop from SynchronousSender.

2.0.21
++++++
* Minor fixes

2.0.20
++++++
* 2017-03-09-profile is updated to consume MGMT_STORAGE API version '2016-01-01'

2.0.19
++++++
* skipped version to align package versions with azure-cli

2.0.18 (2017-10-09)
+++++++++++++++++++
* Azure Stack: handle adfs authority url with a trailing slash

2.0.17 (2017-09-22)
+++++++++++++++++++
* minor fixes
* Address problems with 'AzureCloud' clouds.config file in concurrent scenarios
* More user-friendly handling of invalid cloud configurations
* `availability-set create`: Fixed issue where this command would not work on Azure Stack.

2.0.16 (2017-09-11)
+++++++++++++++++++
* Enable command module to set its own correlation ID in telemetry
* Fix json dump issue when telemetry is set to diagnostics mode

2.0.15 (2017-08-31)
+++++++++++++++++++
* minor fixes

2.0.14 (2017-08-28)
+++++++++++++++++++

* Add legal note to --version

2.0.13 (2017-08-11)
+++++++++++++++++++
* fixes issue where `three_state_flag` would not work correctly if custom labels were used.

2.0.12 (2017-07-27)
+++++++++++++++++++
* output sdk auth info for service principals with certificates

2.0.11 (2017-07-07)
+++++++++++++++++++
* minor fixes

2.0.10 (2017-06-21)
+++++++++++++++++++
* Fix deployment progress exceptions

2.0.9 (2017-06-14)
++++++++++++++++++
* use arm endpoint from the current cloud to create subscription client

2.0.8 (2017-06-13)
++++++++++++++++++
* Improve concurrent handling of clouds.config file (#3636)
* Refresh client request id for each command execution.
* core: Create subscription clients with right SDK profile (#3635)
* Progress Reporting for template deployments (#3510)
* output: add support for picking table output fields through jmespath query  (#3581)
* Improves the muting of parse args + appends history with gestures (#3434)
* Create subscription clients with right SDK profile
* Move all existing recording files to latest folder
* [VM/VMSS] Fix idempotency for VM/VMSS create (#3586)

2.0.7 (2017-05-30)
++++++++++++++++++
* Command paths are no longer case sensitive.
* Certain boolean-type parameters are no longer case sensitive.
* Support login to ADFS on prem server like Azure Stack
* Fix concurrent writes to clouds.config (#3255)

2.0.6 (2017-05-09)
++++++++++++++++++
* RP Auto-Reg: capture missing subscription registration error on LRO (#3268)

2.0.5 (2017-05-05)
++++++++++++++++++
* core: capture exceptions caused by unregistered provider and auto-register it
* login: avoid the bad exception when the user account has no subscription and no tenants
* perf: persist adal token cache in memory till process exits (#2603)

2.0.4 (2017-04-28)
++++++++++++++++++
* Fix bytes returned from hex fingerprint -o tsv (#3053)
* Enhanced Key Vault Certificate Download and AAD SP Integration (#3003)
* Add Python location to az —version (#2986)
* login: support login when there are no subscriptions (#2929)

2.0.3 (2017-04-17)
++++++++++++++++++
* core: fix a failure when login using a service principal twice (#2800)
* core: Allow file path of accessTokens.json to be configurable through an env var(#2605)
* core: Allow configured defaults to apply on optional args(#2703)
* core: Improved performance
* core: Support for multiple API versions
* core: Custom CA Certs - Support setting REQUESTS_CA_BUNDLE environment variable
* core: Cloud configuration - use 'resource manager' endpoint if 'management' endpoint not set

2.0.2 (2017-04-03)
++++++++++++++++++
* Avoid loading azure.storage simply to getting an internal string to be used in exceptional cases when trying to instantiate a storage data plane client. (#2673)
* [KeyVault] KeyVault create fix (#2648)
* Azure DevTest Lab command module in CLI (#2631)
* Allow = in generic update values. (#2638)
* Allowing command module authors to inject formatter class. (#2622)
* Login: skip erroneous tenant (#2634)
* Removed duplicate sql utils code (#2629)
* Refactoring SDK reflaction utils into core.sdk (#2599)
* Add blank line after each example. (#2574)
* login: set default subscription to one with the state of "Enabled" (#2575)
* Add wait commands and --no-wait support (#2524)
* choice list outside of named arguments (#2521)
* core: support login using service principal with a cert (#2457)
* Revert "get choices for completion (#2476)" (#2516)
* Add prompting for missing template parameters. (#2364)
* [KeyVault] Command fixes (#2474)
* get choices for completion (#2476)
* Fix issue with "single tuple" options_list (#2495)

2.0.1 (2017-03-13)
++++++++++++++++++

* Support setting default values for common arguments like default resource group, default web, default vm
* Fix resource_id parsing to accept 'resourcegroups'
* Mitigate AI SDK's problem with numeric in properties
* Fix KeyError: 'environmentName' on 'az account list'
* Support login to specific tenant

2.0.0 (2017-02-27)
++++++++++++++++++

* GA release


0.1.2rc2 (2017-02-22)
+++++++++++++++++++++

* Telemetry: Generate unique event ID for each exception.
* Show privacy statement on first invocation of ‘az’ command.


0.1.2rc1 (2017-02-17)
+++++++++++++++++++++

* Show commands return empty string with exit code 0 for 404 responses
* Fix: Ensure known clouds are always in cloud config
* Handle cloud switching in more user friendly way + remove context
* Add support for prompts for yes / no with -y option
* Remove list output


0.1.1b3 (2017-01-30)
++++++++++++++++++++

* Support Python 3.6.
* Support prompt for confirmations.
* Ensure booleans are lowercase in tsv.
* Handle bom on reading file.
* Catch exceptions whilst trying to check if PyPI module is available.
* Fix TSV output unable to decode non-ascii characters.
* Return empty array '[]' instead of nothing for json output.
* Table alphabetical sort if no query or table transformer set.
* Add user path expansion to file type parameters.
* Print parse errors before usage statement.


0.1.1b2 (2017-01-19)
++++++++++++++++++++

* Fix argcomplete 'default_completer' error after release of argcomplete 1.8.0.
* [Telemetry] Update instrumentation key for telemetry and use new DataModel.


0.1.1b1 (2017-01-17)
++++++++++++++++++++

* Improve @file handling logic.
* Telemetry code improvements and readability changes.
* Fix incorrect parsing of argument name when description contains ':'
* Correct endpoints for USGov.


0.1.0b11 (2016-12-12)
+++++++++++++++++++++

* Preview release.
