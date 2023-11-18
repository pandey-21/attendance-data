import sqlite3
conn=sqlite3.connect('add.db')

cr=conn.cursor()
query1='create table IF NOT EXISTS attend (rollno integer PRIMARY KEY,name TEXT ,DOB DATE ,TotalDays integer , days integer )'
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
def checkone():
    roll=int(input('enter roll no of student'))
    cr.execute('select* from attend where rollno=?',(roll,))
    print(cr.fetchone())

def checkall():
    query2='select* from attend '
    cr.execute(query2)
    
    print(cr.fetchall(),sep='/n')

def AddEntry():
    roll=int(input('enter roll no of student- '))
    name=input('enter name of student- ')
    dob=input('enter DOB of student- ')
    no=int(input('enter no of days attended by student- '))
    cr.execute('insert into attend values(?,?,?,?,?)',(roll,name,dob,100,no))
    conn.commit()

def remove():
    roll=int(input('enter roll no of student to be removed- '))
    cr.execute('delete from attend where rollno=?',(roll,))
    conn.commit()

def change():
    roll=int(input('enter roll no of student to change attendance'))
    attend=int(input('change in attendance'))
    cr.execute("update attend set days=? where rollno=?",(attend,roll))
    conn.commit()

def defaulters():
    attendance=int(input('check less attendance'))
    cr.execute('select name,rollno,days from attend where days<?',(attendance,))
    print("students with attendance less than", attendance)
    print(cr.fetchall())

while True:
    print('Student Database Menu: select from following',sep='/n')
    print('1.View Records of all students')
    print('2.View Records of only 1 students')
    print('3.Add another student')
    print('4.delete data of particular student')
    print('5.update attendance of a student thru roll number')
    print("6.Check students with less attendance")
    print("enter anything to exit program")

    choice=int(input('Choose your query- '))
    if choice==1:
        checkone()
    
    elif choice==2:
        checkall()

    elif choice==3:
        AddEntry()

    elif choice==4:
        remove()

    elif choice==5:
        change()
    
    elif choice==6:
        defaulters()
    else:
        print('thank you!')
        break

    



        





