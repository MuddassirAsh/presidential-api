from fastapi import FastAPI
from db import getRandomQuote, getTenRandomQuotes, getQuotesByAuthor
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class data(BaseModel):
    quote: str
    author: str
    origin: Optional[str] | None = None

@app.get("/api/random")
def random() -> data:
    return getRandomQuote()

@app.get("/api/quotes")
def quotes() -> List[data]:
    return getTenRandomQuotes()

@app.get("/api/author/{author}")
def author(author: str) -> List[data]:
    if author == "Kennedy": # John F. Kennedy
        return getQuotesByAuthor("John F. Kennedy")
    elif author == "Trump": # Donald Trump
        return getQuotesByAuthor("Donald Trump")
    elif author == "Obama": # Barack Obama
        return getQuotesByAuthor("Barack Obama")
    elif author == "Reagan": # Ronald Reagan
        return getQuotesByAuthor("Ronald Reagan")
    elif author == "Roosevelt": # Franklin D. Roosevelt
        return getQuotesByAuthor("Franklin D. Roosevelt")
    elif author == "Bush": # George W. Bush
        return getQuotesByAuthor("George W. Bush")
    elif author == "Clinton": # Bill Clinton
        return getQuotesByAuthor("Bill CLinton")
    elif author == "Washington": # George Washington
        return getQuotesByAuthor("George Washington")
    elif author == "Truman": # Henry Truman
        return getQuotesByAuthor("Henry Truman")
    elif author == "Johnson": # Lyndon B. Johnson
        return getQuotesByAuthor("Lyndon B. Johnson")
    elif author == "Biden": # Joe Biden
        return getQuotesByAuthor("Joe Biden")
    elif author == "Lincoln": # Abraham Lincoln
        return getQuotesByAuthor("Abraham Lincoln")
    else:
        return {"error": "Incorrect author name. Please check the docs for more information."}