from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, Field, ValidationError


DEFAULT_CONFIG_PATH = Path.home() / ".local-db-mcp" / "config.yaml"

DatabaseKind = Literal["postgres", "mysql", "mariadb", "sqlite", "mongodb", "redis"]


class DatabaseConfig(BaseModel):
    name: str = Field(pattern=r"^[A-Za-z0-9_.-]+$")
    kind: DatabaseKind
    dsn: str
    description: str = ""
    read_only: bool = True
    max_rows: int = Field(default=100, ge=1, le=5000)
    connect_timeout_seconds: int = Field(default=10, ge=1, le=120)
    tags: list[str] = Field(default_factory=list)


class ServerConfig(BaseModel):
    default_limit: int = Field(default=100, ge=1, le=5000)
    allow_write_tools: bool = False
    databases: list[DatabaseConfig] = Field(default_factory=list)

    def by_name(self, name: str) -> DatabaseConfig:
        for database in self.databases:
            if database.name == name:
                return database
        available = ", ".join(db.name for db in self.databases) or "none configured"
        raise ValueError(f"Unknown database connection '{name}'. Available: {available}")


def config_path() -> Path:
    override = os.environ.get("LOCAL_DB_MCP_CONFIG")
    if override:
        return Path(override).expanduser()
    return DEFAULT_CONFIG_PATH


def load_config(path: Path | None = None) -> ServerConfig:
    path = path or config_path()
    if not path.exists():
        return ServerConfig()

    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    try:
        return ServerConfig.model_validate(raw)
    except ValidationError as exc:
        raise RuntimeError(f"Invalid local-db-mcp config at {path}: {exc}") from exc


def public_database_payload(database: DatabaseConfig) -> dict[str, Any]:
    return {
        "name": database.name,
        "kind": database.kind,
        "description": database.description,
        "read_only": database.read_only,
        "max_rows": database.max_rows,
        "tags": database.tags,
    }
