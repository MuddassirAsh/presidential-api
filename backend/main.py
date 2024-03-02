from fastapi import FastAPI
from db import getRandomQuote, getTenRandomQuotes, getQuoteByAuthor, getQuotesByAuthor
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

presidents =  \
{
    "kennedy": "John F. Kennedy",
    "trump": "Donald Trump",
    "obama": "Barack Obama",
    "reagan": "Ronald Reagan",
    "roosevelt": "Franklin D. Roosevelt",
    "bush": "George W. Bush",
    "clinton": "Bill Clinton",
    "washington": "George Washington",
    "truman": "Harry S. Truman",
    "johnson": "Lyndon B. Johnson",
    "biden": "Joe Biden",
    "lincoln": "Abraham Lincoln"
} 

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class data(BaseModel):
    quote: str
    author: str

@app.get("/api/random")
def random() -> data:
    return getRandomQuote()

@app.get("/api/quotes")
def quotes() -> List[data]:
    return getTenRandomQuotes()

@app.get("/api/random/{author}")
def quote(author: str) -> data:
    author = author.lower()
    return getQuoteByAuthor(presidents[author])

@app.get("/api/author/{author}")
def author(author: str) -> List[data]:
    author = author.lower()
    return getQuotesByAuthor(presidents[author])

handler = Mangum(app)