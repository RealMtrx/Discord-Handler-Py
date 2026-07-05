<div align="center">
  <h1>Discord Handler — Python</h1>
  <p><strong>A production-ready Discord bot framework built with discord.py v2 and MongoDB — slash commands, prefix commands, anti-crash, webhook logging, and a modular <code>src/</code> architecture.</strong></p>

  <p>
    <a href="https://github.com/RealMtrx/Discord-Handler-Py/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
    <a href="https://github.com/RealMtrx/Discord-Handler-Py/releases"><img src="https://img.shields.io/badge/version-0.9.0--beta-yellow" alt="Version 0.9.0 Beta"></a>
    <a href="https://github.com/RealMtrx/Discord-Handler-Py/stargazers"><img src="https://img.shields.io/github/stars/RealMtrx/Discord-Handler-Py" alt="Stars"></a>
    <a href="https://github.com/RealMtrx/Discord-Handler-Py/issues"><img src="https://img.shields.io/github/issues/RealMtrx/Discord-Handler-Py" alt="Issues"></a>
    <a href="https://github.com/RealMtrx/Discord-Handler-Py/network"><img src="https://img.shields.io/github/forks/RealMtrx/Discord-Handler-Py" alt="Forks"></a>
    <a href="https://github.com/RealMtrx/Discord-Handler/graphs/contributors"><img src="https://img.shields.io/badge/ecosystem-26%20repos-brightgreen" alt="26 Repos"></a>
    <a href="https://discord.gg/0hu2"><img src="https://img.shields.io/badge/discord-0hu2-5865F2" alt="Discord"></a>
  </p>

  <br>

  <p>
    <a href="#-features">Features</a> •
    <a href="#-quick-start">Quick Start</a> •
    <a href="#-project-structure">Structure</a> •
    <a href="#-api-reference">API</a> •
    <a href="#-database-edition">SQL Edition</a> •
    <a href="#-related-repositories">Ecosystem</a>
  </p>
</div>

---

## Overview

Discord Handler Python is a production-ready Discord bot framework built on **discord.py v2** with **MongoDB** storage. It provides a complete foundation for building Discord bots with slash commands, prefix commands, event handling, anti-crash protection, and webhook-based logging — all organized in a clean, scalable `src/` directory structure.

