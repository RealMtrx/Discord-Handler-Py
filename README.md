# Discord Handler — Python

A modern, modular Discord bot handler built with **discord.py v2**, featuring **slash commands** and **prefix commands**, MongoDB integration, webhook logging, and an anti-crash system.

## ✨ Features

- **Slash Commands** (`/ping`)
- **Prefix Commands** (`$ping`)
- **Modular Architecture** — commands and events auto-loaded from `src/commands/` and `src/events/`
- **MongoDB** via `motor` for async database operations
- **Webhook Logging** for errors, guild join/leave, command usage, and ready events
- **Anti-Crash** — catches unhandled exceptions and event errors gracefully
- **Cooldown System** per user per command
- **Custom DNS** (Google / Cloudflare) for stable MongoDB connections

## 📁 Structure

```
Discord-Handler-Py/
├── src/
│   ├── main.py                 # Entry point
│   ├── bot.py                  # Custom Bot class
│   ├── config.py               # Config from .env
│   ├── core/                   # Utilities (webhooks, cooldown, emojis)
│   ├── database/               # MongoDB connection (motor)
│   ├── models/                 # Data models
│   ├── events/                 # Discord event listeners
│   ├── handlers/               # Loaders (commands, events, anticrash, logger)
│   └── commands/
│       ├── slash/              # Slash command modules
│       └── prefix/             # Prefix command modules
├── requirements.txt
├── .env.example
└── LICENSE
```

## 🚀 Usage

1. **Clone** the repo
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Copy `.env.example` to `.env`** and fill in your values (token, client ID, webhooks, etc.)
4. **Run the bot:**
   ```bash
   python src/main.py
   ```

## ⚙️ Requirements

- Python 3.10+
- discord.py >= 2.4.0
- motor (async MongoDB driver)
- python-dotenv
- aiohttp

## 📦 Deployment

```bash
pip install -r requirements.txt
python src/main.py
```

## 📄 License

MIT — see [LICENSE](LICENSE)
