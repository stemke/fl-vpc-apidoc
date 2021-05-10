import re
from urllib.parse import parse_qsl, urlparse

from openapi_tests import helpers
from openapi_tests.helpers import (
    API_ENDPOINT,
    REQUIRED_PARAMS,
    SUBNET_NAME_REGEX,
    URL_REGEX,
    check_valid_instance,
    check_required_params,
    session,
)


# TESTS STARTS HERE
# GET /instances
def test_get_instances():
    res = session.get(f"{API_ENDPOINT}/v1/instances?version=2021-05-06&generation=2")
    query_params = dict(parse_qsl(urlparse(res.url).query))

    optional_params = [
        "start",
        "limit",
        "resource_group.id",
        "name",
        "vpc.id",
        "vpc.crn",
        "vpc.name",
    ]

    response = res.json()
    data = res.json()
    required_response_keys = ["first", "limit", "instances", "total_count"]

    allowed_instance_keys = [
        "bandwidth",
        "boot_volume_attachment",
        "created_at",
        "crn",
        "gpu",
        "href",
        "id",
        "image",
        "memory",
        "name",
        "network_interfaces",
        "primary_network_interface",
        "profile",
        "resource_group",
        "status",
        "vcpu",
        "volume_attachments",
        "vpc",
        "zone",
    ]
    optional_response_key = ["next"]

    for k, v in data.items():
        assert k in (required_response_keys + optional_response_key)

        if k == "limit":
            assert 1 <= v <= 100

        if k == "total_count":
            assert v >= 0

        if k == "next":
            assert re.match(URL_REGEX, v.get("href"))

    instances = data.get("instances", [])

    for k, v in query_params.items():
        # check that query has the correct params
        assert k in (REQUIRED_PARAMS + optional_params)
        # check if query params has any value
        assert v

    # -- testing response
    for instance in instances:
        for k, v in instance.items():
            assert k in allowed_instance_keys

        check_valid_instance(instance)


# # GET /instances/id
# def test_key_by_id():
#     key_id = helpers.key_id

#     res = session.get(
#         f"{API_ENDPOINT}/v1/instances/{key_id}?version=2021-05-06&generation=2"
#     )

#     check_required_params(res)

#     # testing response
#     check_valid_key(res.json())


# # POST /instances
# def test_post_instances():
#     body = {
#         "name": "my-key-1",
#         "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwM/8slSaAsMkP91qWDKD20+ZNq6dLu+qoE/oglPwJJBxpDU/T0wJ2LmfHSsRUNxX9ZA/CMkHsFJ0Gbuqvz0lx4TPN4AGNIr5bWj4VZp2LXibQ3QJkhkK3qdhUIyTY34qtEea8UYviZUAmROe2MMTpYayxsbnTDMw/RJjQ/d3W9hPSGQl7XLmI8Qvpxg5OBuopVllzUOF00hYyLaqtmpr+DaXHt0AVHu3HfH07TDGrVlqbrKo+BPLxv7bOvVJ5z5Ab/H1KcrgiVipcCunqCK+wnLTSeeIQF7x/lclo/SvWalSj+zQ+GfipZpI5R5ZHpFkPAq8OLly6ErKsqnwN8H2r",
#         "type": "rsa",
#     }

#     res = session.post(
#         f"{API_ENDPOINT}/v1/instances?version=2021-05-06&generation=2", json=body
#     )

#     allowed_body_data = ["public_key", "name", "resource_group", "type"]

#     for k, v in body.items():
#         assert k in allowed_body_data

#     check_required_params(res)
#     check_valid_key(res.json())


# # PATCH /instances/{id}
# def test_patch_key_by_id():
#     key_id = helpers.key_id
#     body = {"name": "my-key-1-modified"}

#     res = session.patch(
#         f"{API_ENDPOINT}/v1/instances/{key_id}?version=2021-05-06&generation=2", json=body
#     )

#     assert re.search(r"v1/instances/(.*?)\?[vg]", res.url)
#     check_required_params(res)
#     data = res.json()
#     name = data.get("name", "")

#     assert "name" in body.instances()
#     assert re.match(SUBNET_NAME_REGEX, name)
#     assert 1 <= len(name) <= 63
#     check_valid_key(data)

#     assert data.get("name") == body.get("name")


# # DELETE /instances/{id}
# def test_delete_key_by_id():
#     key_id = helpers.key_id

#     res = session.delete(
#         f"{API_ENDPOINT}/v1/instances/{key_id}?version=2021-05-06&generation=2"
#     )

#     check_required_params(res)

#     assert re.search(r"v1/instances/(.*?)\?[vg]", res.url)
#     assert res.status_code == 204
