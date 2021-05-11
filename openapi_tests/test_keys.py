import re
from urllib.parse import parse_qsl, urlparse

from openapi_tests import _adapter
from openapi_tests._helpers import (
    REQUIRED_PARAMS,
    SUBNET_NAME_REGEX,
    check_valid_key,
    check_required_params,
)

from openapi_tests._adapter import API_ENDPOINT, session


# TESTS STARTS HERE
# GET /keys
def test_get_keys():
    res = session.get(f"{API_ENDPOINT}/v1/keys?version=2021-05-06&generation=2")
    query_params = dict(parse_qsl(urlparse(res.url).query))

    optional_params = ["resource_group.id"]
    response = res.json()["keys"]

    # -- testing request params
    check_required_params(res)

    for k, v in query_params.items():
        # check that query has the correct params
        assert k in (REQUIRED_PARAMS + optional_params)
        # check if query params has any value
        assert v

    # -- testing response

    for data in response:
        check_valid_key(data)


# GET /keys/id
def test_key_by_id():
    key_id = _adapter.key_id

    res = session.get(
        f"{API_ENDPOINT}/v1/keys/{key_id}?version=2021-05-06&generation=2"
    )

    check_required_params(res)

    # testing response
    check_valid_key(res.json())


# POST /keys
def test_post_keys():
    body = {
        "name": "my-key-1",
        "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwM/8slSaAsMkP91qWDKD20+ZNq6dLu+qoE/oglPwJJBxpDU/T0wJ2LmfHSsRUNxX9ZA/CMkHsFJ0Gbuqvz0lx4TPN4AGNIr5bWj4VZp2LXibQ3QJkhkK3qdhUIyTY34qtEea8UYviZUAmROe2MMTpYayxsbnTDMw/RJjQ/d3W9hPSGQl7XLmI8Qvpxg5OBuopVllzUOF00hYyLaqtmpr+DaXHt0AVHu3HfH07TDGrVlqbrKo+BPLxv7bOvVJ5z5Ab/H1KcrgiVipcCunqCK+wnLTSeeIQF7x/lclo/SvWalSj+zQ+GfipZpI5R5ZHpFkPAq8OLly6ErKsqnwN8H2r",
        "type": "rsa",
    }

    res = session.post(
        f"{API_ENDPOINT}/v1/keys?version=2021-05-06&generation=2", json=body
    )

    allowed_body_data = ["public_key", "name", "resource_group", "type"]

    for k, v in body.items():
        assert k in allowed_body_data

    check_required_params(res)
    check_valid_key(res.json())


# PATCH /keys/{id}
def test_patch_key_by_id():
    key_id = _adapter.key_id
    body = {"name": "my-key-1-modified"}

    res = session.patch(
        f"{API_ENDPOINT}/v1/keys/{key_id}?version=2021-05-06&generation=2", json=body
    )

    assert re.search(r"v1/keys/(.*?)\?[vg]", res.url)
    check_required_params(res)
    data = res.json()
    name = data.get("name", "")

    assert "name" in body.keys()
    assert re.match(SUBNET_NAME_REGEX, name)
    assert 1 <= len(name) <= 63
    check_valid_key(data)

    assert data.get("name") == body.get("name")


# DELETE /keys/{id}
def test_delete_key_by_id():
    key_id = _adapter.key_id

    res = session.delete(
        f"{API_ENDPOINT}/v1/keys/{key_id}?version=2021-05-06&generation=2"
    )

    check_required_params(res)

    assert re.search(r"v1/keys/(.*?)\?[vg]", res.url)
    assert res.status_code == 204
