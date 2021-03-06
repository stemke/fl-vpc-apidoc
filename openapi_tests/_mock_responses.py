DELETE_RESPONSE = 204

# VPCS
GET_VPCS_RESPONSE = {
    "limit": 50,
    "first": {"href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs?limit=50"},
    "total_count": 7,
    "vpcs": [
        {
            "id": "r006-1309ba27-c006-4ccd-8605-c88564c89d97",
            "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::vpc:r006-1309ba27-c006-4ccd-8605-c88564c89d97",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-1309ba27-c006-4ccd-8605-c88564c89d97",
            "name": "undaunting-granola-goldfish-pogo",
            "resource_type": "vpc",
            "status": "available",
            "classic_access": False,
            "created_at": "2021-05-07T05:53:52Z",
            "default_network_acl": {
                "id": "r006-5dba5f8b-b0bf-4cf9-a3e2-277f3e99d14f",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::network-acl:r006-5dba5f8b-b0bf-4cf9-a3e2-277f3e99d14f",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/network_acls/r006-5dba5f8b-b0bf-4cf9-a3e2-277f3e99d14f",
                "name": "suspect-curler-sandstorm-unpaved",
            },
            "default_routing_table": {
                "id": "r006-5f62dd2f-6295-45f4-8b3e-4bd56684d94b",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-1309ba27-c006-4ccd-8605-c88564c89d97/routing_tables/r006-5f62dd2f-6295-45f4-8b3e-4bd56684d94b",
                "name": "ultimate-lemon-reshape-strive",
                "resource_type": "routing_table",
            },
            "default_security_group": {
                "id": "r006-f3a12704-cff1-4e4d-b06e-d63d2e018380",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::security-group:r006-f3a12704-cff1-4e4d-b06e-d63d2e018380",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/security_groups/r006-f3a12704-cff1-4e4d-b06e-d63d2e018380",
                "name": "shrink-ungreased-tingle-rebuttal",
            },
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
            "cse_source_ips": [
                {
                    "ip": {"address": "10.12.121.185"},
                    "zone": {
                        "name": "us-south-1",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                    },
                },
                {
                    "ip": {"address": "10.12.158.154"},
                    "zone": {
                        "name": "us-south-2",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-2",
                    },
                },
                {
                    "ip": {"address": "10.12.168.43"},
                    "zone": {
                        "name": "us-south-3",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-3",
                    },
                },
            ],
        },
        {
            "id": "r006-192412ca-4ab4-4e00-a852-188047f8698d",
            "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::vpc:r006-192412ca-4ab4-4e00-a852-188047f8698d",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-192412ca-4ab4-4e00-a852-188047f8698d",
            "name": "my-vpc-2-updated",
            "resource_type": "vpc",
            "status": "available",
            "classic_access": False,
            "created_at": "2021-05-05T07:49:45Z",
            "default_network_acl": {
                "id": "r006-848ce071-a794-4948-833b-82fba500dc61",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::network-acl:r006-848ce071-a794-4948-833b-82fba500dc61",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/network_acls/r006-848ce071-a794-4948-833b-82fba500dc61",
                "name": "washhouse-visa-xray-superhero",
            },
            "default_routing_table": {
                "id": "r006-49b618cf-4f46-4b66-8308-07af99c196e7",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-192412ca-4ab4-4e00-a852-188047f8698d/routing_tables/r006-49b618cf-4f46-4b66-8308-07af99c196e7",
                "name": "bakeshop-outboard-marbled-sullen",
                "resource_type": "routing_table",
            },
            "default_security_group": {
                "id": "r006-d5aa0794-b90a-43e1-8371-2c3d2f8cd3d0",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::security-group:r006-d5aa0794-b90a-43e1-8371-2c3d2f8cd3d0",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/security_groups/r006-d5aa0794-b90a-43e1-8371-2c3d2f8cd3d0",
                "name": "luckless-naming-hypnosis-hunting",
            },
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
            "cse_source_ips": [
                {
                    "ip": {"address": "10.12.124.44"},
                    "zone": {
                        "name": "us-south-1",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                    },
                },
                {
                    "ip": {"address": "10.12.159.13"},
                    "zone": {
                        "name": "us-south-2",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-2",
                    },
                },
                {
                    "ip": {"address": "10.12.164.47"},
                    "zone": {
                        "name": "us-south-3",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-3",
                    },
                },
            ],
        },
        {
            "id": "r006-2633780c-f410-4c49-9ed2-11c9399c31c1",
            "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::vpc:r006-2633780c-f410-4c49-9ed2-11c9399c31c1",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-2633780c-f410-4c49-9ed2-11c9399c31c1",
            "name": "test2",
            "resource_type": "vpc",
            "status": "available",
            "classic_access": False,
            "created_at": "2021-05-09T20:11:41Z",
            "default_network_acl": {
                "id": "r006-40384cd2-0fcb-4601-b64a-764e82737cb5",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::network-acl:r006-40384cd2-0fcb-4601-b64a-764e82737cb5",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/network_acls/r006-40384cd2-0fcb-4601-b64a-764e82737cb5",
                "name": "overeager-seizing-evacuee-utopia",
            },
            "default_routing_table": {
                "id": "r006-19956091-2bcc-4f0f-a162-6f6f01746bfd",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-2633780c-f410-4c49-9ed2-11c9399c31c1/routing_tables/r006-19956091-2bcc-4f0f-a162-6f6f01746bfd",
                "name": "ferry-gleaming-uncounted-late",
                "resource_type": "routing_table",
            },
            "default_security_group": {
                "id": "r006-1a40a4fa-25e4-4992-8e46-1dcef205c69a",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::security-group:r006-1a40a4fa-25e4-4992-8e46-1dcef205c69a",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/security_groups/r006-1a40a4fa-25e4-4992-8e46-1dcef205c69a",
                "name": "backed-educator-change-yelling",
            },
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
            "cse_source_ips": [
                {
                    "ip": {"address": "10.249.66.60"},
                    "zone": {
                        "name": "us-south-1",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                    },
                },
                {
                    "ip": {"address": "10.12.163.243"},
                    "zone": {
                        "name": "us-south-2",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-2",
                    },
                },
                {
                    "ip": {"address": "10.12.168.181"},
                    "zone": {
                        "name": "us-south-3",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-3",
                    },
                },
            ],
        },
        {
            "id": "r006-50fe8d83-efeb-4377-9020-4803c62d04d6",
            "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::vpc:r006-50fe8d83-efeb-4377-9020-4803c62d04d6",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-50fe8d83-efeb-4377-9020-4803c62d04d6",
            "name": "stardust-matchbox-broiler-nervous",
            "resource_type": "vpc",
            "status": "available",
            "classic_access": False,
            "created_at": "2021-05-07T05:55:58Z",
            "default_network_acl": {
                "id": "r006-7f8c3820-c591-4a4c-9e32-e39626efa109",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::network-acl:r006-7f8c3820-c591-4a4c-9e32-e39626efa109",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/network_acls/r006-7f8c3820-c591-4a4c-9e32-e39626efa109",
                "name": "partake-budding-sitter-deniable",
            },
            "default_routing_table": {
                "id": "r006-c9ddefb2-b636-4b81-a5ba-be568653ebfc",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-50fe8d83-efeb-4377-9020-4803c62d04d6/routing_tables/r006-c9ddefb2-b636-4b81-a5ba-be568653ebfc",
                "name": "tamale-coasting-carve-matter",
                "resource_type": "routing_table",
            },
            "default_security_group": {
                "id": "r006-3ef64e04-585e-4188-9170-38e71c389f84",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::security-group:r006-3ef64e04-585e-4188-9170-38e71c389f84",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/security_groups/r006-3ef64e04-585e-4188-9170-38e71c389f84",
                "name": "coach-gloating-mumbo-undrilled",
            },
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
            "cse_source_ips": [
                {
                    "ip": {"address": "10.12.121.191"},
                    "zone": {
                        "name": "us-south-1",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                    },
                },
                {
                    "ip": {"address": "10.12.158.162"},
                    "zone": {
                        "name": "us-south-2",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-2",
                    },
                },
                {
                    "ip": {"address": "10.12.168.45"},
                    "zone": {
                        "name": "us-south-3",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-3",
                    },
                },
            ],
        },
        {
            "id": "r006-7e371d94-51c1-4636-a01b-8b469c6bde5c",
            "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::vpc:r006-7e371d94-51c1-4636-a01b-8b469c6bde5c",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-7e371d94-51c1-4636-a01b-8b469c6bde5c",
            "name": "veteran-wish-lance-manorial",
            "resource_type": "vpc",
            "status": "available",
            "classic_access": False,
            "created_at": "2021-05-07T05:56:55Z",
            "default_network_acl": {
                "id": "r006-c7d45e9a-7589-4eaa-bce7-ab76d05f1031",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::network-acl:r006-c7d45e9a-7589-4eaa-bce7-ab76d05f1031",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/network_acls/r006-c7d45e9a-7589-4eaa-bce7-ab76d05f1031",
                "name": "automaker-duly-unpopular-mandate",
            },
            "default_routing_table": {
                "id": "r006-3e8cdeab-82ec-4ffc-bbd4-53ec91b92a57",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-7e371d94-51c1-4636-a01b-8b469c6bde5c/routing_tables/r006-3e8cdeab-82ec-4ffc-bbd4-53ec91b92a57",
                "name": "polymer-tavern-remolded-fretted",
                "resource_type": "routing_table",
            },
            "default_security_group": {
                "id": "r006-5516747e-c011-4a7c-86ae-ba9b77dea82c",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::security-group:r006-5516747e-c011-4a7c-86ae-ba9b77dea82c",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/security_groups/r006-5516747e-c011-4a7c-86ae-ba9b77dea82c",
                "name": "cost-scorebook-clique-slam",
            },
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
            "cse_source_ips": [
                {
                    "ip": {"address": "10.249.66.135"},
                    "zone": {
                        "name": "us-south-1",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                    },
                },
                {
                    "ip": {"address": "10.12.158.167"},
                    "zone": {
                        "name": "us-south-2",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-2",
                    },
                },
                {
                    "ip": {"address": "10.12.165.215"},
                    "zone": {
                        "name": "us-south-3",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-3",
                    },
                },
            ],
        },
        {
            "id": "r006-d0d3c70f-0e56-4d72-a635-7378824257ba",
            "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::vpc:r006-d0d3c70f-0e56-4d72-a635-7378824257ba",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-d0d3c70f-0e56-4d72-a635-7378824257ba",
            "name": "test2-2",
            "resource_type": "vpc",
            "status": "available",
            "classic_access": False,
            "created_at": "2021-05-09T20:12:15Z",
            "default_network_acl": {
                "id": "r006-81cf2221-f723-47d3-95d2-7066124cc202",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::network-acl:r006-81cf2221-f723-47d3-95d2-7066124cc202",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/network_acls/r006-81cf2221-f723-47d3-95d2-7066124cc202",
                "name": "freemason-vacuumed-libraries-tight",
            },
            "default_routing_table": {
                "id": "r006-b9d46fa5-c7f1-4cd3-8419-f334be100ab6",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-d0d3c70f-0e56-4d72-a635-7378824257ba/routing_tables/r006-b9d46fa5-c7f1-4cd3-8419-f334be100ab6",
                "name": "stipend-control-sandpit-suggest",
                "resource_type": "routing_table",
            },
            "default_security_group": {
                "id": "r006-13f3a00b-0375-4796-b337-5fd22cbc9596",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::security-group:r006-13f3a00b-0375-4796-b337-5fd22cbc9596",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/security_groups/r006-13f3a00b-0375-4796-b337-5fd22cbc9596",
                "name": "jawed-paralyses-affiliate-sheath",
            },
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
            "cse_source_ips": [
                {
                    "ip": {"address": "10.12.120.90"},
                    "zone": {
                        "name": "us-south-1",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                    },
                },
                {
                    "ip": {"address": "10.12.160.160"},
                    "zone": {
                        "name": "us-south-2",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-2",
                    },
                },
                {
                    "ip": {"address": "10.12.171.195"},
                    "zone": {
                        "name": "us-south-3",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-3",
                    },
                },
            ],
        },
        {
            "id": "r006-d263746c-260c-4151-9748-05de5ed1ea03",
            "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::vpc:r006-d263746c-260c-4151-9748-05de5ed1ea03",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-d263746c-260c-4151-9748-05de5ed1ea03",
            "name": "sesame-crestless-excursus-evident",
            "resource_type": "vpc",
            "status": "available",
            "classic_access": False,
            "created_at": "2021-05-07T05:55:34Z",
            "default_network_acl": {
                "id": "r006-2f09e9db-bc13-4b3e-b7b8-4426f7bf635f",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::network-acl:r006-2f09e9db-bc13-4b3e-b7b8-4426f7bf635f",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/network_acls/r006-2f09e9db-bc13-4b3e-b7b8-4426f7bf635f",
                "name": "ebook-uncooked-liable-almanac",
            },
            "default_routing_table": {
                "id": "r006-f2660956-51dd-462a-b424-77cba31533c0",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-d263746c-260c-4151-9748-05de5ed1ea03/routing_tables/r006-f2660956-51dd-462a-b424-77cba31533c0",
                "name": "entire-speech-fridge-sanded",
                "resource_type": "routing_table",
            },
            "default_security_group": {
                "id": "r006-67ab2f42-9418-4286-8cda-02f5af49088b",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::security-group:r006-67ab2f42-9418-4286-8cda-02f5af49088b",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/security_groups/r006-67ab2f42-9418-4286-8cda-02f5af49088b",
                "name": "kerchief-handgrip-staleness-foe",
            },
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
            "cse_source_ips": [
                {
                    "ip": {"address": "10.249.66.127"},
                    "zone": {
                        "name": "us-south-1",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                    },
                },
                {
                    "ip": {"address": "10.12.158.155"},
                    "zone": {
                        "name": "us-south-2",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-2",
                    },
                },
                {
                    "ip": {"address": "10.12.170.164"},
                    "zone": {
                        "name": "us-south-3",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-3",
                    },
                },
            ],
        },
    ],
}


