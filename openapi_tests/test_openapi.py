# from openapi_tests import parameters as pm
import requests
from urllib.parse import parse_qsl, urlsplit, urlparse
import re

iam_token = ""

# with open("./iam_token.txt") as f:
#     iam_token = f.read().strip()


HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    "Authorization": iam_token,
    "token_type": "Bearer",
}

session = requests.Session()
session.headers = HEADERS

VPC_API_ENDPOINT = "https://us-south.iaas.cloud.ibm.com"


def check_required_params(request, required_params):
    query_params = dict(parse_qsl(urlparse(request.url).query))

    # check that the request params contains the required params in the api spec
    for k in required_params:
        assert k in query_params.keys()

# GET /vpcs
def test_get_vpcs():
    req = session.get(f"{VPC_API_ENDPOINT}/v1/vpcs?version=2021-01-01&generation=2&classic_access=true")
    query_params = dict(parse_qsl(urlparse(req.url).query))

    required_params = [
        "version",
        "generation"
    ]

    optional_params = [
        "start",
        "limit",
        "resource_group",
        "classic_access"
    ]

    check_required_params(req, required_params)

    for k, v in query_params.items():
        # check that query has the correct params
        assert k in (required_params + optional_params)
        # check if query params has any value
        assert v

        if k == "limit":
            assert k.isdigit()

        if k == "classic_access":
            assert v in ["true", "false"]


    # test if version matches the date YYYY-MM-DD
    regex = r'(\d{4}-\d{2}-\d{2})'
    assert re.search(regex, query_params.get("version"))
    # check if generation is a number
    assert query_params.get("generation").isdigit()


# POST /vpcs
def test_post_vpcs():
    req = session.post(f"{VPC_API_ENDPOINT}/v1/vpcs?version=2021-01-01&generation=2&classic_access=true")

    required_params = [
        "version",
        "generation"
    ]

    check_required_params(req, required_params)