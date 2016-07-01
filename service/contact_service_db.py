"""

"""
import sqlite3

def regist_contact(contact):
    query = 'insert into contact values(?,?,?,?);'

    con = sqlite3.connect('contact.db')
    cur = con.cursor()
    cur.execute(query,(contact.name, contact.hpnum, contact.email, contact.age))
    con.commit()
    con.close()


def view_all_contact():
    pass

def _to_dic(line):
    pass

def modify_contact(contact):
    pass

def remove_contact(name):
    pass

def search_contact(name):
    con = sqlite3.connect('contact.db')
    cur = con.cursor()
    cur.execute('select * from contact where name=?', (name,))
    a_list = cur.fetchone()
    con.close()

    return a_list


if __name__ == "__main__":
    print("실행 모듈이 아닙니다.")