# Cursor Setup

Run setup first:

```powershell
cd D:\local-db-mcp
.\scripts\setup.ps1
notepad $HOME\.local-db-mcp\config.yaml
```

This repo includes a project-local Cursor config at:

```text
.cursor/mcp.json
```

If your project uses a different path, copy this block into Cursor's MCP config:

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

Restart Cursor after changing MCP configuration.
