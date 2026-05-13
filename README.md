# NemoClaw Community

[![License](https://img.shields.io/badge/License-Apache_2.0-blue)](LICENSE)
[![Security Policy](https://img.shields.io/badge/Security-Report%20a%20Vulnerability-red)](SECURITY.md)

NemoClaw Community is a collection of NemoClaw examples for building constrained, inspectable agent workflows.

## What's Here

| Directory | Description |
| --------- | ----------- |
| `examples/personal-community-sentiment-triage/` | Hermes-based NemoClaw example for community sentiment triage across Slack, Outlook, GitHub mirrors, and NVIDIA forum mirrors. |
| `scripts/` | Repository maintenance checks used by CI. |

## Getting Started

The NemoClaw CLI is intended to become the stable entry point for these examples. During the current preview, each example includes local scripts that perform the lower-level runtime setup.

Clone the repository and move into the example:

```bash
git clone https://github.com/NVIDIA/nemoclaw-community.git
cd nemoclaw-community/examples/personal-community-sentiment-triage
```

Then follow the full setup guide in [examples/personal-community-sentiment-triage/README.md](examples/personal-community-sentiment-triage/README.md).

## Requirements

- Linux host with Docker or a compatible container runtime
- NemoClaw CLI when available, or the preview runtime prerequisites documented by each example
- Access to an OpenAI-compatible inference endpoint
- Optional integration credentials for Slack, Microsoft Graph/Outlook, GitHub, and source ETL mirrors

This project will download and install additional third-party open source software projects. Review the license terms of these open source projects before use. See [THIRD-PARTY-NOTICES](THIRD-PARTY-NOTICES) for the repository inventory.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). This project uses Developer Certificate of Origin sign-offs for inbound contributions.

## Security

See [SECURITY.md](SECURITY.md). Do not file public GitHub issues for security vulnerabilities.

## Support

See [SUPPORT.md](SUPPORT.md) for support channels and expectations.

## Governance And Maintainers

- Governance: [GOVERNANCE.md](GOVERNANCE.md)
- Maintainers: [MAINTAINERS.md](MAINTAINERS.md)
- Code owners: [.github/CODEOWNERS](.github/CODEOWNERS)

## License

This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE) for details.
