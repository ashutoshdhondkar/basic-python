# program to implement CRUD
# the program will add userid and respective password to database

import sqlite3

conn = sqlite3.connect("sample.db") # created a database and its object

while(1):
    print("****Main Menu****")
    print("1: create a table")
    print("2: insert data")
    print("3: update a data")
    print("4: view data of particular account")
    print("5: view all the data")
    print("6: delete row")
    print("7: exit")
    ip = int(input("Enter your choice : "))
    if(ip==1):
        conn.execute('''CREATE TABLE IF NOT EXISTS INFORMATION(
                        USERID TEXT PRIMARY KEY NOT NULL,
                        PASSWORD TEXT NOT NULL);
                    ''')
        print("Table created successfully")
    elif(ip==2):
        userid = input("Enter your userid : ")
        password = input("Enter password :")
        conn.execute('''INSERT INTO INFORMATION(USERID,PASSWORD) VALUES('%s','%s')'''%(userid,password))
        conn.commit()
    elif(ip==3):
        userid = input("Enter userid : ")
        new = input("Enter new password:")
        conn.execute("UPDATE INFORMATION SET PASSWORD = '%s' WHERE USERID = '%s';"%(new,userid))
        conn.commit()
    elif(ip==4):
        userid=input("Enter userid :")
        result = conn.execute("SELECT * FROM INFORMATION WHERE USERID='%s';"%(userid))
        for row in result:
            print("userid = {} and password = {}".format(row[0],row[1]))
    elif(ip==5):
        result = conn.execute("SELECT * FROM INFORMATION")
        for row in result:
            print("Userid = {} and password = {}".format(row[0],row[1]))
    elif(ip==6):
        userid = input("Enter userid:")
        conn.execute("DELETE FROM INFORMATION WHERE USERID = '%s';"%(userid))
        print("Data deleted successfully")
    elif(ip==7):
        exit()
