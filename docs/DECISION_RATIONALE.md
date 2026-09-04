# Decision Rationale and Interview Defense

## Why NVIDIA Nemotron?
The demo is intended to show an enterprise AI operations workload on NVIDIA's model and inference ecosystem rather than a generic chatbot.

## Why deterministic action policy?
Language models are probabilistic. Infrastructure authorization must be explicit, testable and deny-by-default.

## Why human approval?
Consequential or privileged infrastructure actions can affect availability, security and compliance. The PoC therefore keeps those actions human-owned.

## Why synthetic evidence?
The project is a public portfolio demonstration. Synthetic data avoids exposing employer, customer, credential or operational information.

## Why this is more than RAG
RAG supplies trusted operational context. The differentiator is the governed action loop: evidence, reasoning, risk evaluation, bounded execution, approval and audit.
