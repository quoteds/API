import requests
# from urllib.request import Request, urlopen
import urllib
import re
import time
import sqlite3
from bs4 import BeautifulSoup

# url = "http://wisdomquotes.com/love-quotes/"

# response = ''
# while response == '':
#     try:
#         response = requests.get(url)
#         break
#     except:
#         print("Connection refused by the server..")
#         print("Let me sleep for 5 seconds")
#         print("ZZzzzz...")
#         time.sleep(5)
#         print("Was a nice sleep, now let me continue...")
#         continue
# # response = requests.get(url)
# print(response)

# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# # page = urllib.request.urlopen(url)
# page = urlopen(req).read()
# print(page)
# soup = BeautifulSoup(page, "html.parser")

# name = soup.find_all("blockquote")
# quotes = {}

url = "http://wisdomquotes.com/life-quotes/"

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

query = "SELECT COUNT(*) FROM love"
row = cursor.execute(query)
stuff = row.fetchall()

if stuff[0][0] != 0:
    connection.commit()
    connection.close()
else:
    query = "INSERT INTO love VALUES (?, ?, ?)"
    for quote in quotes:
        cursor.execute(query,(quote,quotes[quote],0))
    connection.commit()
    connection.close()