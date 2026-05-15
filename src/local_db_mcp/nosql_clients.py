from __future__ import annotations

from typing import Any

from pymongo import MongoClient
from redis import Redis

from .config import DatabaseConfig
from .safety import clamp_limit


def health_check_mongodb(database: DatabaseConfig) -> dict[str, Any]:
    client: MongoClient = MongoClient(database.dsn, serverSelectionTimeoutMS=database.connect_timeout_seconds * 1000)
    try:
        client.admin.command("ping")
        return {"ok": True, "name": database.name, "kind": database.kind}
    finally:
        client.close()


def list_mongodb_collections(database: DatabaseConfig) -> list[dict[str, Any]]:
    client: MongoClient = MongoClient(database.dsn, serverSelectionTimeoutMS=database.connect_timeout_seconds * 1000)
    try:
        db = client.get_default_database()
        return [{"database": db.name, "collection": name} for name in db.list_collection_names()]
    finally:
        client.close()


def mongodb_find(
    database: DatabaseConfig,
    collection: str,
    filter_doc: dict[str, Any] | None,
    projection: dict[str, Any] | None,
    *,
    limit: int | None,
    default_limit: int,
) -> dict[str, Any]:
    row_limit = clamp_limit(limit, default_limit, database.max_rows)
    client: MongoClient = MongoClient(database.dsn, serverSelectionTimeoutMS=database.connect_timeout_seconds * 1000)
    try:
        db = client.get_default_database()
        cursor = db[collection].find(filter_doc or {}, projection).limit(row_limit)
        rows = []
        for item in cursor:
            item["_id"] = str(item.get("_id"))
            rows.append(item)
        return {"rows": rows, "row_count": len(rows), "limited_to": row_limit}
    finally:
        client.close()


def health_check_redis(database: DatabaseConfig) -> dict[str, Any]:
    client = Redis.from_url(database.dsn, socket_connect_timeout=database.connect_timeout_seconds)
    try:
        return {"ok": bool(client.ping()), "name": database.name, "kind": database.kind}
    finally:
        client.close()


def redis_scan(database: DatabaseConfig, pattern: str = "*", limit: int | None = None, default_limit: int = 100) -> dict[str, Any]:
    row_limit = clamp_limit(limit, default_limit, database.max_rows)
    client = Redis.from_url(database.dsn, socket_connect_timeout=database.connect_timeout_seconds, decode_responses=True)
    try:
        keys: list[str] = []
        cursor = 0
        while len(keys) < row_limit:
            cursor, batch = client.scan(cursor=cursor, match=pattern, count=min(100, row_limit))
            keys.extend(batch)
            if cursor == 0:
                break
        return {"keys": keys[:row_limit], "row_count": min(len(keys), row_limit), "limited_to": row_limit}
    finally:
        client.close()
