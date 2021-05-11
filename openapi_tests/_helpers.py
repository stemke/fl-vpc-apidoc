import re
from urllib.parse import parse_qsl, urlparse
from dateutil.parser import parse


REQUIRED_PARAMS = ["version", "generation"]

URL_REGEX = r"^http(s)?:\/\/([^\/?#]*)([^?#]*)(\?([^#]*))?(#(.*))?$"

ID_REGEX = r"^[-0-9a-z_]+$"

NAME_REGEX = r"^-?([a-z]|[a-z][-a-z0-9]*[a-z0-9]|[0-9][-a-z0-9]*([a-z]|[-a-z][-a-z0-9]*[a-z0-9]))$"

IPV4_REGEX = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$"

SUBNET_NAME_REGEX = r"^([a-z]|[a-z][-a-z0-9]*[a-z0-9])$"

RESOURCE_GROUP_ID_REGEX = r"^[0-9a-f]{32}$"

IP_ADDRESS_REGEX = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"


RESPONSE_KEYS = [
    "href",
    "id",
    "name"
]

ID_KEYS = [
    "id",
    "href",
    "crn"
]

NETWORK_ACL_KEYS = RESPONSE_KEYS + [
    "crn",
    "deleted",
]

ROUTING_TABLE_KEYS = RESPONSE_KEYS + [
    "resource_type",
    "deleted"
]

NET_KEYS = RESPONSE_KEYS + [
    "created_at",
    "crn",
    "resource_group",
    "status",
    # doesn't exist in api spec
    "resource_type",
]

VALID_VPC_KEYS = NET_KEYS + [
    "classic_access",
    "cse_source_ips",
    "default_network_acl",
    "default_routing_table",
    "default_security_group",
]

SUBNET_KEYS = NET_KEYS + [
    "ip_version",
    "network_acl",
    "available_ipv4_address_count",
    "ipv4_cidr_block",
    "routing_table",
    "total_ipv4_address_count",
    "vpc",
    "zone",
]

INSTANCE_CODES = [
    "cannot_start",
    "cannot_start_capacity",
    "cannot_start_compute",
    "cannot_start_ip_address",
    "cannot_start_network",
    "cannot_start_storage",
    "encryption_key_deleted",
]

NET_STATUS = [
    "available",
    "deleting",
    "failed",
    "pending"
]

INSTANCE_STATUSES = [
    "deleting",
    "failed",
    "paused",
    "pausing",
    "pending",
    "restarting",
    "resuming",
    "running",
    "starting",
    "stopped",
    "stopping",
]

def check_valid_params(keys, param):
    for key, val in param.items():
        assert key in keys
        assert val

        if key == "crn":
            assert val.startswith("crn:")

        elif key == "href":
            assert re.match(URL_REGEX, val)

        elif key == "id":
            assert 1 <= len(val) <= 63
            assert re.match(ID_REGEX, val)

        elif key == "name":
            assert 1 <= len(val) <= 63
            assert re.match(NAME_REGEX, val)

        elif key == "deleted":
            assert re.match(URL_REGEX, val.get("more_info"))

        elif key == "ip_version":
            assert val in ["ipv4"]

        elif key == "created_at":
            assert is_date(val)


def check_valid_resource_group(resource_group):
    for k, v in resource_group.items():
        assert k in RESPONSE_KEYS

        if k == "href":
            assert re.match(URL_REGEX, v)

        elif k == "id":
            assert re.match(RESOURCE_GROUP_ID_REGEX, v)

        elif k == "name":
            assert re.match(r"^[a-zA-Z0-9-_ ]+$", v)
            assert 1 <= len(v) <= 40


def check_valid_routing_table(rt):
    for rk in ["id", "href", "name", "resource_type"]:
        assert rk in rt.keys()

    for k, v in rt.items():
        assert k in ROUTING_TABLE_KEYS

        if k == "href":
            assert re.match(URL_REGEX, v)

        elif k == "id":
            assert re.match(ID_REGEX, v)

        elif k == "name":
            assert 1 <= len(v) <= 63
            assert re.match(NAME_REGEX, v)

        elif k == "deleted":
            assert re.match(URL_REGEX, v.get("more_info"))


def check_valid_vpc(vpc):
    for key in vpc.keys():
        assert key in VALID_VPC_KEYS

    assert isinstance(vpc.get("classic_access"), bool)
    assert is_date(vpc.get("created_at"))
    assert vpc.get("crn").startswith("crn:")

    check_valid_params(NETWORK_ACL_KEYS, vpc.get("default_network_acl"))
    check_valid_params(NETWORK_ACL_KEYS, vpc.get("default_security_group"))

    for rt_key, rt_val in vpc.get("default_routing_table").items():
        assert rt_key in ROUTING_TABLE_KEYS
        assert rt_val

        if rt_key == "href":
            assert re.match(URL_REGEX, rt_val)

        elif rt_key == "id":
            assert re.match(ID_REGEX, rt_val)

        elif rt_key == "name":
            assert 1 <= len(rt_val) <= 63
            assert re.match(NAME_REGEX, rt_val)

        elif rt_key == "resource_type":
            assert rt_val in ["routing_table"]

        elif rt_key == "deleted":
            assert re.match(URL_REGEX, rt_val.get("more_info"))


