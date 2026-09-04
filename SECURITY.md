# Security Model

OpsGuard AI treats the language model as a reasoning component, not a security boundary.

## Invariants

- Authorization is evaluated before tool execution.
- Privileged actions require explicit approval.
- Secrets are never supplied to the model context.
- Only approved knowledge sources are retrievable.
- Retrieved text is treated as untrusted data.
- The model cannot grant itself permissions.
- Every proposed and executed action is auditable.

## Risk classes

- LOW: read-only diagnostics, approved cache refresh, local client reconnect.
- MEDIUM: user-scoped configuration reset; requires policy-specific approval.
- HIGH: service restart, firewall change, identity privilege change, credential rotation; always human-approved in this PoC.
