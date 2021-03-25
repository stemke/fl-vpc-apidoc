# fl-vpc-apidoc
Will use this space to submit the VPC API Doc automated test and results from Freelancer project.  Before you start, connect with project lead to understand the feedback template to use for issues, and get the list of methods to test.

**Freelancer Results Template**

1. VPC API operation being tested (e.g.: `GET /vpcs/<id>`):
  
    Sequence of `curl` commands used to test the operation:

2. Was the final `curl` command the same as the one in the API specification?  (Yes/No)

    If "No": was it changed becausethe specification's command did not work?

3. Was the output of the VPC API operation being tested compatible with the specification and/or specification example output? (Yes/No)

    If "No": list each incompatibility. If there was no specification example, list a validexample here.

Examples:
* Property `foo` was not present in the response but was marked required in the specification (and included in the example)
* HTTP status code `202` was required by the specification but code `204` was returned
* Property `bar` had value `Baz`, but only `baz` is allowed in the specification
