from fastapi import FastAPI
from db import getRandomQuote, getTenRandomQuotes, getQuotesByAuthor
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/api/author/{author}")
def author(author: str) -> List[data]:
    author = author.lower()
    if author == "kennedy": # John F. Kennedy
        return getQuotesByAuthor("John F. Kennedy")
    elif author == "trump": # Donald Trump
        return getQuotesByAuthor("Donald Trump")
    elif author == "obama": # Barack Obama
        return getQuotesByAuthor("Barack Obama")
    elif author == "reagan": # Ronald Reagan
        return getQuotesByAuthor("Ronald Reagan")
    elif author == "roosevelt": # Franklin D. Roosevelt
        return getQuotesByAuthor("Franklin D. Roosevelt")
    elif author == "bush": # George W. Bush
        return getQuotesByAuthor("George W. Bush")
    elif author == "clinton": # Bill Clinton
        return getQuotesByAuthor("Bill Clinton")
    elif author == "washington": # George Washington
        return getQuotesByAuthor("George Washington")
    elif author == "truman": # Henry Truman
        return getQuotesByAuthor("Harry S. Truman")
    elif author == "johnson": # Lyndon B. Johnson
        return getQuotesByAuthor("Lyndon B. Johnson")
    elif author == "biden": # Joe Biden
        return getQuotesByAuthor("Joe Biden")
    elif author == "lincoln": # Abraham Lincoln
        return getQuotesByAuthor("Abraham Lincoln")
    else:
        return {"error": "Incorrect author name. Please check the docs for more information."}
    