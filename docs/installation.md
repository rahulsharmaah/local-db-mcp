---
id: installation
title: Installation
---

# Installation

## Requirements

- Python 3.11 or newer
- A local database you can connect to
- An MCP-compatible client such as Codex, Claude Desktop, or Cursor

## Install From Source

```bash
git clone https://github.com/rahulsharmaah/local-db-mcp.git
cd local-db-mcp
python -m venv .venv
python -m pip install -e ".[dev]"
```

The editable install exposes this command:

```bash
local-db-mcp
```

## One-Command Bootstrap

Windows PowerShell:

```powershell
.\scripts\setup.ps1
```

macOS, Linux, or WSL:

```bash
./scripts/setup.sh
```

The setup scripts create a virtual environment, install the package, and create `~/.local-db-mcp/config.yaml` when it does not already exist.

## Verify Installation

```bash
local-db-mcp
```

The command starts an MCP stdio server and waits for a client. That is expected behavior.
