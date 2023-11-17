import sqlite3
conn=sqlite3.connect('add.db')

cr=conn.cursor()
query1='create table IF NOT EXISTS attend (rollno integer primary key,name TEXT ,DOB DATE ,TotalDays integer , days integer )'
cr.execute(query1)
conn.commit()
'''
entries=[
    (1, 'John Doe', '1995-05-15', 100, 90),
    (2, 'Jane Smith', '1998-02-22', 100, 95),
    (3, 'Bob Johnson', '1997-08-10', 100, 80),
    (4, 'Alice Brown', '1996-11-30', 100, 85),
    (5, 'Charlie Wilson', '1999-04-05', 100, 92)
]

cr.executemany('insert INTO attend (rollno, name, DOB, TotalDays, days)values(?,?,?,?,?)',entries)'''
def checkone(roll):    
    cr.execute('select* from attend where rollno=?',roll)
    print(cr.fetchone())

def checkall():
    query2='select* from attend '
    cr.execute(query2)
    print(cr.fetchall())

def AddEntry(roll,name,date,total,no):
    cr.execute('insert into attend values(?,?,?,?,?)',(roll,name,date,total,no))
    conn.commit()

def remove(no):
    cr.execute('delete from attend where rollno=?',(no,))
    conn.commit()

def change(attend,roll):
    cr.execute("update attend set days=? where rollno=?",(attend,roll))
    conn.commit()

def defaulters(attendance):
    cr.execute('select name,rollno,days from attend where days<?',(attendance,))
    print("students with attendance less than", attendance)
    print(cr.fetchall())







