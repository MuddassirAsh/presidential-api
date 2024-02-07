from db import insertMany, deleteMany
import json

try: 
    with open('./quotes/washington.json') as f:
        quotes = json.load(f)
    
    insertMany(quotes)
    print("Data has been successfully written to database")
except Exception as e:
    print(f"Something went wrong {e}")
