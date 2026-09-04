# NVIDIA OpsGuard AI

**Governed Agentic AI for Enterprise IT Operations**

> Resolve routine IT incidents in minutes instead of hours—without giving AI unrestricted control of enterprise infrastructure.

NVIDIA OpsGuard AI is a portfolio proof of concept showing how an enterprise AI operations agent can investigate incidents, retrieve approved operational knowledge, correlate evidence, recommend remediation, safely execute bounded low-risk actions, escalate privileged actions for human approval, and preserve a complete audit trail.

## Anchor scenario

An employee reports that the corporate VPN will not connect. OpsGuard AI:

1. validates the request and user context;
2. gathers synthetic endpoint, identity, VPN and service-health evidence;
3. retrieves only approved runbook and knowledge-base material;
4. uses an NVIDIA Nemotron model to reason over authorized context;
5. produces a probable root cause and remediation plan;
6. executes only explicitly permitted low-risk actions;
7. blocks or queues privileged actions for human approval; and
8. records evidence, recommendation, approvals and actions for auditability.

## Killer value proposition

- Lower mean time to resolution (MTTR)
- Deflect repetitive Level 1 support work
- Provide 24x7 first-response capability
- Preserve institutional operational knowledge
- Reduce unsafe or inconsistent manual remediation
- Keep privileged infrastructure actions under human control
- Create an auditable decision trail

## Core architecture principle

**The model is not the authorization layer.**

~~~text
User / Incident Context
        -> deterministic authorization
        -> approved evidence collectors
        -> approved KB / runbook retrieval
        -> minimum authorized context
        -> NVIDIA Nemotron reasoning
        -> remediation recommendation
        -> policy / risk evaluation
        -> bounded low-risk action OR PENDING approval
        -> execution / escalation
        -> audit trail
~~~

## Security demonstrations

- Prompt injection embedded in a troubleshooting note
- Attempt to request domain-admin or root-level action
- Unapproved runbook / poisoned knowledge source
- Credential or secret exfiltration request
- Autonomous restart of a critical production service
- Attempt to bypass human approval through prompt text

## Technology direction

- NVIDIA Nemotron via NVIDIA NIM APIs
- Python
- Streamlit
- Retrieval-Augmented Generation (RAG)
- Synthetic service desk, identity, endpoint and network data
- Deterministic policy checks
- Human-in-the-loop approval
- Immutable-style audit event model for the PoC

## Repository layout

~~~text
nvidia-opsguard-ai/
├── README.md
├── SECURITY.md
├── .env.example
├── requirements.txt
├── src/
│   ├── app.py
│   ├── agent.py
│   ├── policy.py
│   ├── tools.py
│   └── audit.py
├── demo/
│   └── DEMO_SCRIPT.md
├── tests/
│   └── test_policy.py
├── architecture/
│   └── ARCHITECTURE.md
├── docs/
│   ├── BUILD_AND_DEMO_RUNBOOK.md
│   ├── EXECUTIVE_BRIEF.md
│   └── DECISION_RATIONALE.md
└── presentation/
    └── README.md
~~~

## Portfolio thesis

> AI operations agents should be fast enough to reduce MTTR, constrained enough to protect production, and transparent enough to defend every consequential action.

## Important PoC notes

This repository uses synthetic data only and is not production-ready. Never place real credentials, secrets, customer information, privileged tokens or production incident data in the demo. Production deployment requires enterprise identity, secrets management, network controls, observability, resilience, legal/security review and organization-specific approval policy.
