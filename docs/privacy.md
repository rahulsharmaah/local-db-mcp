---
id: privacy
title: Privacy Policy
---

# Privacy Policy

Local DB MCP runs locally in the MCP client environment where it is installed. The project does not operate a hosted service and does not collect, store, or transmit usage data to the project maintainers.

Database credentials are read from the user's local configuration file. Tool responses are designed not to expose DSNs, passwords, tokens, or other connection secrets.

Users are responsible for configuring their MCP client, database credentials, network access, and workspace secrets according to their organization's security requirements.

## Data Access

Local DB MCP can query databases that the user configures. By default, the server exposes read-only inspection tools and applies result limits.

The project recommends using least-privilege, read-only database users in addition to the server's application-level write protections.

## Contact

Security and privacy concerns can be reported through the repository's security guidance:

```text
https://github.com/rahulsharmaah/local-db-mcp/blob/main/SECURITY.md
```
