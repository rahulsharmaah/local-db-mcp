# Cursor Setup

Cursor supports MCP server configuration through a project or user MCP config. This repository includes a ready-to-copy template at `.cursor/mcp.json`.

## Install the Server

```bash
python -m pip install "git+https://github.com/rahulsharmaah/local-db-mcp.git"
```

Create `~/.local-db-mcp/config.yaml` from `examples/config.example.yaml`.

## Use the Cursor Template

```text
.cursor/mcp.json
```

If your Cursor setup uses a user-level MCP configuration instead, copy this server definition:

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

Restart Cursor after changing MCP configuration. Then ask Cursor to run `health_check` and `list_connections` before issuing database-specific queries.
