from openapi_core import create_spec
import json
from openapi_core.validation.request.validators import RequestValidator
import requests


with open("./apikey.json") as f:
    spec_dict = json.load(f)



with open("iam_token.txt") as f:
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
r = session.get(f"{VPC_API_ENDPOINT}/v1/vpcs?version=2021-01-01&generation=2")
print(r.json())