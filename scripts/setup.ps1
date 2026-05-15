$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$ConfigDir = Join-Path $HOME ".local-db-mcp"
$ConfigPath = Join-Path $ConfigDir "config.yaml"
$VenvPath = Join-Path $ProjectRoot ".venv"
$PythonPath = Join-Path $VenvPath "Scripts\python.exe"

Write-Host "Setting up Local DB MCP in $ProjectRoot"

if (-not (Test-Path $VenvPath)) {
    python -m venv $VenvPath
}

& $PythonPath -m pip install --upgrade pip
& $PythonPath -m pip install -e $ProjectRoot

New-Item -ItemType Directory -Force -Path $ConfigDir | Out-Null
if (-not (Test-Path $ConfigPath)) {
    Copy-Item (Join-Path $ProjectRoot "examples\config.example.yaml") $ConfigPath
    Write-Host "Created config: $ConfigPath"
} else {
    Write-Host "Config already exists: $ConfigPath"
}

Write-Host ""
Write-Host "Next steps:"
Write-Host "1. Edit $ConfigPath with your local database DSNs."
Write-Host "2. Add this MCP server to Codex, Claude Desktop, or Cursor:"
Write-Host "   Command: $PythonPath"
Write-Host "   Args: -m local_db_mcp.server"
Write-Host ""
Write-Host "Smoke test:"
Write-Host "   & `"$PythonPath`" -m local_db_mcp.server"
