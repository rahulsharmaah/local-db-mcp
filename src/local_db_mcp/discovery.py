from __future__ import annotations

import socket
from typing import Any


COMMON_SERVICES = [
    ("postgres", "127.0.0.1", 5432),
    ("mysql_mariadb", "127.0.0.1", 3306),
    ("mongodb", "127.0.0.1", 27017),
    ("redis", "127.0.0.1", 6379),
    ("mssql", "127.0.0.1", 1433),
    ("elasticsearch", "127.0.0.1", 9200),
]


def probe_local_services(timeout_seconds: float = 0.5) -> list[dict[str, Any]]:
    results = []
    for service, host, port in COMMON_SERVICES:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout_seconds)
        try:
            ok = sock.connect_ex((host, port)) == 0
        finally:
            sock.close()
        results.append({"service": service, "host": host, "port": port, "open": ok})
    return results
