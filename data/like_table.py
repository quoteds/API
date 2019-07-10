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

# cursor.execute("DROP TABLE anime")

table = "CREATE TABLE IF NOT EXISTS main (name text, likes int, users int)"
cursor.execute(table)

query = "SELECT COUNT(*) FROM main"
row = cursor.execute(query)
stuff = row.fetchall()

if stuff[0][0] != 0 :
    connection.commit()
    connection.close()
else :
    query = "INSERT INTO main VALUES (?, ?, ?)"
    for name in options:
        cursor.execute(query, (name, 0, 0))
    connection.commit()
    connection.close()

