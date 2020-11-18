import sqlite3
#El objeto de conexion se crea en la vairable conn
conn = sqlite3.connect('Second')

c = conn.cursor()
c.execute('''CREATE TABLE task(id INTEGER PRIMARY KEY,name TEXT NOT NULL,priority INTEGER NOT NULL);''')


c.execute('INSERT INTO task(name,priority) VALUES (?,?)',('PRUEBAx',223))
