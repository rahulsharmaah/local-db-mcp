# Local DB MCP

Use this skill when a user wants to inspect configured PostgreSQL, MySQL, MariaDB, SQLite, MongoDB, or Redis databases through the Local DB MCP server.

## Workflow

1. Start with `health_check` to confirm configured connections are reachable.
2. Use `list_connections` to identify available database profiles without exposing DSNs.
3. Use `list_tables` or `describe_table` before writing ad hoc SQL.
4. Prefer narrow, read-only queries through `query_sql_readonly`.
5. For MongoDB, use `mongodb_find_readonly` with a small limit and projection when possible.
6. For Redis, use `redis_scan_keys`; do not request values unless a future explicit read tool exists.

## Safety

- Treat credentials, DSNs, and config paths as private.
- Do not ask the user to paste secrets into chat.
- Keep query limits small unless the user explicitly asks for more.
- Do not attempt writes unless the server and user have both explicitly allowed write tools.
