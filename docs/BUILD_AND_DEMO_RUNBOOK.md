# Build and Demo Runbook

1. Create a Python virtual environment.
2. Install `requirements.txt`.
3. Copy `.env.example` to `.env`.
4. Add an NVIDIA API key only when enabling the live-model integration.
5. Run policy tests with `python -m unittest discover -s tests -v`.
6. Launch with `streamlit run src/app.py`.
7. Execute the VPN anchor scenario.
8. Demonstrate one low-risk action that is allowed.
9. Demonstrate one privileged action that is blocked or queued for approval.
10. Review the audit trail.

The starter version runs the deterministic control flow without requiring live infrastructure. The next implementation phase wires the recommendation layer to NVIDIA NIM while keeping action authorization outside the model.