POST_VPCS_RESPONSE = GET_VPCS_RESPONSE["vpcs"][0]

GET_VPC_BY_ID_RESPONSE = POST_VPCS_RESPONSE

PATCH_VPC_BY_ID_RESPONSE = GET_VPC_BY_ID_RESPONSE
PATCH_VPC_BY_ID_RESPONSE["name"] = "test2-updated"


# SUBNETS
GET_SUBNETS_RESPONSE = {
    "limit": 50,
    "first": {"href": "https://us-south.iaas.cloud.ibm.com/v1/subnets?limit=50"},
    "total_count": 1,
    "subnets": [
        {
            "id": "0717-e7127621-d990-42a8-bb4b-7365402aab33",
            "crn": "crn:v1:bluemix:public:is:us-south-1:a/0f0d916bcdeb41fc82e06b1b60b219b9::subnet:0717-e7127621-d990-42a8-bb4b-7365402aab33",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/subnets/0717-e7127621-d990-42a8-bb4b-7365402aab33",
            "name": "my-subnet-1",
            "resource_type": "subnet",
            "available_ipv4_address_count": 3,
            "ipv4_cidr_block": "10.240.0.0/29",
            "ip_version": "ipv4",
            "zone": {
                "name": "us-south-1",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
            },
            "vpc": {
                "id": "r006-192412ca-4ab4-4e00-a852-188047f8698d",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::vpc:r006-192412ca-4ab4-4e00-a852-188047f8698d",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-192412ca-4ab4-4e00-a852-188047f8698d",
                "name": "my-vpc-2-updated",
                "resource_type": "vpc",
            },
            "status": "available",
            "total_ipv4_address_count": 8,
            "created_at": "2021-05-05T10:54:37Z",
            "network_acl": {
                "id": "r006-848ce071-a794-4948-833b-82fba500dc61",
                "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::network-acl:r006-848ce071-a794-4948-833b-82fba500dc61",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/network_acls/r006-848ce071-a794-4948-833b-82fba500dc61",
                "name": "washhouse-visa-xray-superhero",
            },
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
            "routing_table": {
                "id": "r006-49b618cf-4f46-4b66-8308-07af99c196e7",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/r006-192412ca-4ab4-4e00-a852-188047f8698d/routing_tables/r006-49b618cf-4f46-4b66-8308-07af99c196e7",
                "name": "bakeshop-outboard-marbled-sullen",
                "resource_type": "routing_table",
            },
        }
    ],
}


