import asyncio
import time

from src.bot import Bot
from src.config import config
from src.database.mongo import mongo
from src.handlers.anticrash import setup_anticrash
from src.handlers.commands import load_slash_commands
from src.handlers.events import load_events
from src.handlers.logger import print_startup_banner
from src.handlers.models import StartupData
from src.handlers.prefix import load_prefix_commands


async def main():
    start_time = time.time()

    bot = Bot()

    data = StartupData()

    print()
    print("=" * 50)
    print(f"  Starting {config.bot_name}...")
    print("=" * 50)
    print()

    print("  \ud83d\udee1\ufe0f Setting up anti-crash...")
    setup_anticrash(bot)

    print("  \ud83d\udce0 Loading events...")
    event_data = await load_events(bot)
    data.total_events = event_data.total_events

    print("  \u26a1 Loading slash commands...")
    slash_data = load_slash_commands(bot)
    data.total_slash = slash_data.total_slash

    print("  \ud83d\udcac Loading prefix commands...")
    prefix_data = load_prefix_commands(bot)
    data.total_prefix = prefix_data.total_prefix

    print("  \ud83c\udfdb\ufe0f Connecting to MongoDB...")
    await mongo.connect()

    print_startup_banner(data, start_time)

    try:
        await bot.start(config.token)
    except KeyboardInterrupt:
        pass
    finally:
        await mongo.close()
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
