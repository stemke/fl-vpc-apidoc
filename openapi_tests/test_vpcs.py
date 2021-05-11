import re
from urllib.parse import parse_qsl, urlparse

from openapi_tests import _adapter
from openapi_tests._helpers import (
    REQUIRED_PARAMS,
    RESOURCE_GROUP_ID_REGEX,
    SUBNET_NAME_REGEX,
    URL_REGEX,
    check_required_params,
    check_valid_vpc,
)

from openapi_tests._adapter import API_ENDPOINT, session


# TESTS STARTS HERE
# GET /vpcs
def test_get_vpcs():
    res = session.get(f"{API_ENDPOINT}/v1/vpcs?version=2021-05-06&generation=2")
    query_params = dict(parse_qsl(urlparse(res.url).query))

    optional_params = ["start", "limit", "resource_group.id", "classic_access"]

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

        elif k == "classic_access":
            assert v in ["true", "false"]

    # -- testing response
    required_response_keys = ["limit", "first", "total_count", "vpcs"]
    response_keys = required_response_keys + ["next"]
    data = res.json()

    for k in required_response_keys:
        assert k in data.keys()

    for k, v in data.items():
        assert k in response_keys

        if k == "total_count":
            assert v >= 0

        elif k == "vpcs" and v:
            for vpc in v:
                check_valid_vpc(vpc)

        elif k == "limit":
            assert 1 <= v <= 100

        elif k == "next":
            assert re.match(URL_REGEX, v.get("href", ""))

        else:
            assert v


# GET /vpcs/id
def test_vpc_by_id():
    vpc_id = _adapter.vpc_id
    res = session.get(
        f"{API_ENDPOINT}/v1/vpcs/{vpc_id}?version=2021-05-06&generation=2"
    )

    check_required_params(res)

    # testing response
    check_valid_vpc(res.json())


# POST /vpcs
def test_post_vpcs():
    body = {"name": "my-vpc-2"}

    res = session.post(
        f"{API_ENDPOINT}/v1/vpcs?version=2021-05-06&generation=2", json=body
    )

    optional_body_data = [
        "VPCPrototype",
        "address_prefix_management",
        "classic_access",
        "name",
        "resource_group",
    ]

    for k, v in body.items():
        assert k in optional_body_data

        if k == "address_prefix_management":
            assert v in ["auto", "manual"]

        elif k == "classic_access":
            assert v in ["true", "false"]

        elif k == "name":
            assert 1 <= len(v) <= 63
            assert re.match(SUBNET_NAME_REGEX, v)

        elif k == "resource_group":
            assert re.match(RESOURCE_GROUP_ID_REGEX, v.get("id"))

    check_required_params(res)
    check_valid_vpc(res.json())


# PATCH /vpcs/{id}
def test_patch_vpc_by_id():
    vpc_id = _adapter.vpc_id
    body = {"name": "test2-updated"}

    res = session.patch(
        f"{API_ENDPOINT}/v1/vpcs/{vpc_id}?version=2021-05-06&generation=2", json=body
    )

    assert re.search(r"v1/vpcs/(.*?)\?[vg]", res.url)
    check_required_params(res)
    data = res.json()
    name = data.get("name", "")

    assert "name" in body.keys()
    assert re.match(SUBNET_NAME_REGEX, name)
    assert 1 <= len(name) <= 63
    check_valid_vpc(data)

    assert data.get("name") == body.get("name")


# DELETE /vpcs/{id}
def test_delete_vpc_by_id():
    vpc_id = _adapter.vpc_id

    res = session.delete(
        f"{API_ENDPOINT}/v1/vpcs/{vpc_id}?version=2021-05-06&generation=2"
    )

    check_required_params(res)

    assert re.search(r"v1/vpcs/(.*?)\?[vg]", res.url)
    assert res.status_code == 204
