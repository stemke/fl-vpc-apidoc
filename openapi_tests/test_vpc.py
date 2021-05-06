from openapi_tests.helpers import (
    API_ENDPOINT,
    check_required_params,
    REQUIRED_PARAMS,
    session,
    is_date,
    check_valid_keys,
    URL_REGEX,
    ID_REGEX,
    NAME_REGEX,
)

from urllib.parse import parse_qsl, urlparse
import re
import json


# TESTS STARTS HERE
# GET /vpcs
def test_get_vpcs():
    res = session.get(f"{API_ENDPOINT}/v1/vpcs?version=2021-04-20&generation=2")
    query_params = dict(parse_qsl(urlparse(res.url).query))

    optional_params = ["start", "limit", "resource_group.id", "classic_access"]
    valid_vpc_keys = ['classic_access', 'created_at', 'crn', 'default_network_acl', 'default_routing_table', 'default_security_group', 'href', 'id', 'name', 'resource_group', 'status', 'cse_source_ips']

    # -- testing request params
    check_required_params(res)

    for k, v in query_params.items():
        # check that query has the correct params
        assert k in (REQUIRED_PARAMS + optional_params)
        # check if query params has any value
        assert v

        if k == "limit":
            assert v.isdigit()
            assert int(v) in range(1, 101)

        if k == "classic_access":
            assert v in ["true", "false"]

    # -- testing response
    required_response_keys = ["limit", "first", "total_count", "vpcs"]

    data = res.json()
    for k, v in data.items():
        assert k in required_response_keys

        if k == "total_count":
            assert v >= 0

        elif k == "vpcs" and v:
            network_acl_keys = ["crn", "href", "id", "name", "deleted"]
            routing_table_keys = ["href", "id", "name", "resource_type", "deleted"]

            for vpc in v:
                for key in vpc.keys():
                    print(key)
                # print()
                    assert key in valid_vpc_keys

                assert isinstance(vpc.get("classic_access"), bool)
                assert is_date(vpc.get("created_at"))
                assert vpc.get("crn").startswith("crn:")

                check_valid_keys(network_acl_keys, vpc.get("default_network_acl"))
                check_valid_keys(network_acl_keys, vpc.get("default_security_group"))

                for rt_key, rt_val in vpc.get("default_routing_table").items():
                    assert rt_key in routing_table_keys
                    assert rt_val

                    if rt_key == "href":
                        assert re.match(URL_REGEX, rt_val)

                    if rt_key == "id":
                        assert re.match(ID_REGEX, rt_val)

                    if rt_key == "name":
                        assert 1 <= len(rt_val) <= 63
                        assert re.match(NAME_REGEX, rt_val)

                    if rt_key == "resource_type":
                        assert rt_val in ["routing_table"]

                    if rt_key == "deleted":
                        assert re.match(URL_REGEX, rt_val.get("more_info"))


        else:
            assert v

        if k == "limit":
            assert 1 <= v <= 100


# GET /vpcs/id
def test_vpc_by_id():
    vpc_id = "r006-192412ca-4ab4-4e00-a852-188047f8698d"
    res = session.get(
        f"{API_ENDPOINT}/v1/vpcs/{vpc_id}?version=2021-04-20&generation=2"
    )

    check_required_params(res)


# POST /vpcs
def test_post_vpcs():
    body = {"name": "r006-192412ca-4ab4-4e00-a852-188047f8698d"}

    res = session.post(
        f"{API_ENDPOINT}/v1/vpcs?version=2021-04-20&generation=2", json=body
    )

    optional_body_data = [
        "VPCPrototype",
        "address_prefix_management",
        "classic_access",
        "name",
        "resource_group",
    ]

    request_body = dict(parse_qsl(res.request.body))
    for k, v in request_body.items():
        assert k in optional_body_data

        if k == "address_prefix_management":
            assert v in ["auto", "manual"]

        if k == "classic_access":
            assert v in ["true", "false"]

        if k == "name":
            assert 1 <= len(v) <= 63
            assert re.match(r"^([a-z]|[a-z][-a-z0-9]*[a-z0-9])$", v)

        if k == "resource_group":
            assert re.match(r"^[0-9a-f]{32}$", v)

    check_required_params(res)


# PATCH /vpcs/{id}
def test_patch_vpc_by_id():
    vpc_id = "r006-192412ca-4ab4-4e00-a852-188047f8698d"
    body = {"name": "test2_updated"}

    res = session.patch(
        f"{API_ENDPOINT}/v1/vpcs/{vpc_id}?version=2021-04-20&generation=2", json=body
    )

    assert re.search(r"v1/vpcs/(.*?)\?[vg]", res.url)
    check_required_params(res)

    request_body = json.loads(res.request.body)
    name = res.json().get("name", "")

    assert "name" in request_body.keys()
    assert re.match(r"^([a-z]|[a-z][-a-z0-9]*[a-z0-9])$", name)
    assert 1 <= len(name) <= 63


# DELETE /vpcs/{id}
def test_delete_vpc_by_id():
    vpc_id = "r006-192412ca-4ab4-4e00-a852-188047f8698d"

    res = session.delete(
        f"{API_ENDPOINT}/v1/vpcs/{vpc_id}?version=2021-04-20&generation=2"
    )

    check_required_params(res)

    assert re.search(r"v1/vpcs/(.*?)\?[vg]", res.url)
    assert res.status_code == 204
