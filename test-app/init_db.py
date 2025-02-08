import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())


cur = connection.cursor()

cur.execute("INSERT INTO calcs (x, y, operation, answer) VALUES (?, ?, ?, ?)", 
            (3, 5, "Add", 8.0))

cur.execute("INSERT INTO calcs (x, y, operation, answer) VALUES (?, ?, ?, ?)", 
            (3, 5, "Divide", 0.6))

connection.commit()
connection.close()