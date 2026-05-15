# Claude Desktop Setup

Install Local DB MCP:

```bash
pip install .
```

Create `~/.local-db-mcp/config.yaml` from `examples/config.example.yaml`, then add this to Claude Desktop's MCP config file.

Typical config file locations:

```text
macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
Windows: %APPDATA%\Claude\claude_desktop_config.json
```

Config:

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

Restart Claude Desktop after editing the config.