POST_SUBNETS_RESPONSE = GET_SUBNETS_RESPONSE["subnets"][0]

GET_SUBNET_BY_ID_RESPONSE = POST_SUBNETS_RESPONSE
GET_SUBNET_BY_ID_RESPONSE["status"] = "available"

PATCH_SUBNET_BY_ID_RESPONSE = GET_SUBNET_BY_ID_RESPONSE
PATCH_SUBNET_BY_ID_RESPONSE.update({"name": "my-subnet-1-modified"})


# KEYS
GET_KEYS_RESPONSE = {
    "keys": [
        {
            "id": "r006-b98ab62e-45eb-4791-aea4-bb2b11635271",
            "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::key:r006-b98ab62e-45eb-4791-aea4-bb2b11635271",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/keys/r006-b98ab62e-45eb-4791-aea4-bb2b11635271",
            "fingerprint": "SHA256:yEC4lTys+UrUiAmfcfdkQwThQ6C3RTZEetbywTjIVRk",
            "name": "my-key-1",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwM/8slSaAsMkP91qWDKD20+ZNq6dLu+qoE/oglPwJJBxpDU/T0wJ2LmfHSsRUNxX9ZA/CMkHsFJ0Gbuqvz0lx4TPN4AGNIr5bWj4VZp2LXibQ3QJkhkK3qdhUIyTY34qtEea8UYviZUAmROe2MMTpYayxsbnTDMw/RJjQ/d3W9hPSGQl7XLmI8Qvpxg5OBuopVllzUOF00hYyLaqtmpr+DaXHt0AVHu3HfH07TDGrVlqbrKo+BPLxv7bOvVJ5z5Ab/H1KcrgiVipcCunqCK+wnLTSeeIQF7x/lclo/SvWalSj+zQ+GfipZpI5R5ZHpFkPAq8OLly6ErKsqnwN8H2r",
            "type": "rsa",
            "length": 2048,
            "created_at": "2021-05-05T11:50:30Z",
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
        },
        {
            "id": "r006-95b4aa4f-be7d-41b1-9231-22bb6dd88ae9",
            "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::key:r006-95b4aa4f-be7d-41b1-9231-22bb6dd88ae9",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/keys/r006-95b4aa4f-be7d-41b1-9231-22bb6dd88ae9",
            "fingerprint": "SHA256:MEn7Rvec7ATaa6ZX9M1eDMBJu1GrVmiZqiFzw+cDfog",
            "name": "my-key-2",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwM/8slSaAsMkP91qWDKD20+ZNq6dLu+qoE/oglPwJJBxpDU/T0wJ2LmfHSsRUNxX9ZA/CMkHsFJ0Gbuqvz0lx4TPN4AGNIr5bWj4VZp2LXibQ3QJkhkK3qdhUIyTY34qtEea8UYviZUAmROe2MMTpYayxsbnTDMw/RJjQ/d3W9hPSGQl7XLmI8Qvpxg5OBuopVllzUOF00hYyLaqtmpr+DaXHt0AVHu3HfH07TDGrVlqbrKo+BPLxv7bOvVJ5z5Ab/H1KcrgiVipcCunqCK+wnLTSeeIQF7x/lclo/SvWalSj+zQ+GfipZpI5R5ZHpFkPAq8OLly6ErKsqnwN8H2s",
            "type": "rsa",
            "length": 2048,
            "created_at": "2021-05-10T06:53:21Z",
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
        },
    ]
}

