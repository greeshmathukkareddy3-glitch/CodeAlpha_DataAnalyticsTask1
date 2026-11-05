import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

print("Website Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.find_all("article", class_="product_pod"):
    name = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]

    books.append({
        "Book Name": name,
        "Price": price,
        "Rating": rating
    })

df = pd.DataFrame(books)

print(df)

df.to_csv("books_data.csv", index=False)

print("Data saved successfully!")