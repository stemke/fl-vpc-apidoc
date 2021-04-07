import requests
import json


with open("iam_token.txt") as f:
    iam_token = f.read().strip()

HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    "Authorization": f"Bearer {iam_token}",
    "token_type": "Bearer",
}

session = requests.Session()
session.headers = HEADERS

VPC_API_ENDPOINT = "https://us-south.iaas.cloud.ibm.com"

# GET /vpcs
def get_vpcs():
    r = session.get(f"{VPC_API_ENDPOINT}/v1/vpcs?version=2021-01-01&generation=2")
    print(r.json())

# GET /vps/<id>
def get_vpcs_detail():
    _id = "r006-1e1ef30a-6c4c-4ce8-b805-08cba781eb7a"
    r = session.get(f"{VPC_API_ENDPOINT}/v1/vpcs/{_id}?version=2021-01-01&generation=2")
    print(r.json())    


# POST /vpcs
def post_vpcs():
    payload = json.dumps({"name": "vpc-1"})
    r = session.post(f"{VPC_API_ENDPOINT}/v1/vpcs?version=2021-01-01&generation=2", data=payload)
    print(r.json())


# get_vpcs()
# post_vpcs()
# get_vpcs_detail()