GET_KEY_BY_ID_RESPONSE = GET_KEYS_RESPONSE["keys"][0]

POST_KEYS_RESPONSE = GET_KEY_BY_ID_RESPONSE

PATCH_KEY_BY_ID_RESPONSE = {
    "id": "r006-bd961078-f094-43fa-8201-dc193b4768ca",
    "crn": "crn:v1:bluemix:public:is:us-south:a/0f0d916bcdeb41fc82e06b1b60b219b9::key:r006-bd961078-f094-43fa-8201-dc193b4768ca",
    "href": "https://us-south.iaas.cloud.ibm.com/v1/keys/r006-bd961078-f094-43fa-8201-dc193b4768ca",
    "fingerprint": "SHA256:yEC4lTys+UrUiAmfcfdkQwThQ6C3RTZEetbywTjIVRk",
    "name": "my-key-1-modified",
    "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwM/8slSaAsMkP91qWDKD20+ZNq6dLu+qoE/oglPwJJBxpDU/T0wJ2LmfHSsRUNxX9ZA/CMkHsFJ0Gbuqvz0lx4TPN4AGNIr5bWj4VZp2LXibQ3QJkhkK3qdhUIyTY34qtEea8UYviZUAmROe2MMTpYayxsbnTDMw/RJjQ/d3W9hPSGQl7XLmI8Qvpxg5OBuopVllzUOF00hYyLaqtmpr+DaXHt0AVHu3HfH07TDGrVlqbrKo+BPLxv7bOvVJ5z5Ab/H1KcrgiVipcCunqCK+wnLTSeeIQF7x/lclo/SvWalSj+zQ+GfipZpI5R5ZHpFkPAq8OLly6ErKsqnwN8H2r",
    "type": "rsa",
    "length": 2048,
    "created_at": "2021-05-05T11:19:46Z",
    "resource_group": {
        "id": "ea28d6d5de624c9e974fda9ecd3f4263",
        "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
        "name": "Default",
    },
}


