from pymongo import MongoClient


class MongoManager:

    def __init__(self, database, collection):
        uri = "mongodb://localhost:27017/?readPreference=primary"
        self.mongoClient = MongoClient(uri)

        self.database = database
        self.collection = collection

    def insert_document(self, document):
        self.mongoClient.get_database(self.database).get_collection(self.collection).insert_one(document=document)

    def get_all_documents(self):
        return self.mongoClient.get_database(self.database).get_collection(self.collection).find()

    def close(self):
        self.mongoClient.close()