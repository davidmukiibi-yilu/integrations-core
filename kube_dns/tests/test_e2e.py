import pytest

from datadog_checks.base import AgentCheck


@pytest.mark.e2e
def test_e2e(dd_agent_check, aggregator, instance):

    with pytest.raises(Exception):
        dd_agent_check(instance, rate=True)
    endpoint_tag = "endpoint:" + instance.get('prometheus_endpoint')
    tags = instance.get('tags').append(endpoint_tag)
    aggregator.assert_service_check("kubedns.prometheus.health", AgentCheck.CRITICAL, count=2, tags=tags)
