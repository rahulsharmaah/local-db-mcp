# Query Examples

List connections:

```json
{
  "tool": "list_connections"
}
```

Probe common local DB ports:

```json
{
  "tool": "discover_local_services"
}
```

PostgreSQL:

```json
{
  "tool": "query_sql_readonly",
  "arguments": {
    "connection": "app_postgres",
    "sql": "SELECT id, status, created_at FROM accounts ORDER BY id",
    "limit": 50
  }
}
```

MySQL / MariaDB:

```json
{
  "tool": "query_sql_readonly",
  "arguments": {
    "connection": "app_mysql",
    "sql": "SELECT id, name, status FROM customers LIMIT 20"
  }
}
```

MongoDB:

```json
{
  "tool": "mongodb_find_readonly",
  "arguments": {
    "connection": "app_mongo",
    "collection": "users",
    "filter_doc": {"status": "active"},
    "projection": {"email": 1, "status": 1},
    "limit": 25
  }
}
```

Redis:

```json
{
  "tool": "redis_scan_keys",
  "arguments": {
    "connection": "local_redis",
    "pattern": "session:*",
    "limit": 50
  }
}
```
