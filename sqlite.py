import sqlite3

conn = sqlite3.connect('hola.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY,name TEXT NOT NULL,priority INTEGER NOT NULL);''')
c.execute('INSERT INTO tasks(id,name,priority) VALUES(?,?,?)',(0,'Simon',123));
 
