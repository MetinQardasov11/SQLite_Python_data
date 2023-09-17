import sqlite3 as sql
connect = sql.connect('Library_new.db')
cursor = connect.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS Books(NAME TEXT, AUTHOR TEXT, PUBLISHING_HOUSE TEXT,PAGE_SIZE INT)')
    connect.commit() 
def add_data():
    cursor.execute("INSERT INTO Books VALUES('Sirler xezinesi', 'Nizami Gencevi','Gence',700)")
    connect.commit() 
def add_data_2(name,author,publishing_house,page_size):
    cursor.execute("INSERT INTO Books VALUES(?,?,?,?)",(name,author,publishing_house,page_size))
    connect.commit()

name = input('Name: ')
author = input('Author: ')
publishing_house = input('Publishing House: ')
page_size = int(input('Page Size: '))

add_data()
add_data_2(name,author,publishing_house,page_size) 

connect.close()