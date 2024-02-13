from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
import json
from bson import json_util

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
uri = f"mongodb+srv://{username}:{password}@serverlessinstance0.3fnxace.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.db
collection = db.quotes

def insertOne(data):
    result = collection.insert_one(data)
    return result

def insertMany(data):
    result = collection.insert_many(data)
    return result

def getRandomQuote():
    cursor = collection.aggregate( [ { "$sample": { "size" : 1 } } ] )
    for i in cursor:
        quote = i.get("quotes")
        author = i.get("author")
    return {"quote": quote, "author": author}

def getTenRandomQuotes():
    lst = []
    cursor = collection.aggregate( [ { "$sample": { "size" : 10 } } ] )
    for i in cursor:
        quote = i.get("quotes")
        author = i.get("author")
        lst.append({"quote": quote, "author": author})
    return lst

def getQuoteByAuthor(author: str):
    cursor = collection.aggregate([ 
        { "$match": { "author" : author } },
        { "$sample": { "size" : 1 } } 
        ])
    for i in cursor:
        quote = i.get("quotes")
        author = i.get("author")
    return {"quote": quote, "author": author}

def getQuotesByAuthor(author: str):
    lst = []
    cursor = collection.aggregate([ 
        { "$match": { "author" : author } },
        { "$sample": { "size" : 10 } } 
        ])
    for i in cursor:
        quote = i.get("quotes")
        author = i.get("author")
        lst.append({"quote": quote, "author": author})
    return lst

def parse_json(data):
    return json.loads(json_util.dumps(data))

# Used for testing purposes
# def deleteMany():
#     result = collection.delete_many({})
#     return result

# file is meant to be imported as a module instead of executing directly
if __name__ == "__main__":
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)