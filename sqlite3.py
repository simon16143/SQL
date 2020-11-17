import sqlite3

conn = sqlite3.connect('First')
c = conn.cursor()
c.execute('''CREATE TABLE tasks(id INTEGER PRIMARY KEY,name TEXT NOT NULL,priority INTEGER NOT NULL
);''')


c.execute('INSERT INTO tasks(id,name,priority) VALUES(?,?,?)',(0,'My first Task',1))
