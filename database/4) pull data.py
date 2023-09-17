import sqlite3 as sql
connect = sql.connect('Library_new.db')
cursor = connect.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS Books(NAME TEXT, AUTHOR TEXT, PUBLISHING_HOUSE TEXT,PAGE_SIZE INT)')
    connect.commit() 
def pull_data_from_table():
    cursor.execute("SELECT * FROM Books")
    list_1 = cursor.fetchall()
    print("Books table's datas.......")
    for i in list_1:
        print(i)
def pull_name_author_from_table():
    cursor.execute("SELECT NAME,AUTHOR FROM Books")
    list_2 = cursor.fetchall()
    print("Books table's name and author datas........")
    for i in list_2:
        print(i)
def pull_data_where(publishing_house):
    cursor.execute("SELECT * FROM Books WHERE PUBLISHING_HOUSE = ?",(publishing_house,))
    list_3 = cursor.fetchall()
    for i in list_3:
        print(i)

#pull_data_from_table()
#pull_name_author_from_table() 
pull_data_where("Gence")
create_table()  
connect.close()
