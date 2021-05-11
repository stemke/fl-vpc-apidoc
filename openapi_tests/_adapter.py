import requests_mock
from . import _mock_responses
import requests
import os


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


iam_token = ""  # get_iam_token()

API_ENDPOINT = "https://us-south.iaas.cloud.ibm.com"

HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    "Authorization": iam_token,
    "token_type": "Bearer",
}


vpc_id = _mock_responses.GET_VPC_BY_ID_RESPONSE.get("id")
subnet_id = _mock_responses.GET_SUBNET_BY_ID_RESPONSE.get("id")
key_id = _mock_responses.GET_KEY_BY_ID_RESPONSE.get("id")
instance_id = _mock_responses.GET_INSTANCE_BY_ID_RESPONSE.get("id")
floating_ips_id = _mock_responses.GET_FLOATING_IP_BY_ID_RESPONSE.get("id")


session = requests.Session()
adapter = requests_mock.Adapter()
session.mount(API_ENDPOINT, adapter)
session.headers = HEADERS


# VPCS
adapter.register_uri(
    "GET", f"{API_ENDPOINT}/v1/vpcs", json=_mock_responses.GET_VPCS_RESPONSE
)
adapter.register_uri(
    "POST", f"{API_ENDPOINT}/v1/vpcs", json=_mock_responses.POST_VPCS_RESPONSE
)
adapter.register_uri(
    "DELETE",
    f"{API_ENDPOINT}/v1/vpcs/{vpc_id}",
    status_code=_mock_responses.DELETE_RESPONSE,
)
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/vpcs/{vpc_id}",
    json=_mock_responses.GET_VPC_BY_ID_RESPONSE,
)
adapter.register_uri(
    "PATCH",
    f"{API_ENDPOINT}/v1/vpcs/{vpc_id}",
    json=_mock_responses.PATCH_VPC_BY_ID_RESPONSE,
)


# SUBNETS
adapter.register_uri(
    "GET", f"{API_ENDPOINT}/v1/subnets", json=_mock_responses.GET_SUBNETS_RESPONSE
)
adapter.register_uri(
    "POST", f"{API_ENDPOINT}/v1/subnets", json=_mock_responses.POST_SUBNETS_RESPONSE
)
adapter.register_uri(
    "DELETE",
    f"{API_ENDPOINT}/v1/subnets/{subnet_id}",
    status_code=_mock_responses.DELETE_RESPONSE,
)
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/subnets/{subnet_id}",
    json=_mock_responses.GET_SUBNET_BY_ID_RESPONSE,
)
adapter.register_uri(
    "PATCH",
    f"{API_ENDPOINT}/v1/subnets/{subnet_id}",
    json=_mock_responses.PATCH_SUBNET_BY_ID_RESPONSE,
)


# KEYS
adapter.register_uri(
    "GET", f"{API_ENDPOINT}/v1/keys", json=_mock_responses.GET_KEYS_RESPONSE
)
adapter.register_uri(
    "POST", f"{API_ENDPOINT}/v1/keys", json=_mock_responses.POST_KEYS_RESPONSE
)
adapter.register_uri(
    "DELETE",
    f"{API_ENDPOINT}/v1/keys/{key_id}",
    status_code=_mock_responses.DELETE_RESPONSE,
)
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/keys/{key_id}",
    json=_mock_responses.GET_KEY_BY_ID_RESPONSE,
)
adapter.register_uri(
    "PATCH",
    f"{API_ENDPOINT}/v1/keys/{key_id}",
    json=_mock_responses.PATCH_KEY_BY_ID_RESPONSE,
)


# INSTANCES
adapter.register_uri(
    "GET", f"{API_ENDPOINT}/v1/instances", json=_mock_responses.GET_INSTANCES_RESPONSE
)
adapter.register_uri(
    "POST",
    f"{API_ENDPOINT}/v1/instances",
    json=_mock_responses.POST_INSTANCES_RESPONSE,
)
adapter.register_uri(
    "DELETE",
    f"{API_ENDPOINT}/v1/instances/{instance_id}",
    status_code=_mock_responses.DELETE_RESPONSE,
)
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/instances/{instance_id}",
    json=_mock_responses.GET_INSTANCE_BY_ID_RESPONSE,
)
adapter.register_uri(
    "PATCH",
    f"{API_ENDPOINT}/v1/instances/{instance_id}",
    json=_mock_responses.PATCH_INSTANCE_BY_ID_RESPONSE,
)


# FLOATING IPS
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/floating_ips",
    json=_mock_responses.GET_FLOATING_IPS_RESPONSE,
)
adapter.register_uri(
    "POST",
    f"{API_ENDPOINT}/v1/floating_ips",
    json=_mock_responses.POST_FLOATING_IPS_RESPONSE,
)
adapter.register_uri(
    "DELETE",
    f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}",
    status_code=_mock_responses.DELETE_RESPONSE,
)
adapter.register_uri(
    "GET",
    f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}",
    json=_mock_responses.GET_FLOATING_IP_BY_ID_RESPONSE,
)
adapter.register_uri(
    "PATCH",
    f"{API_ENDPOINT}/v1/floating_ips/{floating_ips_id}",
    json=_mock_responses.PATCH_FLOATING_IP_BY_ID_RESPONSE,
)
