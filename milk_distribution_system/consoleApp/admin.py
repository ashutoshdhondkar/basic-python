from database import Connection

def RegisterAdmin(name,username,password,contact_no,register_date,access_token= '1234'):
    db,cursor = Connection()
    search_sql = f"select username from admin where username = '{username}';"
    insert_sql =f"""insert into admin(name,username,password,contact_no,register_date,access_token)
                    values('{name}','{username}','{password}','{contact_no}','{register_date}','{access_token}'); 
                """
    flag = 0
    try: 
        cursor.execute(search_sql)
        rs = cursor.fetchall()
        # print(rs)
        if(len(rs)>0):
            flag = 1
            # print(rs[3])
    except Exception as e:
        print(e)
        print("Error connecting to database")
    else:
        if(flag==1):
            print("username already taken")
            # return False
        elif(flag==0):
            cursor.execute(insert_sql)
            db.commit()
            print("Registered successfully as admin")
            # return True
    finally:
        db.close()

# RegisterAdmin('ashutosh','ashutosh_5199','ashutosh','9819270718','21/08/2018','1234')

def CheckAdminLogin(username,password):
    flag = 0
    db,cursor = Connection()
    search_sql = f"select * from admin where username like '{username}' and password like '{password}';"
    try:
        cursor.execute(search_sql)
        rs = cursor.fetchall()
        if(len(rs)>0):
            flag = 1
    except Exception:
        print("Something went wrong")
    else:
        if(flag == 1):
            # registerd user
            return True
        else:
            # invalid admin
            return False
            # print("Do you wish to register")
    finally:
        db.close()