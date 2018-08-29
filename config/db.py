from pymongo import MongoClient, errors
from config.config import DATABASE_CONFIG

def getdb():
    client = MongoClient(DATABASE_CONFIG['host'], DATABASE_CONFIG['port'])
    db = client[DATABASE_CONFIG['database']]
    return db



