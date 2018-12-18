from database import Connection

def RegisterCustomer(customer_name,customer_contact,customer_address,customer_type,customer_email,register_date):
    db,cursor = Connection()
    search_sql = f"select * from customer where customer_contact = '{customer_contact}';"
    insert_sql =f"""insert into customer(customer_name,customer_contact,customer_address,customer_type,
                                    customer_email,register_date)
                    values('{customer_name.lower()}','{customer_contact}','{customer_address}','{customer_type}',
                           '{customer_email}','{register_date}'); 
                """
    flag = 0
    try: 
        cursor.execute(search_sql)
        rs = cursor.fetchall()
        # print(rs)
        if(len(rs)>0):
            flag = 1
    except Exception as e:
        print(e)
        print("Error connecting to database")
    else:
        if(flag==1):
            # return False
            print("Customer is already registered")
        elif(flag==0):
            cursor.execute(insert_sql)
            db.commit()
            print("Successfully created account")
            # return True
    finally:
        db.close()

# RegisterCustomer('ashutosh', '9819270718', 'chembur', 's', '@gmail.com', '2018')

def CheckCustomerLogin(customer_name,customer_contact):
    flag = 0
    db,cursor = Connection()
    search_sql = f"select * from customer where customer_name like '{customer_name}' and customer_contact like '{customer_contact}';"
    try:
        cursor.execute(search_sql)
        rs = cursor.fetchall()
        if(len(rs)>0):
            flag = 1
    except Exception as e:
        print(e)
        print("Something went wrong")
    else:
        if(flag == 1):
            # registerd user
            # print("Registered customer")
            return True,rs[0][0]
        else:
            # invalid customer
            # print("invalid customer")
            return False,None
            # print("Do you wish to register")
    finally:
        db.close()
# CheckCustomerLogin('ashutosh', '9819270718')

def GetAllCustomers():
    db,cursor = Connection()
    search_sql = "select * from customer;"
    try:
        cursor.execute(search_sql)
        rs = cursor.fetchall()
    except Exception:
        print("Error in loading customers")
    else:
        print("Customer Id".center(20)+"Customer Name".center(30)+"Customer contact".center(30))
        for x in rs:
            print(f"{str(x[0]).center(20)}{x[1].center(30)}{x[2].center(30)}")
    finally:
        db.close()
# GetAllCustomers()

def DeleteCustomer(customer_id):
    db,cursor = Connection()
    # flag=0
    delete_sql = f"delete from customer where customer_id = {customer_id};"
    search_sql = f"select * from customer where customer_id = {customer_id};"
    try:
        cursor.execute(search_sql)
        rs = cursor.fetchall()
        if(len(rs)>0):
            cursor.execute(delete_sql)
            db.commit()
            print("Customer deleted successfully")
        else:
            print("No such customer exists please check all the customers")
    except Exception:
        db.rollback()
        print("Some error in deleting the customer")
    else:
        pass
    finally:
        db.close()

def CustomerPersonalDetails(customer_id):
    search_sql = f"select * from customer where customer_id = {customer_id};"
    db,cursor = Connection()
    try:
        cursor.execute(search_sql)
        rs = cursor.fetchall()
    except Exception:
        pass
    else:
        print("Personal Details".center(80,'-'))
        for x in rs:
            print("Customer Id".ljust(40) + str(x[0]).ljust(40))
            print("Customer Name".ljust(40) + str(x[1]).ljust(40))
            print("Customer Contact".ljust(40) + str(x[2]).ljust(40))
            print("Customer address".ljust(40) + str(x[3]).ljust(40))
            print("Customer type".ljust(40) + str(x[4]).ljust(40))
            print("Customer email".ljust(40) + str(x[5]).ljust(40))
            print("Registration date".ljust(40) + str(x[6]).ljust(40))
        print("".center(80))
    finally: 
        db.close()