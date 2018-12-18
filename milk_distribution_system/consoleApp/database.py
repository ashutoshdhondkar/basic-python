import pymysql as sql

# function to connect to database and return a cursor and a database object
def Connection(host = "localhost",user="root",password="",dbname="mds"):
    try:
        db = sql.connect(host,user,password,dbname)
        cursor = db.cursor()
    except Exception as e:
        print(e)
        print("Error in connection")
    else:
        # print("connected successfully")
        return db,cursor

# Connection()
