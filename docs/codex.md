# Codex Setup

Run setup first:

```powershell
cd D:\local-db-mcp
.\scripts\setup.ps1
notepad $HOME\.local-db-mcp\config.yaml
```

Then add the MCP server to your Codex MCP configuration:

```json
{
  "mcpServers": {
    "local-db": {
      "command": "D:/local-db-mcp/.venv/Scripts/python.exe",
      "args": ["-m", "local_db_mcp.server"],
      "env": {
        "LOCAL_DB_MCP_CONFIG": "C:/Users/user/.local-db-mcp/config.yaml"
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
