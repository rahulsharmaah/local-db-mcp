---
id: codex-cloud
title: Codex Cloud
---

# Codex Cloud Setup

Codex Cloud runs in a remote workspace. It can install and run Local DB MCP there, but it cannot directly reach a database that only exists on a developer laptop as `localhost`.

Use Codex Cloud when the database is reachable from the cloud workspace, such as:

- a development database available on a private network reachable by the workspace
- a database exposed through an approved tunnel
- an ephemeral database started during workspace setup
- a checked-in SQLite fixture that contains no private data

## Install During Workspace Setup

Add Local DB MCP to the workspace setup steps:

```bash
python -m pip install "git+https://github.com/rahulsharmaah/local-db-mcp.git"
```

Create the MCP config file in the workspace environment and point `LOCAL_DB_MCP_CONFIG` to it:

```bash
mkdir -p ~/.local-db-mcp
cat > ~/.local-db-mcp/config.yaml <<'YAML'
default_limit: 100
allow_write_tools: false

databases: []
YAML
```

Populate `databases` from the workspace's approved secret manager or setup process. Do not commit real DSNs.

## MCP Server Definition

Use this server definition in the MCP configuration available to the Codex Cloud workspace:

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

## Recommended First Prompt

```text
Use the local-db MCP server. Run health_check and list_connections first.
Only run read-only queries and keep result limits small.
```

## Boundary

For laptop-only databases, use Codex desktop or another local MCP client instead. Codex Cloud should only be connected to databases that your organization has intentionally made reachable from the cloud workspace.
