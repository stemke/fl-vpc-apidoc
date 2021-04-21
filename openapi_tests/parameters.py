# import requests
# import json
# import sys


# with open("./openapi.json") as f:
#     API_SPEC = json.load(f)

# # paths = API_SPEC["components"]

# # for k,v in paths.items():
# #     # print(v)
# #     break
# # # print(API_SPEC["components"])
# # # print(API_SPEC["servers"])

# # SERVER_URLS = [s["url"] for s in API_SPEC["servers"]]



# # VPC_API_ENDPOINT = "https://us-south.iaas.cloud.ibm.com"
# # r = f"{VPC_API_ENDPOINT}/v1/vpcs?version=2021-01-01&generation=2"

# # print(r)




# import requests
# from urllib.parse import urlsplit, urlparse, parse_qs

# with open("./iam_token.txt") as f:
#     iam_token = f.read().strip()


# HEADERS = {
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Accept": "application/json",
#     "Authorization": iam_token,
#     "token_type": "Bearer",
# }

# session = requests.Session()
# session.headers = HEADERS

# VPC_API_ENDPOINT = "https://us-south.iaas.cloud.ibm.com"

# # GET /vpcs

# # r = session.get(f"{VPC_API_ENDPOINT}/v1/vpcs?version=2021-01-01&generation=2&love=3")
# # print(parse_qs(urlparse(r.url).query))

# TEST_PATHS = {
#     "vpcs": "/vpcs"
# }


# def get_params(path, method):
#     loc = API_SPEC["paths"][TEST_PATHS[path]]
#     required = []
#     optional = []

#     params = loc["parameters"]
#     for p in params:
#         required.append(p)

#     for p in loc[method]["parameters"]:
#         if p.get("$ref"):
#             optional.append(p["$ref"].rsplit("/", 1)[-1])

#     return required, optional

# # get_params("vpcs", "post")