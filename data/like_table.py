import sqlite3

options = [
    "life",
    "motivate",
    "love",
    "nature",
    "anime",
    "spiritual"
]

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

table = "CREATE TABLE IF NOT EXISTS main (name text, likes int)"
cursor.execute(table)

query = "INSERT INTO main VALUES (?, ?)"

for name in options:
    cursor.execute(query, (name, 0))

connection.commit()
connection.close()
