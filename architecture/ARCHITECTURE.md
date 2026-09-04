# Architecture

~~~text
Employee / Service Desk Ticket
           |
           v
Identity + Incident Scope
           |
           v
Deterministic Authorization
           |
    +------+------+
    |             |
    v             v
Evidence Tools   Approved KB / Runbooks
    |             |
    +------+------+
           v
Minimum Authorized Context
           |
           v
NVIDIA Nemotron / NIM
           |
           v
Recommendation + Proposed Action
           |
           v
Policy / Risk Engine
     +-----+------+
     |            |
 LOW / bounded   HIGH / privileged
     |            |
     v            v
 Auto execute    PENDING Human Approval
     |            |
     +-----+------+
           v
         Audit
~~~