# INSTANCES

GET_INSTANCES_RESPONSE_OLD = {
    "first": {"href": "https://us-south.iaas.cloud.ibm.com/v1/instances?limit=20"},
    "instances": [
        {
            "bandwidth": 1000,
            "boot_volume_attachment": {
                "deleted": {
                    "more_info": "https://cloud.ibm.com/apidocs/vpc#deleted-resources"
                },
                "device": {"id": "80b3e36e-41f4-40e9-bd56-beae81792a68"},
                "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/1e09281b-f177-46fb-baf1-bc152b2e391a/volume_attachments/82cbf856-9cbb-45fb-b62f-d7bcef32399a",
                "id": "82cbf856-9cbb-45fb-b62f-d7bcef32399a",
                "name": "my-volume-attachment",
                "volume": {
                    "crn": "crn:v1:bluemix:public:is:us-south-1:a/123456::volume:1a6b7274-678d-4dfb-8981-c71dd9d4daa5",
                    "deleted": {
                        "more_info": "https://cloud.ibm.com/apidocs/vpc#deleted-resources"
                    },
                    "href": "https://us-south.iaas.cloud.ibm.com/v1/volumes/1a6b7274-678d-4dfb-8981-c71dd9d4daa5",
                    "id": "1a6b7274-678d-4dfb-8981-c71dd9d4daa5",
                    "name": "my-volume",
                },
            },
            "created_at": "2019-01-01T12:00:00.000Z",
            "crn": "crn:v1:bluemix:public:is:us-south-1:a/123456::instance:1e09281b-f177-46fb-baf1-bc152b2e391a",
            "gpu": {
                "count": 1,
                "manufacturer": "nvidia",
                "memory": 1,
                "model": "Tesla V100",
            },
            "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/1e09281b-f177-46fb-baf1-bc152b2e391a",
            "id": "1e09281b-f177-46fb-baf1-bc152b2e391a",
            "image": {
                "crn": "crn:v1:bluemix:public:is:us-south:a/123456::image:72b27b5c-f4b0-48bb-b954-5becc7c1dcb8",
                "deleted": {
                    "more_info": "https://cloud.ibm.com/apidocs/vpc#deleted-resources"
                },
                "href": "https://us-south.iaas.cloud.ibm.com/v1/images/72b27b5c-f4b0-48bb-b954-5becc7c1dcb8",
                "id": "72b27b5c-f4b0-48bb-b954-5becc7c1dcb8",
                "name": "my-image",
            },
            "memory": 8,
            "name": "my-instance",
            "network_interfaces": [
                {
                    "deleted": {
                        "more_info": "https://cloud.ibm.com/apidocs/vpc#deleted-resources"
                    },
                    "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/1e09281b-f177-46fb-baf1-bc152b2e391a/network_interfaces/10c02d81-0ecb-4dc5-897d-28392913b81e",
                    "id": "10c02d81-0ecb-4dc5-897d-28392913b81e",
                    "name": "my-network-interface",
                    "primary_ipv4_address": "192.168.3.4",
                    "resource_type": "network_interface",
                    "subnet": {
                        "crn": "crn:v1:bluemix:public:is:us-south-1:a/123456::subnet:7ec86020-1c6e-4889-b3f0-a15f2e50f87e",
                        "deleted": {
                            "more_info": "https://cloud.ibm.com/apidocs/vpc#deleted-resources"
                        },
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/subnets/7ec86020-1c6e-4889-b3f0-a15f2e50f87e",
                        "id": "7ec86020-1c6e-4889-b3f0-a15f2e50f87e",
                        "name": "my-subnet",
                    },
                }
            ],
            "primary_network_interface": {
                "deleted": {
                    "more_info": "https://cloud.ibm.com/apidocs/vpc#deleted-resources"
                },
                "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/1e09281b-f177-46fb-baf1-bc152b2e391a/network_interfaces/10c02d81-0ecb-4dc5-897d-28392913b81e",
                "id": "10c02d81-0ecb-4dc5-897d-28392913b81e",
                "name": "my-network-interface",
                "primary_ipv4_address": "192.168.3.4",
                "resource_type": "network_interface",
                "subnet": {
                    "crn": "crn:v1:bluemix:public:is:us-south-1:a/123456::subnet:7ec86020-1c6e-4889-b3f0-a15f2e50f87e",
                    "deleted": {
                        "more_info": "https://cloud.ibm.com/apidocs/vpc#deleted-resources"
                    },
                    "href": "https://us-south.iaas.cloud.ibm.com/v1/subnets/7ec86020-1c6e-4889-b3f0-a15f2e50f87e",
                    "id": "7ec86020-1c6e-4889-b3f0-a15f2e50f87e",
                    "name": "my-subnet",
                },
            },
            "profile": {
                "href": "https://us-south.iaas.cloud.ibm.com/v1/instance/profiles/bc1-4x16",
                "name": "bc1-4x16",
            },
            "resource_group": {
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/fee82deba12e4c0fb69c3b09d1f12345",
                "id": "fee82deba12e4c0fb69c3b09d1f12345",
                "name": "my-resource-group",
            },
            "status": "deleting",
            "vcpu": {"architecture": "amd64", "count": 4},
            "volume_attachments": [
                {
                    "deleted": {
                        "more_info": "https://cloud.ibm.com/apidocs/vpc#deleted-resources"
                    },
                    "device": {"id": "80b3e36e-41f4-40e9-bd56-beae81792a68"},
                    "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/1e09281b-f177-46fb-baf1-bc152b2e391a/volume_attachments/82cbf856-9cbb-45fb-b62f-d7bcef32399a",
                    "id": "82cbf856-9cbb-45fb-b62f-d7bcef32399a",
                    "name": "my-volume-attachment",
                    "volume": {
                        "crn": "crn:v1:bluemix:public:is:us-south-1:a/123456::volume:1a6b7274-678d-4dfb-8981-c71dd9d4daa5",
                        "deleted": {
                            "more_info": "https://cloud.ibm.com/apidocs/vpc#deleted-resources"
                        },
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/volumes/1a6b7274-678d-4dfb-8981-c71dd9d4daa5",
                        "id": "1a6b7274-678d-4dfb-8981-c71dd9d4daa5",
                        "name": "my-volume",
                    },
                }
            ],
            "vpc": {
                "crn": "crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b",
                "deleted": {
                    "more_info": "https://cloud.ibm.com/apidocs/vpc#deleted-resources"
                },
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/4727d842-f94f-4a2d-824a-9bc9b02c523b",
                "id": "4727d842-f94f-4a2d-824a-9bc9b02c523b",
                "name": "my-vpc",
            },
            "zone": {
                "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                "name": "us-south-1",
            },
        }
    ],
    "limit": 20,
    "next": {
        "href": "https://us-south.iaas.cloud.ibm.com/v1/instances?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=20"
    },
    "total_count": 132,
}

