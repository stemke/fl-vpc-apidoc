import json
from openapi_tests.helpers import API_ENDPOINT, check_required_params, REQUIRED_PARAMS, session
from urllib.parse import parse_qsl, urlparse
import re


# TESTS STARTS HERE
# GET /subnets
def test_get_subnets():
    res = session.get(f"{API_ENDPOINT}/v1/subnets?version=2021-04-20&generation=2")
    query_params = dict(parse_qsl(urlparse(res.url).query))

    optional_params = [
		"start",
		"limit",
		"resource_group.id",
		"routing_table.id",
		"routing_table.name",
        "ipv4_cidr_block"
	]

    check_required_params(res)

    for k, v in query_params.items():
        # check if query contains optional params
        if k in optional_params:
            # check if query params has any value
            assert v

        if k == "limit":
            assert v.isdigit()
            assert int(v) in range(1, 101)


# POST /subnets
def test_post_subnets():
    body = {
        "name": "my-subnet-1",
        "ipv4_cidr_block": "10.0.1.0/24",
        "ip_version": "ipv4",
        "zone": { "name": "us-south-1" },
        "vpc": { "id": "a0819609-0997-4f92-9409-86c95ddf59d3" }
    }

    res = session.post(
        f"{API_ENDPOINT}/v1/subnets?version=2021-04-20&generation=2", json=body
    )

    check_required_params(res)

    optional_body_data = [
        "ip_version",
        "name",
        "network_acl",
        "public_gateway",
        "resource_group",
        "routing_table",

        # to double check
        "ipv4_cidr_block",
        "zone",
        "vpc"
    ]

    required_body_data = ["vpc"]
    request_body = json.loads(res.request.body)

    for param in required_body_data:
        assert param in request_body.keys()

    for vpc_param in request_body["vpc"]:
        assert "id" in vpc_param

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


# PATCH /subnets/{id}
def test_patch_subnet_by_id():

    subnet_id = "0717-e7127621-d990-42a8-bb4b-7365402aab33"
    body = {"name": "test"}

    res = session.patch(
        f"{API_ENDPOINT}/v1/subnets/{subnet_id}?version=2021-04-20&generation=2", data=body
    )

    assert re.search(r"v1/subnets/(.*?)\?[vg]", res.url)
    check_required_params(res)

    request_body = dict(parse_qsl(res.request.body))
    name = request_body.get("name", '')
    assert "name" in request_body.keys()
    assert re.match(r'^([a-z]|[a-z][-a-z0-9]*[a-z0-9])$', name)
    assert 1 <= len(name) <= 63


# DELETE /subnets/{id}
def test_delete_subnet_by_id():
    subnet_id = "0717-e7127621-d990-42a8-bb4b-7365402aab33"

    res = session.delete(
        f"{API_ENDPOINT}/v1/subnets/{subnet_id}?version=2021-04-20&generation=2")

    assert re.search(r"v1/subnets/(.*?)\?[vg]", res.url)
    check_required_params(res)
