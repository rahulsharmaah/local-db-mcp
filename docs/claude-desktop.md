# Claude Desktop Setup

Run setup first:

```powershell
cd D:\local-db-mcp
.\scripts\setup.ps1
notepad $HOME\.local-db-mcp\config.yaml
```

Add this to Claude Desktop's MCP config file.

Windows path:

```text
%APPDATA%\Claude\claude_desktop_config.json
```

Config:

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

Restart Claude Desktop after editing the config.