GET_INSTANCES_RESPONSE = {
    "first": {"href": "https://us-south.iaas.cloud.ibm.com/v1/instances?limit=50"},
    "instances": [
        {
            "bandwidth": 4000,
            "boot_volume_attachment": {
                "device": {"id": "a8a15363-a6f7-4f01-af60-715e85b28141"},
                "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/eb1b7391-2ca2-4ab5-84a8-b92157a633b0/volume_attachments/7389-a8a15363-a6f7-4f01-af60-715e85b28141",
                "id": "a8a15363-a6f7-4f01-af60-715e85b28141",
                "name": "my-boot-volume-attachment",
                "volume": {
                    "crn": "crn:[...]",
                    "href": "https://us-south.iaas.cloud.ibm.com/v1/volumes/49c5d61b-41e7-4c01-9b7a-1a97366c6916",
                    "id": "49c5d61b-41e7-4c01-9b7a-1a97366c6916",
                    "name": "my-boot-volume",
                },
            },
            "created_at": "2020-03-26T16:11:57Z",
            "crn": "crn:[...]",
            "dedicated_host": {
                "crn": "crn:[...]",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/dedicated_hosts/0787-8c2a09be-ee18-4af2-8ef4-6a6060732221",
                "id": "0787-8c2a09be-ee18-4af2-8ef4-6a6060732221",
                "name": "test-new",
                "resource_type": "dedicated_host",
            },
            "disks": [],
            "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/eb1b7391-2ca2-4ab5-84a8-b92157a633b0",
            "id": "eb1b7391-2ca2-4ab5-84a8-b92157a633b0",
            "image": {
                "crn": "crn:[...]",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/images/9aaf3bcb-dcd7-4de7-bb60-24e39ff9d366",
                "id": "9aaf3bcb-dcd7-4de7-bb60-24e39ff9d366",
                "name": "my-image",
            },
            "memory": 8,
            "name": "my-instance",
            "network_interfaces": [
                {
                    "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/e402fa1b-96f6-4aa2-a8d7-703aac843651/network_interfaces/7ca88dfb-8962-469d-b1de-1dd56f4c3275",
                    "id": "7ca88dfb-8962-469d-b1de-1dd56f4c3275",
                    "name": "my-network-interface",
                    "primary_ipv4_address": "10.0.0.32",
                    "resource_type": "network_interface",
                    "subnet": {
                        "crn": "crn:[...]",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/subnets/7389-bea6a632-5e13-42a4-b4b8-31dc877abfe4",
                        "id": "bea6a632-5e13-42a4-b4b8-31dc877abfe4",
                        "name": "my-subnet",
                    },
                }
            ],
            "placement_target": {
                "crn": "crn:[...]",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/dedicated_hosts/0787-8c2a09be-ee18-4af2-8ef4-6a6060732221",
                "id": "0787-8c2a09be-ee18-4af2-8ef4-6a6060732221",
                "name": "test-new",
                "resource_type": "dedicated_host",
            },
            "primary_network_interface": {
                "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/e402fa1b-96f6-4aa2-a8d7-703aac843651/network_interfaces/7ca88dfb-8962-469d-b1de-1dd56f4c3275",
                "id": "7ca88dfb-8962-469d-b1de-1dd56f4c3275",
                "name": "my-network-interface",
                "primary_ipv4_address": "10.0.0.32",
                "resource_type": "network_interface",
                "subnet": {
                    "crn": "crn:[...]",
                    "href": "https://us-south.iaas.cloud.ibm.com/v1/subnets/bea6a632-5e13-42a4-b4b8-31dc877abfe4",
                    "id": "bea6a632-5e13-42a4-b4b8-31dc877abfe4",
                    "name": "my-subnet",
                },
            },
            "profile": {
                "href": "https://us-south.iaas.cloud.ibm.com/v1/instance/profiles/bx2-2x8",
                "name": "bx2-2x8",
            },
            "resource_group": {
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/4bbce614c13444cd8fc5e7e878ef8e21",
                "id": "4bbce614c13444cd8fc5e7e878ef8e21",
                "name": "Default",
            },
            "status": "running",
            "status_reasons": [],
            "vcpu": {"architecture": "amd64", "count": 2},
            "volume_attachments": [
                {
                    "device": {"id": "a8a15363-a6f7-4f01-af60-715e85b28141"},
                    "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/e402fa1b-96f6-4aa2-a8d7-703aac843651/volume_attachments/7389-a8a15363-a6f7-4f01-af60-715e85b28141",
                    "id": "a8a15363-a6f7-4f01-af60-715e85b28141",
                    "name": "my-boot-volume-attachment",
                    "volume": {
                        "crn": "crn:[...]",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/volumes/49c5d61b-41e7-4c01-9b7a-1a97366c6916",
                        "id": "49c5d61b-41e7-4c01-9b7a-1a97366c6916",
                        "name": "my-boot-volume",
                    },
                },
                {
                    "device": {"id": "e77125cb-4df0-4988-a878-531ae0ae0b70"},
                    "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/e402fa1b-96f6-4aa2-a8d7-703aac843651/volume_attachments/7389-e77125cb-4df0-4988-a878-531ae0ae0b70",
                    "id": "e77125cb-4df0-4988-a878-531ae0ae0b70",
                    "name": "my-volume-attachment-1",
                    "volume": {
                        "crn": "crn:[...]",
                        "href": "https://us-south.iaas.cloud.ibm.com/v1/volumes/2cc091f5-4d46-48f3-99b7-3527ae3f4392",
                        "id": "2cc091f5-4d46-48f3-99b7-3527ae3f4392",
                        "name": "my-data-volume",
                    },
                },
            ],
            "vpc": {
                "crn": "crn:[...]",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/vpcs/f0aae929-7047-46d1-92e1-9102b07a7f6f",
                "id": "f0aae929-7047-46d1-92e1-9102b07a7f6f",
                "name": "my-vpc",
            },
            "zone": {
                "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                "name": "us-south-1",
            },
        }
    ],
    "limit": 50,
    "total_count": 1,
}

