#This file crats a single shared database to MongoDB
from pymongo import MongoClient
from pymongo.database import Database
from app.config import settings
#MongoClient manages pool of connections to MongoDBserver 
client : MongoClient = MongoClient(settings.MONGO_URI)
database : Database = client[settings.MONGO_DB_NAME]
#Sends a ping command to the MongoDB  to confirm that the connection is alive
def ping_database() -> bool:
    try:
        client.admin.command('ping')
        return True
    except Exception :
        return False