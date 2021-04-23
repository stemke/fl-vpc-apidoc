# from openapi_tests import parameters as pm
import json
import os
import re
from urllib.parse import parse_qsl, urlparse, urlsplit

import requests

path = os.path.join(__file__, "../iam_token.txt")

if os.path.exists(path):
    with open(path) as f:
        token = f.read().strip()
else:
    token = ""


iam_token = os.getenv("IAM_TOKEN", token)


HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    "Authorization": iam_token,
    "token_type": "Bearer",
}

session = requests.Session()
session.headers = HEADERS

VPC_API_ENDPOINT = "https://us-south.iaas.cloud.ibm.com"

REQUIRED_PARAMS = ["version", "generation"]

def check_required_params(request, required_params=REQUIRED_PARAMS):
    query_params = dict(parse_qsl(urlparse(request.url).query))

    # check that the request params contains the required params in the api spec
    for k in required_params:
        assert k in query_params.keys()

    # test if version matches the date YYYY-MM-DD
    regex = r"(^[0-9]{4}-[0-9]{2}-[0-9]{2})"
    assert re.search(regex, query_params.get("version"))
    # check if generation is a number
    assert query_params.get("generation") == "2"


# GET /vpcs
def test_get_vpcs():
    res = session.get(f"{VPC_API_ENDPOINT}/v1/vpcs?version=2021-04-20&generation=2")
    query_params = dict(parse_qsl(urlparse(res.url).query))

    optional_params = ["start", "limit", "resource_group", "classic_access"]

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


# POST /vpcs
def test_post_vpcs():
    body = {"name": "test"}

    res = session.post(
        f"{VPC_API_ENDPOINT}/v1/vpcs?version=2021-04-20&generation=2", data=body
    )

    required_params = ["version", "generation"]

    optional_body_params = [
        "VPCPrototype",
        "address_prefix_management",
        "classic_access",
        "name",
        "resource_group",
    ]

    request_body = dict(parse_qsl(res.request.body))
    for k, v in request_body.items():
        assert k in optional_body_params

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
    vpc_id = "123"
    res = session.post(
        f"{VPC_API_ENDPOINT}/v1/vpcs/{vpc_id}?version=2021-01-26&generation=1"
    )

    assert re.search(r"v1/vpcs/(.*?)\?[vg]", res.url)
    check_required_params(res)
