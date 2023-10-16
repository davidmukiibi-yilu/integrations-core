# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def shared_skip_proxy():
    return False


def shared_timeout():
    return 10


def instance_blacklist_project_names():
    return []


def instance_collect_hypervisor_load():
    return True


def instance_collect_hypervisor_metrics():
    return True


def instance_collect_network_metrics():
    return True


def instance_collect_project_metrics():
    return True


def instance_collect_server_diagnostic_metrics():
    return True


def instance_collect_server_flavor_metrics():
    return True


def instance_domain_id():
    return 'default'


def instance_endpoint_interface():
    return 'public'


def instance_exclude_network_ids():
    return []


def instance_exclude_server_ids():
    return []


def instance_ironic_microversion():
    return '1.80'


def instance_paginated_limit():
    return 1000


def instance_use_agent_proxy():
    return True


def instance_use_legacy_check_version():
    return False


def instance_use_shortname():
    return False


def instance_username():
    return 'admin'


def instance_whitelist_project_names():
    return []