GET_INSTANCE_BY_ID_RESPONSE = GET_INSTANCES_RESPONSE["instances"][0]

POST_INSTANCES_RESPONSE = GET_INSTANCE_BY_ID_RESPONSE

PATCH_INSTANCE_BY_ID_RESPONSE = GET_INSTANCE_BY_ID_RESPONSE
PATCH_INSTANCE_BY_ID_RESPONSE["name"] = "my-instance-updated"

# FLOATING IPS
GET_FLOATING_IPS_RESPONSE_OLD = {
    "limit": 50,
    "first": {"href": "https://us-south.iaas.cloud.ibm.com/v1/floating_ips?limit=50"},
    "total_count": 1,
    "floating_ips": [
        {
            "id": "r006-e554cebe-3de3-40d3-b094-54dc2d8e6d8f",
            "crn": "crn:v1:bluemix:public:is:us-south-1:a/0f0d916bcdeb41fc82e06b1b60b219b9::floating-ip:r006-e554cebe-3de3-40d3-b094-54dc2d8e6d8f",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/floating_ips/r006-e554cebe-3de3-40d3-b094-54dc2d8e6d8f",
            "address": "169.48.152.25",
            "name": "my-floating-ip-1-updated",
            "status": "available",
            "created_at": "2021-05-05T13:41:41Z",
            "zone": {
                "name": "us-south-1",
                "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
            },
            "resource_group": {
                "id": "ea28d6d5de624c9e974fda9ecd3f4263",
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/ea28d6d5de624c9e974fda9ecd3f4263",
                "name": "Default",
            },
        }
    ],
}

