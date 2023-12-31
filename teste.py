import sqlite3 as sql

conn = sql.connect('src/dados.db')
c = conn.cursor()

c.execute(
    'create table if not exists user(Id integer primary key autoincrement, server real, user text, pwd text)'
)
c.execute(
    'DELETE FROM user'
)
conn.commit()