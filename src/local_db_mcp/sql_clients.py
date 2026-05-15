from __future__ import annotations

from typing import Any

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.engine import Engine

from .config import DatabaseConfig
from .safety import assert_read_only_sql, clamp_limit


def _engine(database: DatabaseConfig) -> Engine:
    return create_engine(database.dsn, pool_pre_ping=True)


def health_check_sql(database: DatabaseConfig) -> dict[str, Any]:
    engine = _engine(database)
    try:
        with engine.connect() as conn:
            value = conn.execute(text("SELECT 1")).scalar()
        return {"ok": value == 1, "name": database.name, "kind": database.kind}
    finally:
        engine.dispose()


def list_sql_tables(database: DatabaseConfig) -> list[dict[str, Any]]:
    engine = _engine(database)
    try:
        inspector = inspect(engine)
        rows: list[dict[str, Any]] = []
        for schema in inspector.get_schema_names():
            if schema in {"information_schema", "pg_catalog", "mysql", "performance_schema", "sys"}:
                continue
            for table in inspector.get_table_names(schema=schema):
                rows.append({"schema": schema, "table": table})
        return rows
    finally:
        engine.dispose()


def describe_sql_table(database: DatabaseConfig, table: str, schema: str | None = None) -> dict[str, Any]:
    engine = _engine(database)
    try:
        inspector = inspect(engine)
        columns = inspector.get_columns(table, schema=schema)
        primary_key = inspector.get_pk_constraint(table, schema=schema)
        indexes = inspector.get_indexes(table, schema=schema)
        return {
            "schema": schema,
            "table": table,
            "columns": [
                {
                    "name": col["name"],
                    "type": str(col.get("type")),
                    "nullable": bool(col.get("nullable")),
                    "default": str(col.get("default")) if col.get("default") is not None else None,
                }
                for col in columns
            ],
            "primary_key": primary_key,
            "indexes": indexes,
        }
    finally:
        engine.dispose()


def query_sql(
    database: DatabaseConfig,
    sql: str,
    *,
    limit: int | None,
    default_limit: int,
) -> dict[str, Any]:
    assert_read_only_sql(sql)
    row_limit = clamp_limit(limit, default_limit, database.max_rows)
    engine = _engine(database)
    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql))
            rows = result.fetchmany(row_limit)
            columns = list(result.keys())
        return {
            "columns": columns,
            "rows": [dict(zip(columns, row, strict=False)) for row in rows],
            "row_count": len(rows),
            "limited_to": row_limit,
        }
    finally:
        engine.dispose()
