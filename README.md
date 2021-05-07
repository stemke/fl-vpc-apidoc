# FL VPC API Docs

[![test](https://github.com/stemke/fl-vpc-apidoc/actions/workflows/test.yml/badge.svg)](https://github.com/stemke/fl-vpc-apidoc/actions/workflows/test.yml)

Will use this space to submit the VPC API Doc automated test and results from Freelancer project.  Before you start, connect with project lead to understand the feedback template to use for issues, and get the list of methods to test.


## Generating iam_token

### Via IBM Cloud Console

```sh
$ iam_token=$(ibmcloud iam oauth-tokens | awk -F: '{ print $2}')
```

### Via python requests library

```python
import requests

def get_iam_token(api_token='your_api_key'):
    '''
    param: `api_token` parameter can be passed as method argument or from environment variables
    '''

    DEFAULT_IAM_URL = 'https://iam.cloud.ibm.com'
    CONTENT_TYPE = 'application/x-www-form-urlencoded'
    OPERATION_PATH = "/identity/token"
    REQUEST_TOKEN_GRANT_TYPE = 'urn:ibm:params:oauth:grant-type:apikey'
    REQUEST_TOKEN_RESPONSE_TYPE = 'cloud_iam'
    TOKEN_NAME = 'access_token'

    apikey = os.getenv('API_KEY', api_token)

    headers = {
        'Content-type': CONTENT_TYPE,
        'Accept': 'application/json'
    }

    data = {
        'grant_type': REQUEST_TOKEN_GRANT_TYPE,
        'apikey': apikey,
        'response_type': REQUEST_TOKEN_RESPONSE_TYPE
    }

    req = requests.post(f"{DEFAULT_IAM_URL}{OPERATION_PATH}", headers=headers, data=data).json()
    return req.get(TOKEN_NAME)

# My IAM TOKEN
iam_token = get_iam_token()
```

## Resources

* VPC API Docs site -> https://cloud.ibm.com/apidocs/vpc
* Python SDK repository -> https://github.com/IBM/vpc-python-sdk/
## Freelancer Results Template

1. VPC API operation being tested (e.g.: `GET /vpcs/<id>`):

    Sequence of `curl` commands used to test the operation:

2. Was the final `curl` command the same as the one in the API specification?  (Yes/No)

    If "No": was it changed becausethe specification's command did not work?

3. Was the output of the VPC API operation being tested compatible with the specification and/or specification example output? (Yes/No)

    If "No": list each incompatibility.

4. If there was no specification example output (and there should be), list a valid response/return example that should be added to the spec output.

Examples:
* Property `foo` was not present in the response but was marked required in the specification (and included in the example)
* HTTP status code `202` was required by the specification but code `204` was returned
* Property `bar` had value `Baz`, but only `baz` is allowed in the specification

## Test Endpoints

- `POST`, `GET` (individual), `GET` (list), `PATCH`, and `DELETE` for `/vpcs`
- `POST`, `GET` (individual), `GET` (list), `PATCH`, and `DELETE` for `/subnets`
- `POST`, `GET` (individual), `GET` (list), `PATCH`, and `DELETE` for `/keys`
- `POST`, `GET` (individual), `GET` (list), `PATCH`, and `DELETE` for `/instances`
- `POST`, `GET` (individual), `GET` (list), `PATCH`, and `DELETE` for `/floating_ips`

## Results


| method to test   | date tested | Github issue needed? | notes |
|----------------  |-------------|----------------------|-------|
| GET `/vpcs`      | 2021-04-07  |   n/a                | Gets a list of the VPCs. works as expected |
| GET `/vpcs/<id>` | 2021-04-07  |   n/a                | Get's a specific vpc using the id. works as expected |
| POST `/vpcs/`    | 2021-04-07  |   n/a                | Creates a new VPC once the name is passes as json in the payload. works as expected |


## Observations

- Documentation isn't very clear on how to use or generate `iam_token`
- Documentation doesn't specify that the purpose of using the `apikey` is so that you can generate the `iam_token` and neither dpes it show how to do it.
- id regex is in the form `^[-0-9a-z_]+$`. Since the example is meant to be a unique identifier and an example given is `7ec86020-1c6e-4889-b3f0-a15f2e50f87e`, I would have thought the regular expression should be ``^[-0-9a-f_]+$`` instead. This is the case for
  - `PUT /subnets/{id}`,
  - `subnets[{'id': 'id_val'}]` on `GET /subnets/`,


    **GET /v1/vpcs**
    * `resource_type` is missing from the api spec under `vpcs[]` on the left of the documentation page but is shown in the results.

    **GET /v1/vpcs/{id}**
    * `resource_type` is missing from the api spec response parameters

    **POST /v1/vpcs/**
    * `resource_group` needs to be passed as dict rather than by id. See example below

```python
# correct
r = requests.post(f"{API_ENDPOINT}/v1/vpcs?version=2021-04-20&generation=2",
        headers=HEADERS,
        json={
            'resource_group': {'id':'ea28d6d5de624c9e974fda9ecd3f4262'}
    }).json()

# wrong
r = requests.post(f"{API_ENDPOINT}/v1/vpcs?version=2021-04-20&generation=2",
      headers=HEADERS,
      json={
          'resource_group.id': 'ea28d6d5de624c9e974fda9ecd3f4262'
      }).json()
```


**GET /v1/subnets**
* `resource_type` is missing from the api spec response parameters.