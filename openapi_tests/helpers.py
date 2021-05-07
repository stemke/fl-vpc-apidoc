import os
import re
from urllib.parse import parse_qsl, urlparse
from dateutil.parser import parse

import requests
import requests_mock
from . import mock_responses

REQUIRED_PARAMS = ["version", "generation"]
API_ENDPOINT = "https://us-south.iaas.cloud.ibm.com"

URL_REGEX = r'^http(s)?:\/\/([^\/?#]*)([^?#]*)(\?([^#]*))?(#(.*))?$'
ID_REGEX = r'^[-0-9a-z_]+$'
NAME_REGEX = r'^-?([a-z]|[a-z][-a-z0-9]*[a-z0-9]|[0-9][-a-z0-9]*([a-z]|[-a-z][-a-z0-9]*[a-z0-9]))$'

NETWORK_ACL_KEYS = [
    "crn",
    "href",
    "id",
    "name",
    "deleted"
]

ROUTING_TABLE_KEYS = [
    "href",
    "id",
    "name",
    "resource_type",
    "deleted"
]

VALID_VPC_KEYS = [
    "classic_access",
    "created_at",
    "crn",
    "default_network_acl",
    "default_routing_table",
    "default_security_group",
    "href",
    "id",
    "name",
    "resource_group",
    "status",
    "cse_source_ips",

    # doesn't exist in api spec
    'resource_type'
]

def check_valid_keys(keys, param):
    for key, val in param.items():
        assert key in keys
        assert val

        if key == 'crn':
            assert val.startswith('crn:')
        if key == 'href':
            assert re.match(URL_REGEX, val)
        if key == 'id':
            assert re.match(ID_REGEX, val)
        if key == 'name':
            assert 1 <= len(val) <= 63
            assert re.match(NAME_REGEX, val)
        if key == 'deleted':
            assert re.match(URL_REGEX, val.get('more_info'))

def check_valid_vpc(vpc):
    for key in vpc.keys():
        assert key in VALID_VPC_KEYS

    assert isinstance(vpc.get("classic_access"), bool)
    assert is_date(vpc.get("created_at"))
    assert vpc.get("crn").startswith("crn:")

    check_valid_keys(NETWORK_ACL_KEYS, vpc.get("default_network_acl"))
    check_valid_keys(NETWORK_ACL_KEYS, vpc.get("default_security_group"))

    for rt_key, rt_val in vpc.get("default_routing_table").items():
        assert rt_key in ROUTING_TABLE_KEYS
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

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except (ValueError, TypeError):
        return False


def get_iam_token(api_token="api_token_here"):
    DEFAULT_IAM_URL = "https://iam.cloud.ibm.com"
    CONTENT_TYPE = "application/x-www-form-urlencoded"
    OPERATION_PATH = "/identity/token"
    REQUEST_TOKEN_GRANT_TYPE = "urn:ibm:params:oauth:grant-type:apikey"
    REQUEST_TOKEN_RESPONSE_TYPE = "cloud_iam"
    TOKEN_NAME = "access_token"

    apikey = os.getenv("API_KEY", api_token)

    headers = {"Content-type": CONTENT_TYPE, "Accept": "application/json"}

    data = {
        "grant_type": REQUEST_TOKEN_GRANT_TYPE,
        "apikey": apikey,
        "response_type": REQUEST_TOKEN_RESPONSE_TYPE,
    }

    req = requests.post(
        f"{DEFAULT_IAM_URL}{OPERATION_PATH}", headers=headers, data=data
    ).json()
    return req.get(TOKEN_NAME)


# helper methods
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


iam_token = ""  # get_iam_token()

HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    "Authorization": iam_token,
    "token_type": "Bearer",
}


vpc_id = mock_responses.GET_VPC_BY_ID_RESPONSE.get("id")
subnet_id = mock_responses.GET_SUBNET_BY_ID_RESPONSE.get("id")
key_id = mock_responses.GET_KEY_BY_ID_RESPONSE.get("id")
instance_id = mock_responses.GET_INSTANCE_BY_ID_RESPONSE.get("id")
floating_ips_id = mock_responses.GET_FLOATING_IP_BY_ID_RESPONSE.get("id")


