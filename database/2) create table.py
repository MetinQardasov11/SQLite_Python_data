import sqlite3 as sql
connect = sql.connect('Library_new.db')
cursor = connect.cursor()
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS Books(NAME TEXT, AUTHOR TEXT, PUBLISHING_HOUSE TEXT,PAGE_SIZE INT)')
    connect.commit() 
create_table()  

connect.close()