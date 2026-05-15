---
id: client-templates
title: Client Templates
---

# Client Templates

The repository includes MCP templates that users can copy into their client configuration.

## Standard MCP Template

Use `.mcp.json` for clients that support repository-level MCP configuration:

```json
{
  "mcpServers": {
    "local-db": {
      "command": "local-db-mcp",
      "args": [],
      "env": {
        "LOCAL_DB_MCP_CONFIG": "~/.local-db-mcp/config.yaml"
      }
    }
  }
}
```

## Cursor Template

Cursor users can start from `.cursor/mcp.json`. After installing `local-db-mcp`, restart Cursor so the MCP server list reloads.

## Codex Plugin Bundle

Codex users can use the `.codex-plugin/plugin.json` manifest as the local plugin bundle entry point. The bundle also includes a Local DB MCP skill at `skills/local-db-mcp/SKILL.md`.

## Config File

The templates expect a config file at:

```text
~/.local-db-mcp/config.yaml
```

Set `LOCAL_DB_MCP_CONFIG` to a different path if your environment stores MCP configuration elsewhere.
