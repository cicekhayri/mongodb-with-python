import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

new_accounts = [
    {
        "account_holder": "Bamse",
        "account_id": "MDB139001111",
        "account_type": "checking",
        "balance": 60218,
    },
    {
        "account_holder": "Joe",
        "account_id": "MDB239002222",
        "account_type": "checking",
        "balance": 6021822112,
    }
]

result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

client.close()
