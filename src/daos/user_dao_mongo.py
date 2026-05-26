import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from models.user import User


class UserDAOMongo:

    def __init__(self):

        try:
            load_dotenv()

            mongo_host = os.getenv("MONGODB_HOST")
            mongo_user = os.getenv("DB_USERNAME")
            mongo_password = os.getenv("DB_PASSWORD")
            db_name = os.getenv("MYSQL_DB_NAME")

            # connexion MongoDB Docker
            self.client = MongoClient(
                f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:27017/"
            )

            self.db = self.client[db_name]
            self.collection = self.db["users"]

        except Exception as e:
            print("Erreur :", str(e))

    def select_all(self):

        users = []

        for doc in self.collection.find():

            user = User(
                str(doc["_id"]),
                doc["name"],
                doc["email"]
            )

            users.append(user)

        return users

    def insert(self, user):

        result = self.collection.insert_one({
            "name": user.name,
            "email": user.email
        })

        return str(result.inserted_id)

    def update(self, user):

        result = self.collection.update_one(
            {"_id": ObjectId(user.id)},
            {
                "$set": {
                    "name": user.name,
                    "email": user.email
                }
            }
        )

        return result.modified_count

    def delete(self, user_id):

        result = self.collection.delete_one(
            {"_id": ObjectId(user_id)}
        )

        return result.deleted_count

    def close(self):
        self.client.close()