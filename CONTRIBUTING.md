# Contributing

Thanks for helping improve Local DB MCP. The project is intentionally small, safe by default, and easy to audit.

## Development Setup

1. Fork and clone the repository.
2. Create a virtual environment.
3. Install the project in editable mode:

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
```

4. Create a local config file:

```bash
mkdir -p ~/.local-db-mcp
cp examples/config.example.yaml ~/.local-db-mcp/config.yaml
```

5. Replace the example DSNs with your own local database credentials.

Never commit real credentials, database dumps, private schema exports, or generated local config files.

## Project Structure

```text
src/local_db_mcp/      MCP server and database clients
examples/             Safe example configuration
docs/                 Documentation source for Docusaurus
scripts/              Setup helpers
.github/workflows/    CI and GitHub Pages automation
```

## Safety Principles

- Keep read-only behavior as the default.
- Do not expose DSNs, passwords, tokens, or secret material in tool outputs.
- Do not add write tools without explicit configuration gates and documentation.
- Keep result limits in place for all query tools.
- Prefer clear, boring code over clever abstractions.

## Code Style

- Target Python 3.11+.
- Keep functions small and testable.
- Add type hints for public helpers and MCP tool functions.
- Use explicit error messages that help users fix configuration problems.

Run checks before opening a pull request:

```bash
python -m py_compile src/local_db_mcp/*.py
python -m pytest
```

## Pull Requests

Please include:

- What changed
- Why it changed
- Any database engines affected
- Manual test notes
- Screenshots only if documentation UI changed

## Documentation

Documentation is built with Docusaurus. Update docs whenever you add tools, config keys, or safety behavior.

```bash
npm install
npm run build
```
