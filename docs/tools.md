---
id: tools
title: MCP Tools
---

# MCP Tools

## `health_check`

Checks every configured connection without exposing credentials.

## `list_connections`

Returns connection names, kinds, descriptions, tags, and read-only settings. It does not return DSNs.

## `discover_local_services`

Probes common local database ports and returns hints such as whether PostgreSQL, MySQL, MongoDB, Redis, SQL Server, or Elasticsearch ports appear open.

This does not authenticate and does not replace configuration.

## `list_tables`

Lists SQL tables, MongoDB collections, or Redis keys depending on the connection type.

## `describe_table`

Returns SQL table columns, primary keys, and indexes.

## `query_sql_readonly`

Runs read-only SQL against configured SQL databases.

Allowed starting keywords:

- `SELECT`
- `SHOW`
- `DESCRIBE`
- `DESC`
- `EXPLAIN`
- `WITH`

Mutating keywords such as `INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`, `TRUNCATE`, `CREATE`, `GRANT`, and `REVOKE` are blocked.

## `mongodb_find_readonly`

Runs MongoDB `find` with optional filter and projection.

## `redis_scan_keys`

Scans Redis keys by pattern. It intentionally returns keys only, not values.
