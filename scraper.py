import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlalchemy
from database import create_table, save_to_db
from datetime import datetime

url="http://books.toscrape.com/"
respone=requests.get(url)
soup=BeautifulSoup(respone.text, "html.parser")
Books=soup.find_all("article", class_="product_pod")

data=[]

for book in Books:
    title = book.h3.a["title"]
    price_text = book.find("p", class_="price_color").text
    price = float(re.sub(r"[^\d.]", "", price_text))

    data.append({
        "title": title,
        "price": price,
        "date": datetime.now()
    })

df=pd.DataFrame(data)
create_table()
save_to_db(df)
print("successfully")