> **Version:** 0.9.0 (Stable Beta) — Part of the [Discord Handler](https://github.com/RealMtrx/Discord-Handler) ecosystem (26 repos across 13 languages).

## Features

- **Dual Command System** — Slash commands via `app_commands` and prefix commands via `commands.Bot`
- **MongoDB Integration** — Persistent data storage with Motor (async MongoDB driver)
- **Modular Architecture** — Clean separation: Commands, Events, Handlers, Core, Database, Models
- **Anti-Crash Protection** — Custom `on_error` event and async exception handler with webhook reporting
- **Async Runtime** — Fully async event-driven architecture with `asyncio`
- **Webhook Logging** — Dedicated webhooks for errors, slash/prefix commands, guild joins/leaves, and ready events via aiohttp
- **Cooldown System** — Per-command rate limiting using `CooldownManager` with `threading.Timer` cleanup
- **Emoji System** — Centralized emoji constants via `Emojis` class for consistent rendering
- **Environment Configuration** — Secure token and secrets management via `python-dotenv`
- **Startup Report** — Terminal banner showing loaded commands, events, and MongoDB connection status
- **Graceful Shutdown** — Clean connection teardown on KeyboardInterrupt

## Quick Start

```bash
# Clone the repository
git clone https://github.com/RealMtrx/Discord-Handler-Py.git
cd Discord-Handler-Py

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your bot token, client ID, and MongoDB URI

# Run the bot
python src/main.py
```

### Prerequisites

- **Python 3.10+** — Runtime environment
- **MongoDB** — Local or Atlas instance
- **Discord Application** — Bot token and client ID from the [Discord Developer Portal](https://discord.com/developers/applications)

### Environment Variables

```env
TOKEN=your_bot_token
CLIENT_ID=your_client_id
BOT_NAME=Discord Handler
OWNER_IDS=owner_id_1,owner_id_2
PREFIX=$
MONGODB_URI=mongodb://localhost:27017/discord_bot
ERROR_WEBHOOK=your_webhook_url
SLASH_WEBHOOK=your_webhook_url
PREFIX_WEBHOOK=your_webhook_url
JOIN_WEBHOOK=your_webhook_url
LEAVE_WEBHOOK=your_webhook_url
READY_WEBHOOK=your_webhook_url
```

## Project Structure

```
Discord-Handler-Py/
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template
├── LICENSE
├── src/
│   ├── __init__.py
│   ├── main.py                    # Entry point — initializes everything
│   ├── config.py                  # Config singleton loaded from env vars
│   ├── bot.py                     # Bot class (commands.Bot subclass)
│   ├── Core/                      # Shared utilities
│   │   ├── __init__.py
│   │   ├── command_utils.py       # ErrorReport, format_error, log_command_usage
│   │   ├── cooldown.py            # CooldownManager with Timer cleanup
│   │   ├── emojis.py              # Unicode emoji constants
│   │   ├── error_webhook.py       # Error reporting webhook
│   │   ├── join_guild_webhook.py  # Guild join notification
│   │   ├── leave_guild_webhook.py # Guild leave notification
│   │   ├── prefix_command_webhook.py
│   │   ├── ready_webhook.py       # Bot ready event webhook
│   │   ├── slash_command_webhook.py
│   │   └── webhooks.py            # WebhookEmbed, send_webhook, shared helpers
│   ├── Database/
│   │   ├── __init__.py
│   │   └── mongo.py               # MongoManager — async connection, user CRUD
│   ├── Events/                    # Discord event handlers
│   │   ├── __init__.py
│   │   ├── error.py               # on_error handler
│   │   ├── guild_create.py        # Guild join webhook
│   │   ├── guild_delete.py        # Guild leave webhook
│   │   ├── interaction_create.py  # Slash command dispatch + logging
│   │   ├── message_create.py      # Prefix command dispatch + cooldown
│   │   └── ready.py               # Bot ready — log startup
│   ├── Handlers/                  # Loaders and registrars
│   │   ├── __init__.py
│   │   ├── anticrash.py           # Exception handler + on_error event
│   │   ├── commands.py            # load_slash_commands
│   │   ├── events.py              # load_events
│   │   ├── logger.py              # print_startup_banner
│   │   ├── models.py              # StartupData dataclass
│   │   └── prefix.py              # load_prefix_commands
│   ├── Models/
│   │   ├── __init__.py
│   │   └── user.py                # UserModel with get / create_or_update
│   └── Commands/
│       ├── __init__.py
│       ├── Slash/
│       │   ├── __init__.py
│       │   └── public/
│       │       ├── __init__.py
│       │       └── ping.py        # Shows WebSocket and API latency
│       └── Prefix/
│           ├── __init__.py
│           └── public/
│               ├── __init__.py
│               └── ping.py        # Shows message and API latency
```

## API Reference

### Core Types

| Type | Location | Description |
| ---- | -------- | ----------- |
| `Config` | `config.py` | Application configuration singleton loaded from env vars |
| `Bot` | `bot.py` | `commands.Bot` subclass with config, command maps, and error handler |
| `CooldownManager` | `core/cooldown.py` | Per-command cooldown tracker with `threading.Timer` cleanup |
| `WebhookEmbed` | `core/webhooks.py` | Embed dataclass with `to_dict()` for webhook payloads |
| `MongoManager` | `database/mongo.py` | Async MongoDB connection manager with user CRUD |
| `UserModel` | `models/user.py` | Static methods wrapping `MongoManager` user operations |

### Core Functions

| Function | Location | Description |
| -------- | -------- | ----------- |
| `config = Config()` | `config.py` | Global config instance |
| `cd.check(user_id, command, ms)` | `core/cooldown.py` | Returns `(on_cooldown, remaining)` |
| `send_webhook(url, embed)` | `core/webhooks.py` | Sends an embed to a Discord webhook via aiohttp |
| `format_error(error, command_name)` | `core/command_utils.py` | Returns an `ErrorReport` object |
| `log_command_usage(user_id, user_name, cmd, guild)` | `core/command_utils.py` | Prints command usage to stdout |

### Events

| Event | File | Description |
| ----- | ---- | ----------- |
| `on_ready` | `events/ready.py` | Logs bot login info |
| `on_interaction` | `events/interaction_create.py` | Routes slash commands |
| `on_message` | `events/message_create.py` | Routes prefix commands with cooldown |
| `on_guild_join` | `events/guild_create.py` | Sends guild join webhook |
| `on_guild_remove` | `events/guild_delete.py` | Sends guild leave webhook |
| `on_error` | `events/error.py` | Catches and logs event errors |

### Database

| Function | Location | Description |
| -------- | -------- | ----------- |
| `await mongo.connect()` | `database/mongo.py` | Connects with 10s timeout, configures DNS |
| `await mongo.get_user(user_id)` | `database/mongo.py` | Fetches user by `_id` |
| `await mongo.create_user(user_id, data)` | `database/mongo.py` | Upserts user document |
| `await mongo.close()` | `database/mongo.py` | Closes the MongoDB connection |

### Handlers

| Function | Location | Description |
| -------- | -------- | ----------- |
| `setup_anticrash(bot)` | `handlers/anticrash.py` | Attaches exception handler and `on_error` event |
| `load_slash_commands(bot)` | `handlers/commands.py` | Scans and registers slash commands |
| `load_prefix_commands(bot)` | `handlers/prefix.py` | Scans and registers prefix commands |
| `load_events(bot)` | `handlers/events.py` | Scans and imports event modules |

## Adding Commands

### Slash Command

Create a new file in `src/Commands/Slash/[category]/[name].py`:

```python
import discord
from discord import app_commands
from src.handlers.models import SlashCommand

async def hello_callback(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! 👋")

cmd_data = app_commands.Command(
    name="hello",
    description="Say hello!",
    callback=hello_callback,
)

command = SlashCommand(data=cmd_data, category="public")
```

### Prefix Command

Create a new file in `src/Commands/Prefix/[category]/[name].py`:

```python
import discord
from src.handlers.models import PrefixCommand

async def hello_handler(message: discord.Message, args: list[str]):
    await message.reply("Hello! 👋")

command = PrefixCommand(
    name="hello",
    description="Say hello!",
    category="public",
    aliases=["hi"],
    handler=hello_handler,
)
```

## Database Edition

This is the **MongoDB edition**. A **SQL edition** using Sequelize ORM is also available:

| Feature | MongoDB Edition | SQL Edition |
| ------- | --------------- | ----------- |
| Repository | [Discord-Handler-Py](https://github.com/RealMtrx/Discord-Handler-Py) | [Discord-Handler-Py-Sequelize](https://github.com/RealMtrx/Discord-Handler-Py-Sequelize) |
| Database | MongoDB | SQLite, PostgreSQL, MySQL, MSSQL |
| Driver | Motor (async) + PyMongo | SQLAlchemy / asyncpg |
| Dialects | MongoDB only | Multi-dialect via config |

## Related Repositories

Discord Handler Python is part of a **26-repo ecosystem**. Here are the other repositories:

### Core Framework (MongoDB)

| Language | Repository |
| -------- | ---------- |
| JavaScript | [Discord-Handler-Js](https://github.com/RealMtrx/Discord-Handler-Js) |
| TypeScript | [Discord-Handler-Ts](https://github.com/RealMtrx/Discord-Handler-Ts) |
| Go | [Discord-Handler-Go](https://github.com/RealMtrx/Discord-Handler-Go) |
| Rust | [Discord-Handler-Rs](https://github.com/RealMtrx/Discord-Handler-Rs) |
| C# | [Discord-Handler-Cs](https://github.com/RealMtrx/Discord-Handler-Cs) |
| Java | [Discord-Handler-Java](https://github.com/RealMtrx/Discord-Handler-Java) |
| Kotlin | [Discord-Handler-Kt](https://github.com/RealMtrx/Discord-Handler-Kt) |
| C++ | [Discord-Handler-Cpp](https://github.com/RealMtrx/Discord-Handler-Cpp) |
| Dart | [Discord-Handler-Dart](https://github.com/RealMtrx/Discord-Handler-Dart) |
| Ruby | [Discord-Handler-Rb](https://github.com/RealMtrx/Discord-Handler-Rb) |
| Lua | [Discord-Handler-Lua](https://github.com/RealMtrx/Discord-Handler-Lua) |
| PHP | [Discord-Handler-Php](https://github.com/RealMtrx/Discord-Handler-Php) |

### Database Editions (SQL)

| Language | Repository |
| -------- | ---------- |
| JavaScript | [Discord-Handler-Js-Sequelize](https://github.com/RealMtrx/Discord-Handler-Js-Sequelize) |
| TypeScript | [Discord-Handler-Ts-Sequelize](https://github.com/RealMtrx/Discord-Handler-Ts-Sequelize) |
| Go | [Discord-Handler-Go-Sequelize](https://github.com/RealMtrx/Discord-Handler-Go-Sequelize) |
| Rust | [Discord-Handler-Rs-Sequelize](https://github.com/RealMtrx/Discord-Handler-Rs-Sequelize) |
| Python | [Discord-Handler-Py-Sequelize](https://github.com/RealMtrx/Discord-Handler-Py-Sequelize) |
| C# | [Discord-Handler-Cs-Sequelize](https://github.com/RealMtrx/Discord-Handler-Cs-Sequelize) |
| Java | [Discord-Handler-Java-Sequelize](https://github.com/RealMtrx/Discord-Handler-Java-Sequelize) |
| Kotlin | [Discord-Handler-Kt-Sequelize](https://github.com/RealMtrx/Discord-Handler-Kt-Sequelize) |
| C++ | [Discord-Handler-Cpp-Sequelize](https://github.com/RealMtrx/Discord-Handler-Cpp-Sequelize) |
| Dart | [Discord-Handler-Dart-Sequelize](https://github.com/RealMtrx/Discord-Handler-Dart-Sequelize) |
| Ruby | [Discord-Handler-Rb-Sequelize](https://github.com/RealMtrx/Discord-Handler-Rb-Sequelize) |
| Lua | [Discord-Handler-Lua-Sequelize](https://github.com/RealMtrx/Discord-Handler-Lua-Sequelize) |
| PHP | [Discord-Handler-Php-Sequelize](https://github.com/RealMtrx/Discord-Handler-Php-Sequelize) |

### Hub

| Repository | Description |
| ---------- | ----------- |
| [Discord-Handler](https://github.com/RealMtrx/Discord-Handler) | Central hub — documentation, examples, changelog, roadmap |

## License

MIT License — Copyright © 2026 Mtrx

---

<div align="center">
  <sub>Built by <strong>Mtrx</strong> — Discord: <strong>0hu2</strong></sub>
  <br>
  <sub><a href="https://github.com/RealMtrx/Discord-Handler">Discord Handler Ecosystem</a></sub>
</div>
