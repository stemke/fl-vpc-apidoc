import json
import re
from urllib.parse import parse_qsl, urlparse

from openapi_tests import _adapter
from openapi_tests._helpers import (
    ID_KEYS,
    REQUIRED_PARAMS,
    RESOURCE_GROUP_ID_REGEX,
    RESPONSE_KEYS,
    SUBNET_NAME_REGEX,
    URL_REGEX,
    check_required_params,
    check_valid_params,
    check_valid_subnet,
)

from openapi_tests._adapter import API_ENDPOINT, session


# TESTS STARTS HERE
# GET /subnets
def test_get_subnets():
    res = session.get(f"{API_ENDPOINT}/v1/subnets?version=2021-05-06&generation=2")
    query_params = dict(parse_qsl(urlparse(res.url).query))

    optional_params = [
        "start",
        "limit",
        "resource_group.id",
        "routing_table.id",
        "routing_table.name",
        "ipv4_cidr_block",
    ]

    check_required_params(res)

    for k, v in query_params.items():
        assert k in (optional_params + REQUIRED_PARAMS)
        # check if query contains optional params
        if k in optional_params:
            # check if query params has any value
            assert v

        if k == "limit":
            assert v.isdigit()
            assert 1 <= v <= 100

    data = res.json()
    required_response_keys = ["first", "limit", "subnets", "total_count"]

    optional_response_key = ["next"]

    for k, v in data.items():
        assert k in (required_response_keys + optional_response_key)

        if k == "limit":
            assert 1 <= v <= 100

        if k == "total_count":
            assert v >= 0

        if k == "next":
            assert re.match(URL_REGEX, v.get("href"))

    subnets = data.get("subnets", [])
    for subnet in subnets:
        check_valid_subnet(subnet)


# POST /subnets
def test_post_subnets():
    body = {
        "name": "my-subnet-1",
        "ipv4_cidr_block": "10.0.1.0/24",
        "ip_version": "ipv4",
        "zone": {"name": "us-south-1"},
        "vpc": {"id": _adapter.vpc_id},
        "network_acl": {"id": "r006-848ce071-a794-4948-833b-82fba500dc61"},
    }

    res = session.post(
        f"{API_ENDPOINT}/v1/subnets?version=2021-05-06&generation=2", json=body
    )

    check_required_params(res)

    allowed_body_params = [
        "vpc",
        "ip_version",
        "name",
        "network_acl",
        "resource_group",
        "routing_table",
        # to double check
        "ipv4_cidr_block",
        "total_ipv4_address_count",
        "zone",
    ]

    required_body_data = ["vpc"]
    req_body = json.loads(res.request.body)

    for param in required_body_data:
        assert param in req_body.keys()

    vpc_body = req_body.get("vpc")
    check_valid_params(RESPONSE_KEYS, vpc_body)

    for k, v in vpc_body.items():
        assert k in ID_KEYS

    for k, v in req_body.items():
        assert k in allowed_body_params + ["public_gateway"]

        if k == "ip_version":
            assert v in ["ipv4"]

        if k == "name":
            assert 1 <= len(v) <= 63
            assert re.match(SUBNET_NAME_REGEX, v)

        if k == "network_acl":
            assert len(v.keys()) == 1
            check_valid_params(ID_KEYS, v)

        if k == "public_gateway":
            assert len(v.keys()) == 1
            check_valid_params(ID_KEYS, v)

        if k == "resource_group":
            assert re.match(RESOURCE_GROUP_ID_REGEX, v.get("id"))

        if k == "routing_table":
            assert len(v.keys()) == 1
            check_valid_params(["id", "href"], v)

    # testing for response
    for k in ID_KEYS + allowed_body_params:
        assert k in res.json().keys()

    check_valid_subnet(res.json())


# PATCH /subnets/{id}
def test_patch_subnet_by_id():

    subnet_id = _adapter.subnet_id
    body = {"name": "my-subnet-1-modified"}

    res = session.patch(
        f"{API_ENDPOINT}/v1/subnets/{subnet_id}?version=2021-05-06&generation=2",
        data=body,
    )

    assert re.search(r"v1/subnets/(.*?)\?[vg]", res.url)
    check_required_params(res)

    request_body = dict(parse_qsl(res.request.body))
    name = request_body.get("name", "")
    assert "name" in request_body.keys()
    assert re.match(SUBNET_NAME_REGEX, name)
    assert 1 <= len(name) <= 63

    assert body["name"] == res.json().get("name")
    check_valid_subnet(res.json())


# DELETE /subnets/{id}
def test_delete_subnet_by_id():
    subnet_id = _adapter.subnet_id

    res = session.delete(
        f"{API_ENDPOINT}/v1/subnets/{subnet_id}?version=2021-05-06&generation=2"
    )

    assert re.search(r"v1/subnets/(.*?)\?[vg]", res.url)
    assert res.status_code == 204


def test_get_subnet_by_id():
    subnet_id = _adapter.subnet_id

    res = session.get(
        f"{API_ENDPOINT}/v1/subnets/{subnet_id}?version=2021-05-06&generation=2"
    )

    check_required_params(res)
    check_valid_subnet(res.json())