GET_FLOATING_IPS_RESPONSE = {
    "first": {"href": "https://us-south.iaas.cloud.ibm.com/v1/floating_ips?limit=50"},
    "floating_ips": [
        {
            "address": "192.0.2.2",
            "created_at": "2019-01-28T12:08:05Z",
            "crn": "crn:[...]",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/floating_ips/4dd1852a-3373-46c0-9240-f9c7f0d0c1a3",
            "id": "4dd1852a-3373-46c0-9240-f9c7f0d0c1a3",
            "name": "my-floating-ip-1",
            "resource_group": {
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/4bbce614c13444cd8fc5e7e878ef8e21",
                "id": "4bbce614c13444cd8fc5e7e878ef8e21",
                "name": "Default",
            },
            "status": "pending",
            "target": {
                "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/f2a2ab09-0c9e-4b2d-a1cf-7425d1c834b9/network_interfaces/bd5f7dc3-93c7-4d3a-89b4-26c4cc364a2",
                "id": "bd5f7dc3-93c7-4d3a-89b4-26c4cc364a2",
                "name": "my-network-interface-1",
                "primary_ipv4_address": "10.0.1.9",
                "resource_type": "network_interface",
            },
            "zone": {
                "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                "name": "us-south-1",
            },
        },
        {
            "address": "198.51.100.1",
            "created_at": "2019-01-29T12:08:05Z",
            "crn": "crn:[...]",
            "href": "https://us-south.iaas.cloud.ibm.com/v1/floating_ips/64580c28-713a-4cda-9993-53bc6a529bb4",
            "id": "64580c28-713a-4cda-9993-53bc6a529bb4",
            "name": "my-floating-ip-2",
            "resource_group": {
                "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/4bbce614c13444cd8fc5e7e878ef8e21",
                "id": "4bbce614c13444cd8fc5e7e878ef8e21",
                "name": "Default",
            },
            "status": "pending",
            "target": {
                "href": "https://us-south.iaas.cloud.ibm.com/v1/instances/f2a2ab09-0c9e-4b2d-a1cf-7425d1c834b9/network_interfaces/bd5f7dc3-93c7-4d3a-89b4-26c4cc364a32",
                "id": "bd5f7dc3-93c7-4d3a-89b4-26c4cc364",
                "name": "my-network-interface-1",
                "primary_ipv4_address": "10.0.1.10",
                "resource_type": "network_interface",
            },
            "zone": {
                "href": "https://us-south.iaas.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                "name": "us-south-1",
            },
        },
    ],
    "limit": 50,
    "total_count": 2,
}

GET_FLOATING_IP_BY_ID_RESPONSE = GET_FLOATING_IPS_RESPONSE["floating_ips"][0]

POST_FLOATING_IPS_RESPONSE = GET_FLOATING_IP_BY_ID_RESPONSE

PATCH_FLOATING_IP_BY_ID_RESPONSE = GET_FLOATING_IP_BY_ID_RESPONSE
PATCH_FLOATING_IP_BY_ID_RESPONSE["name"] = "my-floating-ip-updated"