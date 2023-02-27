import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:
        MONGO_DB_URL = "mongodb+srv://trialmongo:version2022@cluster0.2gugo3n.mongodb.net/test"

        # self.client = pymongo.MongoClient(os.getenv('MONGO_DB_URL'),tlsCAFile=ca)
        self.client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)

        self.db_name="sensor_proj"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