session = requests.Session()
adapter = requests_mock.Adapter()
session.mount(API_ENDPOINT, adapter)
session.headers = HEADERS


# VPCS
adapter.register_uri(
    "GET", f"{API_ENDPOINT}/v1/vpcs", json=mock_responses.GET_VPCS_RESPONSE
)
adapter.register_uri(
    "POST", f"{API_ENDPOINT}/v1/vpcs", json=mock_responses.POST_VPCS_RESPONSE
)
adapter.register_uri(
    "DELETE",
    f"{API_ENDPOINT}/v1/vpcs/{vpc_id}",
    status_code=mock_responses.DELETE_RESPONSE,
)
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/vpcs/{vpc_id}",
    json=mock_responses.GET_VPC_BY_ID_RESPONSE,
)
adapter.register_uri(
    "PATCH",
    f"{API_ENDPOINT}/v1/vpcs/{vpc_id}",
    json=mock_responses.PATCH_VPC_BY_ID_RESPONSE,
)


# SUBNETS
adapter.register_uri(
    "GET", f"{API_ENDPOINT}/v1/subnets", json=mock_responses.GET_SUBNETS_RESPONSE
)
adapter.register_uri(
    "POST", f"{API_ENDPOINT}/v1/subnets", json=mock_responses.POST_SUBNETS_RESPONSE
)
adapter.register_uri(
    "DELETE",
    f"{API_ENDPOINT}/v1/subnets/{subnet_id}",
    status_code=mock_responses.DELETE_RESPONSE,
)
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/subnets/{subnet_id}",
    json=mock_responses.GET_SUBNET_BY_ID_RESPONSE,
)
adapter.register_uri(
    "PATCH",
    f"{API_ENDPOINT}/v1/subnets/{subnet_id}",
    json=mock_responses.PATCH_SUBNET_BY_ID_RESPONSE,
)


# KEYS
adapter.register_uri(
    "GET", f"{API_ENDPOINT}/v1/keys", json=mock_responses.GET_KEYS_RESPONSE
)
adapter.register_uri(
    "POST", f"{API_ENDPOINT}/v1/keys", json=mock_responses.POST_KEYS_RESPONSE
)
adapter.register_uri(
    "DELETE",
    f"{API_ENDPOINT}/v1/keys/{key_id}",
    status_code=mock_responses.DELETE_RESPONSE,
)
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/keys/{key_id}",
    json=mock_responses.GET_KEY_BY_ID_RESPONSE,
)
adapter.register_uri(
    "PATCH",
    f"{API_ENDPOINT}/v1/keys/{key_id}",
    json=mock_responses.PATCH_KEY_BY_ID_RESPONSE,
)


# INSTANCES
adapter.register_uri(
    "GET", f"{API_ENDPOINT}/v1/floating_ips", json=mock_responses.GET_INSTANCES_RESPONSE
)
adapter.register_uri(
    "POST",
    f"{API_ENDPOINT}/v1/floating_ips",
    json=mock_responses.POST_INSTANCES_RESPONSE,
)
adapter.register_uri(
    "DELETE",
    f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}",
    status_code=mock_responses.DELETE_RESPONSE,
)
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}",
    json=mock_responses.GET_INSTANCE_BY_ID_RESPONSE,
)
adapter.register_uri(
    "PATCH",
    f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}",
    json=mock_responses.PATCH_INSTANCE_BY_ID_RESPONSE,
)


# FLOATING IPS
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/floating_ips",
    json=mock_responses.GET_FLOATING_IPS_RESPONSE,
)
adapter.register_uri(
    "POST",
    f"{API_ENDPOINT}/v1/floating_ips",
    json=mock_responses.POST_FLOATING_IPS_RESPONSE,
)
adapter.register_uri(
    "DELETE",
    f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}",
    status_code=mock_responses.DELETE_RESPONSE,
)
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}",
    json=mock_responses.GET_FLOATING_IP_BY_ID_RESPONSE,
)
adapter.register_uri(
    "PATCH",
    f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}",
    json=mock_responses.PATCH_FLOATING_IP_BY_ID_RESPONSE,
)
