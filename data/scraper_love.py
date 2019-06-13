import requests
import urllib.request
import re
import time
import sqlite3
from bs4 import BeautifulSoup

url = "http://wisdomquotes.com/love-quotes/"

response = requests.get(url)
print(response)

page = urllib.request.urlopen(url)
print(page)
soup = BeautifulSoup(page, "html.parser")

name = soup.find_all("blockquote")
quotes = {}

for i in range(1,200):
    line = name[i].text.strip()
    arr = [i for i, a in enumerate(line) if a == "."]
    if len(arr) == 1 and arr[0] < 200:
        quote = line[:arr[0]+1]
        if 'tweet' not in (line[arr[0]+2:]):
            print(line[arr[0]+2:])
            quotes[quote] = line[arr[0]+2:]

print(quotes)

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# cursor.execute("DROP TABLE nature")
create_table = "CREATE TABLE IF NOT EXISTS love (qoute text, author text, likes int)"
cursor.execute(create_table)

query = "INSERT INTO love VALUES (?, ?, ?)"

for quote in quotes:
        cursor.execute(query,(quote,quotes[quote],0))

connection.commit()
connection.close()