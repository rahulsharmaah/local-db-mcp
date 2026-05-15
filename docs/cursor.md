# Cursor Setup

Install Local DB MCP:

```bash
pip install .
```

Create `~/.local-db-mcp/config.yaml` from `examples/config.example.yaml`.

This repo includes a Cursor MCP template at:

```text
.cursor/mcp.json
```

If your project uses a different path, copy this block into Cursor's MCP config:

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

Restart Cursor after changing MCP configuration.
