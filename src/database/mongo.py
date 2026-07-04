import asyncio
import logging

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure
import dns.resolver
import dns.asyncresolver

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ["8.8.8.8", "8.8.4.4", "1.1.1.1"]
dns.asyncresolver.default_resolver = dns.asyncresolver.Resolver(configure=False)
dns.asyncresolver.default_resolver.nameservers = ["8.8.8.8", "8.8.4.4", "1.1.1.1"]

from src.config import config


class MongoManager:
    def __init__(self):
        self.client: AsyncIOMotorClient | None = None
        self.db = None

    async def connect(self) -> bool:
        if not config.mongodb_uri or config.mongodb_uri == "#":
            print("  \u274c MongoDB URI not configured, skipping")
            return False

        try:
            self.client = AsyncIOMotorClient(
                config.mongodb_uri,
                serverSelectionTimeoutMS=10000,
                connectTimeoutMS=10000,
            )
            self.db = self.client.get_default_database()
            await self.client.admin.command("ping")
            print("  \u2705 MongoDB connected successfully")
            return True
        except (ServerSelectionTimeoutError, ConnectionFailure, Exception) as e:
            print(f"  \u274c MongoDB connection failed: {e}")
            return False

    async def get_user(self, user_id: str):
        if not self.db:
            return None
        return await self.db.users.find_one({"_id": user_id})

    async def create_user(self, user_id: str, data: dict | None = None):
        if not self.db:
            return None
        doc = {"_id": user_id, "created_at": asyncio.get_event_loop().time()}
        if data:
            doc.update(data)
        await self.db.users.update_one({"_id": user_id}, {"$setOnInsert": doc}, upsert=True)
        return doc

    async def close(self):
        if self.client:
            self.client.close()
            print("  \u2705 MongoDB connection closed")


mongo = MongoManager()
