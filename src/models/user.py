from src.database.mongo import mongo


class UserModel:
    @staticmethod
    async def get(user_id: str):
        return await mongo.get_user(user_id)

    @staticmethod
    async def create_or_update(user_id: str, data: dict):
        return await mongo.create_user(user_id, data)
