import requests
from bs4 import BeautifulSoup
import json
from db import insertMany, insertOne, deleteMany

data = {}
parsed_quotes = []
pages = 11

for page in range(1, pages):
    url = f"https://www.goodreads.com/author/quotes/3047.John_F_Kennedy?page={page}"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    quotes = soup.find_all("div", class_="quoteText")

    for quote_element in quotes:
        quotes = soup.find_all("div", class_="quoteText")
        # Extracting the quote text and removing newline characters
        quote_text = quote_element.get_text(separator=' ', strip=True)

        # Extracting the author/title
        author_element = quote_element.find("span", class_="authorOrTitle")
        author_title = author_element.get_text(strip=True) if author_element else None

        # Extracting the origin if it exists
        origin_element = quote_element.find("i")
        origin_text = origin_element.get_text(strip=True) if origin_element else None

        origin_element2 = quote_element.find("a")
        origin_text2 = origin_element2.get_text(strip=True) if origin_element2 else None

        if origin_text:
            origin_text =  origin_text.replace("[", "").replace("]", "")
            quote_text = quote_text.replace(author_title, "").replace(origin_text, "").replace("―", "")\
            .replace("“", "").replace("”", "").replace("[", "").replace("]", "").strip()
        else:
            quote_text = quote_text.replace(author_title, "").replace("―", "")\
            .replace("“", "").replace("”", "").replace("[", "").replace("]", "").strip()
            
        if origin_text2:
            origin_text2 =  origin_text2.replace("[", "").replace("]", "")
            quote_text = quote_text.replace(origin_text2, "").strip()

        # The scraped author_title is very inconsistent and varied. Thus, it's better to hardcode this value
        # so it's consistent, when were making api calls by author name.
        author_title = "John F. Kennedy"

        # Adding to the parsed_quotes list as a dictionary
        if origin_text:
            data = {"quote": quote_text, "author_title": author_title, "origin": origin_text}
            parsed_quotes.append(data)
            continue
        elif origin_text2:
            data = {"quote": quote_text, "author_title": author_title, "origin": origin_text2}
            parsed_quotes.append(data)
        else:
            data = {"quote": quote_text, "author_title": author_title}
            parsed_quotes.append(data)

# Write parsed_quotes to a JSON file
try: 
    with open('parsed_quotes.json', 'w', encoding='utf-8') as json_file:
        json.dump(parsed_quotes, json_file, ensure_ascii=False, indent=2)
        print("Data has been successfully written to parsed_quotes.json")
    # insertMany(parsed_quotes)
except Exception as e:
    print(f"Something went wrong {e}")

