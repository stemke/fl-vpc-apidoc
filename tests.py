import requests


def test_login():
    assert 1==1
    # tests t ogo here once all docs has been received


# from ibm_vpc import VpcV1
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from ibm_cloud_sdk_core import ApiException

# authenticator = IAMAuthenticator("RwGld3KPE3UsXoDlFypWSdLLP_6Vt8zaOREOtDY46x3h")
# service = VpcV1('2020-06-02', authenticator=authenticator)

# #  Listing VPCs
# print("List VPCs")
# try:
#     vpcs = service.list_vpcs().get_result()['vpcs']
# except ApiException as e:
#   print("List VPC failed with status code " + str(e.code) + ": " + e.message)
# for vpc in vpcs:
#     print(vpc['id'], "\t",  vpc['name'])


API_KEY = "RwGld3KPE3UsXoDlFypWSdLLP_6Vt8zaOREOtDY46x3h"
data = {
    "apikey": API_KEY,
    "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
}

HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

session = requests.Session()
session.headers = HEADERS

ACCESS_TOKEN_URL = "https://iam.cloud.ibm.com/identity/token"
res = session.post(ACCESS_TOKEN_URL, data=data).json()
access_token = res.get("access_token")
print(access_token)

session.headers.update({"Authorization": API_KEY})
VPC_API_ENDPOINT = "https://eu-gb.iaas.cloud.ibm.com"
r = session.get(f"{VPC_API_ENDPOINT}/v1/instances?version=2021-01-26&generation=1&apikey={access_token}", )
print(r.text)