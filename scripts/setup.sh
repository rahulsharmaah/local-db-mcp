#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG_DIR="$HOME/.local-db-mcp"
CONFIG_PATH="$CONFIG_DIR/config.yaml"
VENV_PATH="$PROJECT_ROOT/.venv"
PYTHON_PATH="$VENV_PATH/bin/python"

echo "Setting up Local DB MCP in $PROJECT_ROOT"

if [ ! -d "$VENV_PATH" ]; then
  python3 -m venv "$VENV_PATH"
fi

"$PYTHON_PATH" -m pip install --upgrade pip
"$PYTHON_PATH" -m pip install -e "$PROJECT_ROOT"

mkdir -p "$CONFIG_DIR"
if [ ! -f "$CONFIG_PATH" ]; then
  cp "$PROJECT_ROOT/examples/config.example.yaml" "$CONFIG_PATH"
  echo "Created config: $CONFIG_PATH"
else
  echo "Config already exists: $CONFIG_PATH"
fi

cat <<EOF

Next steps:
1. Edit $CONFIG_PATH with your local database DSNs.
2. Add this MCP server to Codex, Claude Desktop, or Cursor:
   Command: $PYTHON_PATH
   Args: -m local_db_mcp.server

Smoke test:
   "$PYTHON_PATH" -m local_db_mcp.server
EOF
