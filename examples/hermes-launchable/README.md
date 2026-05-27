# NemoClaw Hermes Brev Launchable

This example is a zero-to-one Brev launchable for creating a Hermes agent on a Brev CPU instance.

It is meant for people who want the fastest path from a fresh Brev machine to a working NemoClaw-managed Hermes sandbox. The notebook in this folder installs the host prerequisites, prompts for an NVIDIA Build API key, runs Hermes onboarding, verifies the Hermes API, and shows how to open the Hermes terminal experience through OpenShell.

## Get Started

Go to [Brev](https://brev.nvidia.com) to start from a CPU instance. After the Brev launchable is created, this example can be used as the source notebook for that launchable.

Until the launchable link exists, you can still run the notebook directly on a Brev CPU instance:

1. Open JupyterLab on the Brev instance.
2. Upload or open `hermes-brev-launchable.ipynb`.
3. Run the cells in order.
4. Paste your NVIDIA Build API key when prompted.

The notebook defaults are tuned for a small Brev CPU instance, including CPU-only sandbox creation, Docker host preparation, and a first-onboarding model that validates quickly.

## What This Creates

The notebook creates a NemoClaw sandbox configured for the Hermes agent. When onboarding finishes, you can:

- launch the Hermes terminal UI from the sandbox,
- call the Hermes OpenAI-compatible API on port `8642`,
- use `openshell term` to approve network requests and inspect policy activity.

This folder is intentionally self-contained. It is a Brev onboarding example for Hermes, not a replacement for the broader NemoClaw documentation.
