---
id: configuration
title: Configuration
---

# Configuration

Local DB MCP reads configuration from:

```text
~/.local-db-mcp/config.yaml
```

You can override this with:

```text
LOCAL_DB_MCP_CONFIG=/secure/config/location.yaml
```

## Example

```yaml
default_limit: 100
allow_write_tools: false

databases:
  - name: app_postgres
    kind: postgres
    description: Application PostgreSQL database
    dsn: postgresql+psycopg://app_user:change-me@localhost:5432/app_database
    read_only: true
    max_rows: 200
    tags: ["local", "sql"]

  - name: app_mysql
    kind: mysql
    description: Application MySQL database
    dsn: mysql+pymysql://app_user:change-me@localhost:3306/app_database
    read_only: true
    max_rows: 200
    tags: ["local", "sql"]

  - name: app_mongodb
    kind: mongodb
    description: Application MongoDB database
    dsn: mongodb://localhost:27017/app_database
    read_only: true
    max_rows: 100
```

## Supported `kind` Values

| Kind | Driver |
|---|---|
| `postgres` | SQLAlchemy + psycopg |
| `mysql` | SQLAlchemy + PyMySQL |
| `mariadb` | SQLAlchemy + PyMySQL |
| `sqlite` | SQLAlchemy SQLite |
| `mongodb` | PyMongo |
| `redis` | redis-py |

## Recommended Credentials

Use least-privilege credentials. Prefer database users that are read-only at the database permission level, even though Local DB MCP also blocks mutating SQL in application code.

Never commit your real config file.
