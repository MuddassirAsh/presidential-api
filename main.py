from fastapi import FastAPI
from db import getRandomQuote, getTenRandomQuotes, getQuotesByAuthor
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class data(BaseModel):
    quote: str
    author: str
    origin: Optional[str]

@app.get("/random")
def random():
    return getRandomQuote()

@app.get("/quotes")
def quotes() -> List[data]:
    return getTenRandomQuotes()

@app.get("/author/{author}")
def author(author: str) -> List[data]:
    return getQuotesByAuthor(author)