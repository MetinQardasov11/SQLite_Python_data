import sqlite3 as sql
connect = sql.connect('Library_new.db')
cursor = connect.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS Books(NAME TEXT, AUTHOR TEXT, PUBLISHING_HOUSE TEXT,PAGE_SIZE INT)')
    connect.commit() 
def select_data_from_table():
    cursor.execute("SELECT * FROM Books")
    list_1 = cursor.fetchall()
    print("Books table's datas.......")
    for i in list_1:
        print(i)
def delete_data(author):
    cursor.execute("DELETE FROM Books WHERE AUTHOR = ?",(author,))
    connect.commit()

#delete_data('Imam gazali')
select_data_from_table()
connect.close()