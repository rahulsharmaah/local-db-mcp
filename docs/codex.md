# Codex Setup

Local DB MCP can be used in Codex desktop as a local MCP server or installed as a local Codex plugin bundle.

## Install the Server

```bash
python -m pip install "git+https://github.com/rahulsharmaah/local-db-mcp.git"
```

Create `~/.local-db-mcp/config.yaml` from `examples/config.example.yaml`, then add the MCP server to your Codex MCP configuration.

## MCP Server Configuration

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

## Local Plugin Bundle

This repository includes a Codex plugin manifest at:

```text
.codex-plugin/plugin.json
```

The plugin bundle registers the `local-db` MCP server and includes a Codex skill that tells the agent how to use the database tools safely.

After adding or updating a local plugin, restart Codex so the plugin and MCP tool list reload.

## Recommended Prompt

```text
Use the local-db MCP server. Start with health_check and list_connections.
Use read-only queries only unless I explicitly approve otherwise.
```
