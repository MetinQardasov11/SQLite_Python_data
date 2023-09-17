import sqlite3 as sql
connect = sql.connect('Library_new.db')
cursor = connect.cursor()

connect.close()