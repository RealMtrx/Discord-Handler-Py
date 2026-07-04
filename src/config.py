import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self.token = os.getenv("TOKEN", "#")
        self.client_id = os.getenv("CLIENT_ID", "#")
        self.bot_name = os.getenv("BOT_NAME", "Discord Handler")
        self.prefix = os.getenv("PREFIX", "$")
        self.owner_ids = [
            x.strip() for x in os.getenv("OWNER_IDS", "#,#").split(",")
        ]
        self.mongodb_uri = os.getenv("MONGODB_URI", "#")
        self.error_webhook = os.getenv("ERROR_WEBHOOK", "#")
        self.slash_command_webhook = os.getenv("SLASH_WEBHOOK", "#")
        self.prefix_command_webhook = os.getenv("PREFIX_WEBHOOK", "#")
        self.join_guild_webhook = os.getenv("JOIN_WEBHOOK", "#")
        self.leave_guild_webhook = os.getenv("LEAVE_WEBHOOK", "#")
        self.ready_webhook = os.getenv("READY_WEBHOOK", "#")


config = Config()