def check_valid_subnet(subnet):
    for key in subnet.keys():
        assert key in SUBNET_KEYS

    assert subnet.get("available_ipv4_address_count") > -1
    assert is_date(subnet.get("created_at"))
    assert subnet.get("crn").startswith("crn:")
    assert re.match(URL_REGEX, subnet.get("href"))

    assert re.match(ID_REGEX, subnet.get("id"))
    assert 1 <= len(subnet.get("id", "")) <= 64

    assert subnet.get("ip_version") in ["ipv4"]
    assert re.match(IPV4_REGEX, subnet.get("ipv4_cidr_block"))

    assert 1 <= len(subnet.get("name")) <= 63
    assert re.match(NAME_REGEX, subnet.get("name"))

    check_valid_params(NETWORK_ACL_KEYS, subnet.get("network_acl"))
    check_valid_resource_group(subnet.get("resource_group"))
    check_valid_routing_table(subnet.get("routing_table"))

    assert subnet.get("status") in NET_STATUS
    assert subnet.get("total_ipv4_address_count") > 0
    check_valid_params(RESPONSE_KEYS + ["crn", "resource_type"], subnet.get("vpc"))

    deleted = subnet.get("deleted")
    if deleted:
        assert re.match(URL_REGEX, deleted.get("more_info"))

    check_valid_params(["href", "name"], subnet.get("zone"))

    public_gateway = subnet.get("public_gateway")
    if public_gateway:
        check_valid_params(NETWORK_ACL_KEYS, public_gateway)
        assert public_gateway in ["public_gateway"]


def check_valid_key(key):
    optional_params = ["resource_group.id"]
    required_response_keys = [
        "id",
        "crn",
        "href",
        "fingerprint",
        "name",
        "public_key",
        "type",
        "length",
        "created_at",
        "resource_group",
    ]

    check_valid_params(required_response_keys, key)

    for k, v in key.items():
        assert k in required_response_keys + optional_params

        if k == "fingerprint":
            assert v.startswith("SHA256")

        elif k == "length":
            assert v in [2048, 4096]

        elif k == "public_key":
            assert v

        elif k == "resource_group":
            check_valid_resource_group(v)

        elif k == "type":
            assert v in ["rsa"]


def check_valid_instance(ins):
    assert isinstance(ins.get("bandwidth"), int)

    volume_params = ["deleted", "device", "href", "id", "name", "volume"]
    bva = ins.get("boot_volume_attachment")
    check_valid_params(volume_params, bva)
    check_valid_params(NETWORK_ACL_KEYS, bva.get("volume"))

    # disks not present in old response
    disks = ins.get("disks", [])
    disk_params = ["created_at", "interface_type", "resource_type", "size"]

    for disk in disks:
        check_valid_params(RESPONSE_KEYS + disk_params, disks)

        for k, v in disk.items():
            if k == "interface_type":
                assert v in ["virtio_blk", "nvme"]

            elif k == "resource_type":
                assert v in ["instance_disk"]

            elif k == "size":
                assert 1 <= v <= 100_000

    assert 1 <= ins.get("memory") <= 512

    netw_ints = ins.get("network_interfaces")
    assert len(netw_ints) >= 1

    for net in netw_ints:
        check_valid_params(ROUTING_TABLE_KEYS + ["primary_ipv4_address", "subnet"], net)

        for k, v in net.items():
            if k == "resource_type":
                assert v in ["network_interface"]

            elif k == "primary_ipv4_address":
                assert re.match(IP_ADDRESS_REGEX, v)

            elif k == "subnet":
                check_valid_params(NETWORK_ACL_KEYS, v)

    check_valid_params(["href", "name"], ins.get("profile"))
    check_valid_resource_group(ins.get("resource_group"))

    assert ins.get("status") in INSTANCE_STATUSES

    # status_reasons not present in old response
    status_reasons = ins.get("status_reasons", [])
    for status_reason in status_reasons:
        for k, v in status_reason.items():
            if k == 'code':
                assert v in [INSTANCE_CODES]
                assert re.match(r'^[a-z]+(_[a-z]+)*$', v)

            elif k == 'message':
                assert v

            elif k == 'more_info':
                assert re.match(URL_REGEX, v)

    # vpcu not present in old response
    vpcu = ins.get('vcpu')
    assert vpcu.get('architecture')
    assert vpcu.get('count') >= 1

    volume_attachments = ins.get('volume_attachments')
    for attachment in volume_attachments:
        check_valid_params(RESPONSE_KEYS + ['deleted', 'volume', 'device'], attachment)
        check_valid_params(NETWORK_ACL_KEYS, attachment.get("volume"))

    check_valid_params(NETWORK_ACL_KEYS, ins.get('vpc'))
    check_valid_params(['href', 'name'], ins.get('zone'))

    gpu = ins.get('gpu')
    if gpu:
        assert gpu.get('count') >= 1
        assert gpu.get('manufacturer')
        assert gpu.get('memory') >= 1
        assert gpu.get('model')

    image = ins.get('image')
    if image:
        check_valid_params(NETWORK_ACL_KEYS, image)


def check_valid_floating_ip(ip):
    check_valid_params(NET_KEYS + ['address', 'zone', 'target'], ip)

    for k, v in ip.items():
        if k == 'address':
            assert re.match(IP_ADDRESS_REGEX, v)

        elif k == 'resource_group':
            check_valid_resource_group(v)

        elif k == 'status':
            assert v in NET_STATUS

        elif k == 'zone':
            check_valid_params(["href", "name"], v)

        elif k == 'target':
            check_valid_params(ROUTING_TABLE_KEYS + ['primary_ipv4_address'], v)
            assert v.get("resource_type") in ['network_interface']
            assert re.match(IP_ADDRESS_REGEX, v.get('primary_ipv4_address'))


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except (ValueError, TypeError):
        return False


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