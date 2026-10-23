
import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

books = []
page_number = 1

while url:
    print("Scraping page", page_number)

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").get_text(strip=True)
        availability = book.select_one(".availability").get_text(strip=True)
        rating = book.select_one(".star-rating")["class"][1]

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })

    next_link = soup.select_one("li.next a")

    if next_link:
        url = urljoin(url, next_link["href"])
        page_number += 1
        time.sleep(1)
    else:
        url = None

df = pd.DataFrame(books)

df.to_csv("books_data.csv", index=False)

print("\nFirst five books:")
print(df.head())

print("\nTotal books collected:", len(df))
print("Data saved to books_data.csv")
