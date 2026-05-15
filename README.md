# Local DB MCP

One local MCP server for inspecting configured databases from Codex, Claude Desktop, and Cursor.

It supports:

- PostgreSQL
- MySQL / MariaDB
- SQLite
- MongoDB
- Redis key scans

The server is **read-only by default**. SQL tools only allow `SELECT`, `SHOW`, `DESCRIBE`, `DESC`, `EXPLAIN`, and `WITH` queries.

## Quick Start

Windows PowerShell:

```powershell
cd D:\local-db-mcp
.\scripts\setup.ps1
notepad $HOME\.local-db-mcp\config.yaml
```

macOS / Linux / WSL:

```bash
cd /path/to/local-db-mcp
./scripts/setup.sh
${EDITOR:-nano} ~/.local-db-mcp/config.yaml
```

After editing the config once, point your MCP client at:

```text
Command: D:\local-db-mcp\.venv\Scripts\python.exe
Args:    -m local_db_mcp.server
```

On macOS/Linux:

```text
Command: /path/to/local-db-mcp/.venv/bin/python
Args:    -m local_db_mcp.server
```

## Tools

| Tool | Purpose |
|---|---|
| `health_check` | Test all configured connections without exposing credentials |
| `list_connections` | Show configured connection names and types |
| `discover_local_services` | Probe common local DB ports as setup hints |
| `list_tables` | List SQL tables, MongoDB collections, or Redis keys |
| `describe_table` | Describe SQL table columns, keys, and indexes |
| `query_sql_readonly` | Run read-only SQL |
| `mongodb_find_readonly` | Run read-only MongoDB `find` |
| `redis_scan_keys` | Scan Redis keys without returning values |

## Configuration

The default config path is:

```text
~/.local-db-mcp/config.yaml
```

Override it with:

```text
LOCAL_DB_MCP_CONFIG=/path/to/config.yaml
```

Example:

```yaml
default_limit: 100
allow_write_tools: false

databases:
  - name: bimble_admin
    kind: postgres
    dsn: postgresql+psycopg://bimble_platform:password@localhost:5432/bimble_admin
    read_only: true
    max_rows: 200

  - name: oscar
    kind: mysql
    dsn: mysql+pymysql://user:password@localhost:3306/oscar_15
    read_only: true
    max_rows: 200

  - name: app_mongo
    kind: mongodb
    dsn: mongodb://localhost:27017/app_database
    read_only: true
```

## Safety Model

- DSNs are never returned by `list_connections`.
- SQL writes are blocked by default.
- Results are limited by `default_limit` and each database's `max_rows`.
- Redis support scans keys only; it does not read values.
- MongoDB support exposes `find`, not updates/deletes.

## Client Setup

See:

- [Codex](docs/codex.md)
- [Claude Desktop](docs/claude-desktop.md)
- [Cursor](docs/cursor.md)

## Development

```powershell
cd D:\local-db-mcp
.\.venv\Scripts\python.exe -m py_compile src\local_db_mcp\server.py
.\.venv\Scripts\python.exe -m local_db_mcp.server
```

The server runs over MCP stdio, so it waits for an MCP client after startup.
