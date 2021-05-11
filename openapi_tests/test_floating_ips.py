import re
from urllib.parse import parse_qsl, urlparse

from openapi_tests import _adapter
from openapi_tests._helpers import (
    REQUIRED_PARAMS,
    SUBNET_NAME_REGEX,
    URL_REGEX,
    check_valid_floating_ip,
    check_required_params,
)

from openapi_tests._adapter import API_ENDPOINT, session


# TESTS STARTS HERE
# GET /floating_ips
def test_get_floating_ips():
    res = session.get(f"{API_ENDPOINT}/v1/floating_ips?version=2021-05-06&generation=2")
    query_params = dict(parse_qsl(urlparse(res.url).query))

    optional_params = ["start", "limit", "resource_group.id"]

    # -- testing request params
    check_required_params(res)

    for k, v in query_params.items():
        # check that query has the correct params
        assert k in (REQUIRED_PARAMS + optional_params)
        # check if query params has any value
        assert v

        if k == "limit":
            assert v.isdigit()
            assert 1 <= v <= 100

    # -- testing response
    required_response_keys = ["limit", "first", "total_count", "floating_ips"]
    response_keys = required_response_keys + ["next"]
    data = res.json()

    for k in required_response_keys:
        assert k in data.keys()

    for k, v in data.items():
        assert k in response_keys

        if k == "total_count":
            assert v >= 0

        elif k == "floating_ips" and v:
            for ip in v:
                check_valid_floating_ip(ip)

        elif k == "limit":
            assert 1 <= v <= 100

        elif k == "next":
            assert re.match(URL_REGEX, v.get("href", ""))

        else:
            assert v


# GET /floating_ips/id
def test_floating_ips_by_id():
    floating_ips_id = _adapter.floating_ips_id

    res = session.get(
        f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}?version=2021-05-06&generation=2"
    )

    check_required_params(res)

    # testing response
    check_valid_floating_ip(res.json())


# POST /floating_ips
def test_post_floating_ips():
    body = {
        "name": "my-floating-ip-1",
        "target": {"id": "5a07e83d-c1f3-4df2-bcec-41b09c006847"},
    }

    res = session.post(
        f"{API_ENDPOINT}/v1/floating_ips?version=2021-05-06&generation=2", json=body
    )

    allowed_body_data = ["name", "resource_group", "target"]

    for k, v in body.items():
        assert k in allowed_body_data

    check_required_params(res)
    check_valid_floating_ip(res.json())


# PATCH /floating_ips/{id}
def test_patch_key_by_id():
    floating_ips_id = _adapter.floating_ips_id
    body = {"name": "my-floating-ip-updated"}

    res = session.patch(
        f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}?version=2021-05-06&generation=2",
        json=body,
    )

    assert re.search(r"v1/floating_ips/(.*?)\?[vg]", res.url)
    check_required_params(res)
    data = res.json()
    name = data.get("name", "")

    assert "name" in body.keys()
    assert re.match(SUBNET_NAME_REGEX, name)
    assert 1 <= len(name) <= 63
    check_valid_floating_ip(data)

    assert data.get("name") == body.get("name")


# DELETE /floating_ips/{id}
def test_delete_key_by_id():
    floating_ips_id = _adapter.floating_ips_id

    res = session.delete(
        f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}?version=2021-05-06&generation=2"
    )

    check_required_params(res)

    assert re.search(r"v1/floating_ips/(.*?)\?[vg]", res.url)
    assert res.status_code == 204
