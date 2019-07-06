import json, sqlite3, os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'seed.json')

with open (filename, 'r', encoding = "utf8") as f:
    quotes = json.load(f)

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# cursor.execute("DROP TABLE anime")
# cursor.execute("DROP TABLE temp")

create_table = "CREATE TABLE IF NOT EXISTS anime (quote text, author text, likes int)"
cursor.execute(create_table)

query = "SELECT COUNT(*) FROM anime"
row = cursor.execute(query)
stuff = row.fetchall()

if stuff[0][0] != 0 :
    connection.commit()
    connection.close()
else :
    query = "INSERT INTO anime VALUES (?, ?, ?)"
    for quote in quotes["List"]:
        cursor.execute(query,(quote['quote'], quote['author'],0))
    connection.commit()
    connection.close()
