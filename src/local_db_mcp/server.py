from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from .config import load_config, public_database_payload
from .discovery import probe_local_services
from .nosql_clients import (
    health_check_mongodb,
    health_check_redis,
    list_mongodb_collections,
    mongodb_find,
    redis_scan,
)
from .sql_clients import describe_sql_table, health_check_sql, list_sql_tables, query_sql

mcp = FastMCP(
    "Local DB MCP",
    instructions=(
        "Use this server for local database inspection. Prefer read-only tools. "
        "Never expose credentials. Ask before using any write-capable workflow."
    ),
)


def _config():
    return load_config()


@mcp.tool()
def health_check() -> dict[str, Any]:
    """Check configured database connections without exposing credentials."""
    config = _config()
    results = []
    for database in config.databases:
        try:
            if database.kind in {"postgres", "mysql", "mariadb", "sqlite"}:
                results.append(health_check_sql(database))
            elif database.kind == "mongodb":
                results.append(health_check_mongodb(database))
            elif database.kind == "redis":
                results.append(health_check_redis(database))
        except Exception as exc:
            results.append(
                {
                    "ok": False,
                    "name": database.name,
                    "kind": database.kind,
                    "error": str(exc),
                }
            )
    return {"configured": len(config.databases), "results": results}


@mcp.tool()
def list_connections() -> dict[str, Any]:
    """List configured database connections without showing DSNs or passwords."""
    config = _config()
    return {"connections": [public_database_payload(db) for db in config.databases]}


@mcp.tool()
def discover_local_services() -> dict[str, Any]:
    """Probe common localhost database ports to help users create config entries."""
    return {
        "services": probe_local_services(),
        "note": "Open ports are hints only. Add credentials and database names to config.yaml before querying.",
    }


@mcp.tool()
def list_tables(connection: str) -> dict[str, Any]:
    """List SQL tables or MongoDB collections for a configured connection."""
    database = _config().by_name(connection)
    if database.kind in {"postgres", "mysql", "mariadb", "sqlite"}:
        return {"items": list_sql_tables(database)}
    if database.kind == "mongodb":
        return {"items": list_mongodb_collections(database)}
    if database.kind == "redis":
        return redis_scan(database, pattern="*", limit=100, default_limit=100)
    raise ValueError(f"Unsupported database kind: {database.kind}")


@mcp.tool()
def describe_table(connection: str, table: str, schema: str | None = None) -> dict[str, Any]:
    """Describe a SQL table's columns, primary key, and indexes."""
    database = _config().by_name(connection)
    if database.kind not in {"postgres", "mysql", "mariadb", "sqlite"}:
        raise ValueError("describe_table is only available for SQL connections.")
    return describe_sql_table(database, table=table, schema=schema)


@mcp.tool()
def query_sql_readonly(connection: str, sql: str, limit: int | None = None) -> dict[str, Any]:
    """Run a read-only SQL query against PostgreSQL, MySQL/MariaDB, or SQLite."""
    config = _config()
    database = config.by_name(connection)
    if database.kind not in {"postgres", "mysql", "mariadb", "sqlite"}:
        raise ValueError("query_sql_readonly is only available for SQL connections.")
    return query_sql(database, sql, limit=limit, default_limit=config.default_limit)


@mcp.tool()
def mongodb_find_readonly(
    connection: str,
    collection: str,
    filter_doc: dict[str, Any] | None = None,
    projection: dict[str, Any] | None = None,
    limit: int | None = None,
) -> dict[str, Any]:
    """Run a read-only MongoDB find query."""
    config = _config()
    database = config.by_name(connection)
    if database.kind != "mongodb":
        raise ValueError("mongodb_find_readonly is only available for MongoDB connections.")
    return mongodb_find(
        database,
        collection=collection,
        filter_doc=filter_doc,
        projection=projection,
        limit=limit,
        default_limit=config.default_limit,
    )


@mcp.tool()
def redis_scan_keys(connection: str, pattern: str = "*", limit: int | None = None) -> dict[str, Any]:
    """Scan Redis keys by pattern without returning values."""
    config = _config()
    database = config.by_name(connection)
    if database.kind != "redis":
        raise ValueError("redis_scan_keys is only available for Redis connections.")
    return redis_scan(database, pattern=pattern, limit=limit, default_limit=config.default_limit)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
