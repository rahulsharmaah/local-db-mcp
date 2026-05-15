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
    "connection": "bimble_admin",
    "sql": "SELECT clinic_id, clinic_code, slug, status FROM clinics ORDER BY clinic_id",
    "limit": 50
  }
}
```

MySQL / MariaDB:

```json
{
  "tool": "query_sql_readonly",
  "arguments": {
    "connection": "oscar",
    "sql": "SELECT clinic_no, clinic_name FROM clinic LIMIT 20"
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
