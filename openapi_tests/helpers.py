import os
import re
from urllib.parse import parse_qsl, urlparse

import requests

path = os.path.join(__file__, "../iam_token.txt")

if os.path.exists(path):
    with open(path) as f:
        token = f.read().strip()
else:
    token = ""


IAM_TOKEN = os.getenv("IAM_TOKEN", token)


HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    "Authorization": IAM_TOKEN,
    "token_type": "Bearer",
}

session = requests.Session()
session.headers = HEADERS

API_ENDPOINT = "https://us-south.iaas.cloud.ibm.com"
REQUIRED_PARAMS = ["version", "generation"]

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