# Game Info for Notion

## Description

This project syncs game (and in the future, movie/book/tea) information from external APIs (like RAWG) to a Notion
database. It is designed to be modular and extensible with plugins for different media types.

## Project Structure

- `core/` — Shared interfaces/utilities
- `plugins/` — All data source plugins (e.g. games_rawg)
- `notion_integration/` — Notion API logic
- `cli/` — CLI entry points
- `gui/` — GUI code (e.g. quick_add.py)
- `web/` — (future) Web app code
- `config/` — Configuration files
- `tests/` — Unit/integration tests
- `docs/` — Documentation

## Adding New Plugins

- Add your plugin as a new folder in `plugins/` and follow the structure of existing plugins.

