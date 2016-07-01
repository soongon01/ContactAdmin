"""
main executable module
"""
from model.contact import Contact
import service.contact_service_db as svc

import sqlite3

def main():

    contact = Contact('han','011-3456-2222','han@daum.net', 25)
    svc.regist_contact(contact)
    #print('등록 완료')

    a_list = svc.search_contact('han')
    print(a_list)

    """
    create_table_query = \
        'create table contact (name text, hpnum text, email text, age int);'
    insert_query = "insert into contact values(?,?,?,?)"
    #1. establish connection
    con = sqlite3.connect('contact.db')
    #2. get cursor from the db
    cur = con.cursor()
    #3. send SQL to the db from cursor
    #cur.execute(insert_query, ('kim','010-3333-4444','kim@daum.net',30))
    cur.execute('select * from contact;')
    a_record = cur.fetchone()
    print(a_record[0])
    #print('insert ok..')
    #4. transaction
    con.commit()
    #5. release resource
    con.close()
    """



if __name__ == "__main__":
    main()