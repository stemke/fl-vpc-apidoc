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

    data = res.json()
    required_response_keys = ["first", "limit", "instances", "total_count"]

    old_allowed_instance_keys = [
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

    allowed_instance_keys = [
        "bandwidth",
        "boot_volume_attachment",
        "created_at",
        "crn",
        "dedicated_host",
        "disks",
        "href",
        "id",
        "image",
        "memory",
        "name",
        "network_interfaces",
        "placement_target",
        "primary_network_interface",
        "profile",
        "placement_target",
        "resource_group",
        "status",
        "status_reasons",
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


# GET /instances/id
def test_key_by_id():
    instance_id = helpers.instance_id

    res = session.get(
        f"{API_ENDPOINT}/v1/instances/{instance_id}?version=2021-05-06&generation=2"
    )

    check_required_params(res)

    # testing response
    check_valid_instance(res.json())


# POST /instances
def test_post_instances():
    body = {
        "boot_volume_attachment": {
            "volume": {
                "encryption_key": {"crn": "crn:[...]"},
                "name": "my-boot-volume",
                "profile": {"name": "general-purpose"},
            }
        },
        "image": {"id": "9aaf3bcb-dcd7-4de7-bb60-24e39ff9d366"},
        "keys": [{"id": "363f6d70-0000-0001-0000-00000013b96c"}],
        "name": "my-instance",
        "placement_target": {"id": "0787-8c2a09be-ee18-4af2-8ef4-6a6060732221"},
        "primary_network_interface": {
            "name": "my-network-interface",
            "subnet": {"id": "bea6a632-5e13-42a4-b4b8-31dc877abfe4"},
        },
        "profile": {"name": "bx2-2x8"},
        "volume_attachments": [
            {
                "volume": {
                    "capacity": 1000,
                    "encryption_key": {"crn": "crn:[...]"},
                    "name": "my-data-volume",
                    "profile": {"name": "5iops-tier"},
                }
            }
        ],
        "vpc": {"id": "f0aae929-7047-46d1-92e1-9102b07a7f6f"},
        "zone": {"name": "us-south-1"},
    }

    res = session.post(
        f"{API_ENDPOINT}/v1/instances?version=2021-05-06&generation=2", json=body
    )

    allowed_body_data = [
        "keys",
        "name",
        "network_interfaces",
        "placement_target",
        "profile",
        "resource_group",
        "user_data",
        "volume_attachments",
        "vpc",
        "image",
        "boot_volume_attachment",
        "primary_network_interface",
        'zone',
    ]

    for k, v in body.items():
        assert k in allowed_body_data

    check_required_params(res)
    check_valid_instance(res.json())


# PATCH /instances/{id}
def test_patch_key_by_id():
    instance_id = helpers.instance_id
    body = {"name": "my-instance-updated"}

    res = session.patch(
        f"{API_ENDPOINT}/v1/instances/{instance_id}?version=2021-05-06&generation=2", json=body
    )

    assert re.search(r"v1/instances/(.*?)\?[vg]", res.url)
    check_required_params(res)
    data = res.json()
    name = data.get("name", "")

    assert "name" in body.keys()
    assert re.match(SUBNET_NAME_REGEX, name)
    assert 1 <= len(name) <= 63
    check_valid_instance(data)

    assert data.get("name") == body.get("name")


# DELETE /instances/{id}
def test_delete_key_by_id():
    instance_id = helpers.instance_id

    res = session.delete(
        f"{API_ENDPOINT}/v1/instances/{instance_id}?version=2021-05-06&generation=2"
    )

    check_required_params(res)

    assert re.search(r"v1/instances/(.*?)\?[vg]", res.url)
    assert res.status_code == 204
