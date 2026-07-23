import sqlite3

# connection setup
connection=sqlite3.connect("DataofClass.db")

with connection:
    connection.execute(""" 
    CREATE TABLE IF NOT EXISTS interns(
      intern_id INTEGER PRIMARY KEY AUTOINCREMENT, 
      name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE
    );
                       
""")