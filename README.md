# Local DB MCP

Local DB MCP is a Model Context Protocol server for safe, read-only inspection of developer-owned local databases from Codex, Claude Desktop, Cursor, and other MCP clients.

It is designed for teams that need one consistent way to inspect PostgreSQL, MySQL/MariaDB, SQLite, MongoDB, and Redis during local development without copying credentials into prompts.

## Features

- PostgreSQL, MySQL/MariaDB, SQLite, MongoDB, and Redis support
- Read-only SQL enforcement by default
- Config-driven connection profiles
- No credential disclosure in tool responses
- Result limits per server and per connection
- MCP client guides for Codex, Claude Desktop, and Cursor
- Docusaurus documentation site ready for GitHub Pages

## Quick Start

Install the server from GitHub:

```bash
python -m pip install "git+https://github.com/rahulsharmaah/local-db-mcp.git"
```

Create your user config:

```bash
mkdir -p ~/.local-db-mcp
cp examples/config.example.yaml ~/.local-db-mcp/config.yaml
```

Edit `~/.local-db-mcp/config.yaml` with your database connection strings. Then configure your MCP client to run:

```text
local-db-mcp
```

This repo includes install-ready client assets:

- `.mcp.json` for standard MCP clients
- `.cursor/mcp.json` for Cursor
- `.codex-plugin/plugin.json` for Codex local plugin installs
- `docs/codex-cloud.md` for Codex Cloud workspaces

If you prefer the one-command bootstrap scripts, run:

```bash
./scripts/setup.sh
```

or on Windows PowerShell:

```powershell
.\scripts\setup.ps1
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
LOCAL_DB_MCP_CONFIG=/secure/config/location.yaml
```

Example:

```yaml
default_limit: 100
allow_write_tools: false

databases:
  - name: app_postgres
    kind: postgres
    dsn: postgresql+psycopg://app_user:change-me@localhost:5432/app_database
    read_only: true
    max_rows: 200

  - name: app_mysql
    kind: mysql
    dsn: mysql+pymysql://app_user:change-me@localhost:3306/app_database
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
- [Codex Cloud](docs/codex-cloud.md)
- [Claude Desktop](docs/claude-desktop.md)
- [Cursor](docs/cursor.md)
- [Client Templates](docs/client-templates.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

## Development

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
python -m py_compile src/local_db_mcp/server.py
local-db-mcp
```

The server runs over MCP stdio, so it waits for an MCP client after startup.
