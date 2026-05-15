---
id: security
title: Security
---

# Security

Local DB MCP can access sensitive local databases when users configure it to do so.

Security expectations:

- DSNs and passwords must never be returned by tools.
- Query result size limits must remain in place.
- Read-only behavior must remain the default.
- Any future write-capable workflow must require explicit configuration and documentation.
- Users should use least-privilege database accounts.

Report vulnerabilities privately through GitHub Security Advisories when available.
