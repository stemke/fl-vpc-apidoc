from openapi_tests.helpers import API_ENDPOINT, check_required_params, REQUIRED_PARAMS, session
from urllib.parse import parse_qsl, urlparse
import re


# TESTS STARTS HERE
# GET /subnets
def test_get_subnets():
    res = session.get(f"{API_ENDPOINT}/v1/subnets?version=2021-04-20&generation=2")
    query_params = dict(parse_qsl(urlparse(res.url).query))

    optional_params = ["start", "limit", "resource_group", "classic_access"]

    check_required_params(res)
