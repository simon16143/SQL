import sqlite3
class todo:
  def __init__(self):   
    self.conn = sqlite3.connect('ok.db')
    self.c = self.conn.cursor()
    self.create_work_table()
  def create_work_table(self):
      self.c.execute = ('''CREATE TABLE IF NOT EXISTS work(id INTEGER PRIMARY KEY,
                name TEXT NOT NULL, priority INTEGER NOT NULL);''')
  def add_work(self):
      name = input('add an work: ')
      priority = int(input('add the priority: '))
      for row in self.c.execute('SELECT name FROM work'): 
          if row == name:
              print('El nombre ya se encuentra en la tabla.')
          else:
              self.c.execute('INSERT INTO work(name,priority) VALUES (?,?)',(name,priority))
              self.c.execute('SELECT * FROM work')
              self.conn.commit()
app = todo()
app.add_work()
