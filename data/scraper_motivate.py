import requests
import urllib.request
import re
import time
import sqlite3
from bs4 import BeautifulSoup

url = "https://www.inc.com/lolly-daskal/100-motivational-quotes-that-will-inspire-you-to-succeed.html"

response = requests.get(url)
print(response)

page = urllib.request.urlopen(url)
print(page)
soup = BeautifulSoup(page, "html.parser")

name = soup.find_all("div",attrs={'element':'p'})
# name_s = name.text.strip()
quotes = {}

for i in range(3,len(name)):
    line = name[i].text.strip()
    quote = line[3:]
    arr = [i for i, a in enumerate(quote) if a == "\""]
    print(arr)
    if len(arr) == 2:
        quotes[(quote[arr[0]:arr[1]+1])] = (quote[arr[1]+4:])

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# cursor.execute("DROP TABLE motivate")
create_table = "CREATE TABLE IF NOT EXISTS motivate (qoute text, author text, likes int)"
cursor.execute(create_table)

query = "INSERT INTO motivate VALUES (?, ?, ?)"

for quote in quotes: 
    if quotes[quote] != "Anonymous":
        cursor.execute(query,(quote,quotes[quote],0))

connection.commit()
connection.close()