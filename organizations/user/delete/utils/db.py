from pymongo import MongoClient


class MongoDBConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient("mongodb+srv://kenfang:USxoXtLCp1EMp1wY@mydb.k3gmb.mongodb.net/myDB")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
