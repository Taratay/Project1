import sqlite3 as db


def createtables():
    cur.execute(""
                "CREATE TABLE DRUGS("
                "DRUGSID INTEGER PRIMARY KEY,"
                "NAME VARCHAR(30),"
                "COUNTRY VARCHAR(30),"
                "PRICE MONEY);")

    cur.execute(""
                "CREATE TABLE TREATMENT("
                "TREATMENTID INTEGER PRIMARY KEY,"
                "DRUGSID INTEGER,"
                "DAYUSING INTEGER,"
                "INDAYUSING INTEGER,"
                "DOSE INTEGER,"
                "FOREIGN KEY (DRUGSID) REFERENCES DRUGS(DRUGSID));")

    cur.execute(""
                "CREATE TABLE DIAGNOSIS("
                "DIAGNOSISID INTEGER PRIMARY KEY ,"
                "NAME VARCHAR(30),"
                "TREATMENTID INTEGER,"
                "FOREIGN KEY (TREATMENTID) REFERENCES TREATMENT(TREATMENTID));")

    cur.execute(""
                "CREATE TABLE JOBPOSITION("
                "JOBPOSITIONID INTEGER PRIMARY KEY,"
                "NAME VARCHAR(30));")

    cur.execute(""
                "CREATE TABLE EMPLOYEE("
                "EMPLOYEEID INTEGER PRIMARY KEY,"
                "SURNAME VARCHAR(20),"
                "NAME VARCHAR(15),"
                "PATRONYMIC VARCHAR(20),"
                "BIRTHDAY DATE,"
                "BIRTHDAYCITY VARCHAR(20),"
                "POSITIONID INTEGER,"
                "OKLAD MONEY,"
                "NADBAVKA MONEY,"
                "DATAVIPLATU DATE,"
                "FOREIGN KEY(POSITIONID) REFERENCES JOBPOSITION(JOBPOSITIONID));")

    cur.execute(""
                "CREATE TABLE DOCTOR("
                "DOCTORID INTEGER PRIMARY KEY,"
                "EMPLOYEEID INTEGER,"
                "FOREIGN KEY(EMPLOYEEID) REFERENCES EMPLOYEE(EMPLOYEEID));")

    cur.execute(""
                "CREATE TABLE PATIENT("
                "PATIENTID INTEGER PRIMARY KEY,"
                "SURNAME VARCHAR(20),"
                "NAME VARCHAR(15),"
                "PATRONYMIC VARCHAR(20),"
                "BIRTHDAY DATE,"
                "CARDNUMBER VARCHAR(10),"
                "DOCTORID INTEGER,"
                "FOREIGN KEY(DOCTORID) REFERENCES DOCTOR(DOCTORID));")

    cur.execute(""
                "CREATE TABLE RECEPTION("
                "RECEPTIONID INTEGER PRIMARY KEY,"
                "PATIENTID INTEGER,"
                "EMPLOYEEID INTEGER,"
                "RECEPTIONDATE DATE,"
                "CABINET INTEGER,"
                "DIAGNOSISID INTEGER,"
                "DATALIKARNANOGO DATE,"
                "FOREIGN KEY(PATIENTID) REFERENCES PATIENT(PATIENTID),"
                "FOREIGN KEY(EMPLOYEEID) REFERENCES EMPLOYEE(EMPLOYEEID),"
                "FOREIGN KEY(DIAGNOSISID) REFERENCES DIAGNOSIS(DIAGNOSISID));")

    con.commit()


