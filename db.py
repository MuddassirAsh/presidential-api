from pymongo.mongo_client import MongoClient
url = ""
client = MongoClient(url)
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
        quote = i.get("quote")
        author = i.get("author_title")
        origin = i.get("origin")
        if quote and author and origin:
            return {"quote": quote, "author": author, "origin": origin}
        elif quote and author:
            return {"quote": quote, "author": author}
        else:
            return {"quote": quote}

def getTenRandomQuotes():
    data = []
    cursor = collection.aggregate( [ { "$sample": { "size" : 10 } } ] )
    for i in cursor:
        quote = i.get("quote")
        author = i.get("author_title")
        origin = i.get("origin")
        if quote and author and origin:
            data.append({"quote": quote, "author": author, "origin": origin})
        elif quote and author:
            data.append({"quote": quote, "author": author})
        else:
            data.append({"quote": quote})
    return data

def getQuotesByAuthor(author: str):
    data = []
    cursor = collection.aggregate([ 
        { "$match": { "author_title" : author } },
        { "$sample": { "size" : 10 } } 
        ])
    for i in cursor:
        quote = i.get("quote")
        author = i.get("author_title")
        origin = i.get("origin")
        if quote and author and origin:
            data.append({"quote": quote, "author": author, "origin": origin})
        elif quote and author:
            data.append({"quote": quote, "author": author})
        else:
            data.append({"quote": quote})
    return data

# Used for testing purposes
# def deleteMany():
#     result = collection.delete_many({})
#     return result

# file is meant to be imported as a module instead of executing directly
if __name__ == "__main__":
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        x = getQuotesByAuthor("John F. Kennedy")
        print(x)
    except Exception as e:
        print(e)
    