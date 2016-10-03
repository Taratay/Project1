import sqlite3 as db
from tkinter import *

root = Tk()


con = db.connect('Hospital.db')
cur = con.cursor()
'''
deletetables()
'''

cur.execute('SELECT * FROM JOBPOSITION')
for i in cur.fetchall():
    print(i)
cur.execute('SELECT * FROM PATIENT')
for i in cur.fetchall():
     print(i)
cur.execute('SELECT * FROM EMPLOYEE')
for i in cur.fetchall():
    print(i)
cur.execute('SELECT * FROM DRUGS')
for i in cur.fetchall():
    print(i)
cur.execute('SELECT * FROM TREATMENT')
for i in cur.fetchall():
    print(i)
cur.execute('SELECT * FROM RECEPTION')
for i in cur.fetchall():
    print(i)
cur.execute('SELECT * FROM DOCTOR')
for i in cur.fetchall():
    print(i)
cur.execute('SELECT * FROM DIAGNOSIS')
for i in cur.fetchall():
    print(i)

cur.execute('SELECT * FROM TREATMENT INNER JOIN DRUGS '
            'ON TREATMENT.DRUGSID == DRUGS.DRUGSID')
for i in cur.fetchall():
    print(i)
# for row in cur:
#     print('-'*10)
#     print('ID:', row[0])
#     print('First name:', row[1])
#     print('Second name:', row[2])
#     print('-'*10)
#
# cur.execute("DROP TABLE DRUGS")
# con.commit()
con.close()
root.mainloop()