def inserttables():
    cur.execute("INSERT INTO JOBPOSITION(name) "
                "values ('Alergist'),('Cardiologist'),('Dentist'),('Dermatologist'),('Gynecologist');")

    cur.execute("INSERT INTO PATIENT(Surname,Name,Patronymic,BIRTHDAY,CardNumber, DOCTORID) "
                "values ('Варламов','Геннадий','Леонидович','05.03.1963','1','2'),"
                "('Бобков','Виктор','Борисович','07.07.1978','2','3'),"
                "('Петренко','Геннадий','Ибрагимович','07.07.1978','3','1'),"
                "('Варламов','Йоши','Федорович','07.07.1988','33','4'),"
                "('Коваленко','Геннадий','Ибрагимович','05.11.1956','22','5'),"
                "('Мухамед','Ибрагим','','10.18.1948','15','5'),"
                "('Варламов','Геннадий','Ибрагимович','03.07.1983','158','5'),"
                "('Петренко','Виктор','Ибрагимович','07.12.1948','18','2'),"
                "('Варламов','Степан','Ибрагимович','01.07.1968','24','4'),"
                "('Новиков','Геннадий','Ибрагимович','12.07.1905','31','3');")

    cur.execute("INSERT INTO EMPLOYEE(Surname,Name,Patronymic,Oklad,BirthdayCity,Nadbavka,DataViplatu,positionid,Birthday) "
                "values ('Новиков','Степан','Федорович','1400,061','Киев','256,00','04.21.1955','1','04.21.1955'),"
                "('Бобков','Виктор','Борисович','4000,0598','Львов','123,00','06.14.1965','2','06.14.1965'),"
                "('Ванжула','Оксана','Петровна','3200,4657','Киев','456,00','02.12.1945','2','02.12.1945'),"
                "('Мацуки','Йоши','','2000,00','Москва','789,00','07.07.1978','3','07.07.1978'),"
                "('Петренко','Максим','Леонидович','4800,00','Луцк','321,00','03.12.1980','3','03.12.1980'),"
                "('Петренко','Максим','Леонидович','7000,00','Киев','654,00','09.17.1974','3','09.17.1974'),"
                "('Коваленко','Татьяна','Ивановна','4000,00','Ялта','987,00','11.23.1966','3','11.23.1966'),"
                "('Петрунько','Максим','Семенович','1569,00','Киев','147,00','12.04.1966','4','12.04.1966');")

    cur.execute("INSERT INTO DOCTOR (EMPLOYEEID)"
                "values ('1'),"
                "('2'),"
                "('3'),"
                "('5'),"
                "('7');")

    cur.execute("INSERT INTO DRUGS (NAME,COUNTRY,PRICE)"
        "values ('Lineks','Germany','2,00'),"
        "('Imodium','Germany','4,00'),"
        "('Amiksin','America','5,00'),"
        "('Atsinot','Poland','20,00'),"
        "('Lopan','Germany','1,00'),"
        "('Gekis','France','2,00'),"
        "('Anestetic','Germany','3,00'),"
        "('Jinas','Germany','7,00');")

    cur.execute("INSERT INTO TREATMENT(DRUGSID,DAYUSING,INDAYUSING,DOSE, DRUGSID)"
                "values ('4','4','2','2', '2'),"
                "('6','3','5','3', '1'),"
                "('7','4','2','2', '3'),"
                "('2','10','4','2', '3'),"
                "('8','1','1','6', '5'),"
                "('5','5','2','2', '4'),"
                "('3','2','3','4', '7');")

    cur.execute("INSERT INTO RECEPTION(PATIENTID,EMPLOYEEID,RECEPTIONDATE,CABINET,DIAGNOSISID,DATALIKARNANOGO)"
                "values ('4','2','09.24.2015','204','5','09.24.2015'),"
                "('2','2','09.24.2016','202','2','09.24.2016'),"
                "('6','4','09.27.2015','102','3','09.27.2015'),"
                "('1','3','10.14.2015','100','3','10.14.2015'),"
                "('1','6','05.04.2015','315','5','05.04.2015'),"
                "('3','1','09.30.2015','312','4','09.30.2015'),"
                "('7','5','11.23.2015','303','1','11.23.2015'),"
                "('5','5','12.12.2015','234','2','12.12.2015');")

    cur.execute("INSERT INTO DIAGNOSIS(name, TREATMENTID) "
                "values ('Flu', '1'),"
                "('Alzheimers disease', '2'),"
                "('Asthma', '3'),"
                "('Arthritis', '4'),"
                "('Tuberculosis', '5');")


    con.commit()
'''
def deletetables():
    cur.execute("DROP TABLE DRUGS")
    cur.execute("DROP TABLE TREATMENT")
    cur.execute("DROP TABLE DIAGNOSIS")
    cur.execute("DROP TABLE PATIENT")
    cur.execute("DROP TABLE JOBPOSITION")
    cur.execute("DROP TABLE EMPLOYEE")
    cur.execute("DROP TABLE DOCTOR")
    cur.execute("DROP TABLE RECEPTION")

    con.commit()
'''

con = db.connect('Hospital.db')
cur = con.cursor()
'''
deletetables()
'''
createtables()

inserttables()
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
