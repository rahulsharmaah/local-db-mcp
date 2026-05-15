---
id: intro
title: Introduction
slug: /
---

# Local DB MCP

Local DB MCP gives MCP clients a safe, consistent way to inspect developer-owned local databases.

It is built for teams that use AI coding tools and want database context without pasting credentials, connection strings, screenshots, or ad hoc query output into chat.

## What It Supports

- PostgreSQL
- MySQL and MariaDB
- SQLite
- MongoDB
- Redis key scanning

## Design Goals

- **Safe by default:** read-only query tools and strict result limits
- **Client agnostic:** works with Codex, Claude Desktop, Cursor, and any MCP-compatible client
- **Config driven:** users add local connection profiles once
- **Credential aware:** DSNs are loaded locally and never returned by MCP tools
- **Small and auditable:** clear Python modules with minimal moving parts

## Core Workflow

1. Install Local DB MCP.
2. Create `~/.local-db-mcp/config.yaml`.
3. Add your local database connection profiles.
4. Register the MCP server in your client.
5. Ask your client to run `health_check`, `list_connections`, and read-only queries.

## Included Client Assets

- `.mcp.json` standard MCP server template
- `.cursor/mcp.json` Cursor MCP template
- `.codex-plugin/plugin.json` Codex local plugin manifest
- `skills/local-db-mcp/SKILL.md` Codex usage guidance for safe database inspection
