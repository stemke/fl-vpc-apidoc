from openapi_tests import parameters as pm
import requests
from urllib.parse import parse_qs, urlsplit, urlparse

with open("./iam_token.txt") as f:
    iam_token = f.read().strip()


HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    "Authorization": iam_token,
    "token_type": "Bearer",
}

session = requests.Session()
session.headers = HEADERS

VPC_API_ENDPOINT = "https://us-south.iaas.cloud.ibm.com"

# GET /vpcs

def test_vpc():
    r = session.get(f"{VPC_API_ENDPOINT}/v1/vpcs?version=2021-01-01&generation=2")
    query_params = parse_qs(urlparse(r.url).query)

    required_params = ["version", "generation"]
    optional_params = []
    
    for param in required_params:
        assert param in query_params.keys()


    