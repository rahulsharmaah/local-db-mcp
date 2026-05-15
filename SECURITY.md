# Security Policy

Local DB MCP is designed for local development database inspection. It can access sensitive data if users configure sensitive databases, so security issues are taken seriously.

## Supported Versions

Security fixes are applied to the latest `main` branch until formal releases are introduced.

## Reporting a Vulnerability

Please report suspected vulnerabilities privately through GitHub Security Advisories when available.

Do not open a public issue for:

- Credential exposure
- Query safety bypasses
- Unauthorized write execution
- Secret leakage in MCP responses
- Unsafe default configuration

## Security Expectations

The server should:

- Refuse mutating SQL in read-only tools
- Avoid returning DSNs or credentials
- Limit result sizes
- Require explicit configuration for any future write-capable tooling
- Treat local databases as potentially sensitive production-like data

## User Responsibilities

Users should:

- Use least-privilege database accounts
- Prefer read-only database users
- Keep `~/.local-db-mcp/config.yaml` out of version control
- Avoid configuring production databases unless they fully understand the risk
