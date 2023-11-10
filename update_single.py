import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId


load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

document_to_update = {"_id": ObjectId("654dea47d91d97979fd1ad36")}

add_to_balance = {"$inc": {"balance": 100}}

pprint.pprint(accounts_collection.find_one(document_to_update))

result = accounts_collection.update_one(document_to_update, add_to_balance)
print("Document updated: " + str(result.modified_count))

pprint.pprint(accounts_collection.find_one(document_to_update))

client.close()
