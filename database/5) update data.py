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
def update_data_publishing(old_publishing_house, new_publishing_house):
    cursor.execute("UPDATE Books SET PUBLISHING_HOUSE = ? WHERE PUBLISHING_HOUSE = ?",(new_publishing_house,old_publishing_house))
    connect.commit()
def update_data_author(new_author, old_author):
    cursor.execute("UPDATE Books SET AUTHOR = ? WHERE AUTHOR = ?",(new_author,old_author))
    connect.commit()


update_data_author('Imam gazali','Nizami Gencevi')
update_data_publishing("Horasan","Gence")
select_data_from_table()
connect.close()