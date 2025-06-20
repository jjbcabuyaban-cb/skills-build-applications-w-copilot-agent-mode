from pymongo import MongoClient

def get_mongo_client():
    """Create and return a MongoDB client."""
    client = MongoClient("mongodb://localhost:27017/")
    return client

def get_database(client, db_name):
    """Get a specific database."""
    return client[db_name]
