# Discord Handler (Python)

A modern, feature-rich Discord bot handler built with **discord.py v2** and **Python**, featuring both slash commands and prefix commands with a robust modular architecture designed for scalability and maintainability.

## Features

- **Dual Command System**: Support for both slash commands (`/ping`) and prefix commands (`$ping`)
- **Modular Architecture**: Clean separation of concerns with dedicated handlers
- **Anti-Crash System**: Comprehensive error handling and monitoring
- **Event-Driven**: Fully event-driven architecture
- **Async/Await**: Full asynchronous design with `asyncio`
- **Webhook Logging**: Real-time logging for errors, commands, guild events, and bot status
- **MongoDB Integration**: Persistent data storage with `motor` (async MongoDB driver)
- **Cooldown System**: Per-command cooldown management
- **Environment Configuration**: Secure configuration management with `python-dotenv`
- **Custom DNS**: Google/Cloudflare DNS for stable MongoDB connections

## Project Structure

```
Discord-Handler-Py/
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment configuration template
├── .gitignore
├── src/                          # Python source code
│   ├── main.py                   # Main bot entry point
│   ├── config.py                 # Bot configuration from .env
│   ├── bot.py                    # Custom Bot class (extends commands.Bot)
│   ├── Core/                     # Core utilities and webhooks
│   │   ├── command_utils.py      # Error formatting, logging utilities
│   │   ├── emojis.py             # Centralized emoji definitions
│   │   ├── cooldown.py           # Per-command cooldown management
│   │   ├── webhooks.py           # Webhook base types and sender
│   │   ├── error_webhook.py      # Error reporting via webhook
│   │   ├── join_guild_webhook.py # Webhook when the bot joins a guild
│   │   ├── leave_guild_webhook.py
│   │   ├── prefix_command_webhook.py
│   │   ├── ready_webhook.py
│   │   └── slash_command_webhook.py
│   ├── Database/
│   │   └── mongo.py              # MongoDB connection with motor
│   ├── Events/                   # Discord event listeners
│   │   ├── error.py
│   │   ├── guild_create.py
│   │   ├── guild_delete.py
│   │   ├── interaction_create.py
│   │   ├── message_create.py
│   │   └── ready.py
│   ├── Handlers/                 # Loaders and registrars
│   │   ├── anticrash.py          # Global exception handler
│   │   ├── commands.py           # Slash command loader
│   │   ├── events.py             # Event listener loader
│   │   ├── logger.py             # Startup banner logger
│   │   ├── models.py             # Shared type definitions
│   │   └── prefix.py             # Prefix command loader
│   ├── Models/
│   │   └── user.py               # User data model
│   └── Commands/
│       ├── Prefix/Public/ping.py
│       └── Slash/Public/ping.py
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/RealMtrx/Discord-Handler-Py.git
   cd Discord-Handler-Py
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**

   Copy `.env.example` to `.env` and fill in your values:

   ```env
   TOKEN=your_bot_token
   CLIENT_ID=your_client_id
   BOT_NAME=Discord Handler
   PREFIX=$
   OWNER_IDS=owner_id_1,owner_id_2
   MONGODB_URI=your_mongo_uri
   ERROR_WEBHOOK=#
   SLASH_WEBHOOK=#
   PREFIX_WEBHOOK=#
   JOIN_WEBHOOK=#
   LEAVE_WEBHOOK=#
   READY_WEBHOOK=#
   ```

4. **Run the bot**

   ```bash
   python src/main.py
   ```

## Requirements

- **Python**: 3.10+
- **discord.py**: ^2.4.0 — Discord API wrapper
- **motor**: ^3.0 — Async MongoDB driver
- **pymongo**: ^4.8 — MongoDB driver
- **python-dotenv**: ^1.0 — Environment variable management
- **aiohttp**: ^3.9 — Async HTTP client for webhooks
- **dnspython**: ^2.6 — DNS resolver for MongoDB SRV

## Command Development

### Creating Slash Commands

Create a new file in `src/commands/slash/[category]/[name].py`:

```python
import discord
from discord import app_commands
from src.handlers.models import SlashCommand


async def my_callback(interaction: discord.Interaction):
    await interaction.response.send_message("Response")


cmd_data = app_commands.Command(
    name="commandname",
    description="Command description",
    callback=my_callback,
)

command = SlashCommand(data=cmd_data, category="public")
```

### Creating Prefix Commands

Create a new file in `src/commands/prefix/[category]/[name].py`:

```python
import discord
from src.handlers.models import PrefixCommand


async def my_handler(message: discord.Message, args: list[str]):
    await message.reply("Response")


command = PrefixCommand(
    name="commandname",
    description="Command description",
    category="public",
    aliases=["cmd"],
    handler=my_handler,
)
```

---

**Discord Handler** - A modern, scalable Discord bot framework built with Python.
