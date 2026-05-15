# Codex Setup

Install Local DB MCP:

```bash
pip install .
```

Create `~/.local-db-mcp/config.yaml` from `examples/config.example.yaml`, then add the MCP server to your Codex MCP configuration:

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

Recommended prompt:

```text
Use the local-db MCP server. Start with health_check and list_connections.
Use read-only queries only unless I explicitly approve otherwise.
```

This repository also includes `.codex-plugin/plugin.json` as a starting point for a local Codex plugin bundle.
