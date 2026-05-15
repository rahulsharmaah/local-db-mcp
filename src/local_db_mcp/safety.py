from __future__ import annotations

import re


READ_ONLY_SQL_RE = re.compile(r"^\s*(select|show|describe|desc|explain|with)\b", re.IGNORECASE)
BLOCKED_SQL_RE = re.compile(
    r"\b(insert|update|delete|drop|alter|truncate|create|grant|revoke|merge|call|execute|copy)\b",
    re.IGNORECASE,
)


def assert_read_only_sql(sql: str) -> None:
    if not READ_ONLY_SQL_RE.search(sql):
        raise ValueError("Only SELECT, SHOW, DESCRIBE, DESC, EXPLAIN, and WITH queries are allowed.")
    if BLOCKED_SQL_RE.search(sql):
        raise ValueError("Potentially mutating SQL keyword detected; refusing to run query.")


def clamp_limit(limit: int | None, default_limit: int, max_rows: int) -> int:
    requested = limit or default_limit
    return max(1, min(int(requested), int(max_rows)))
