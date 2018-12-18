from database import Connection
 
def UpdateQuantity(product_id,product_quantity):
    try:
        db,cursor = Connection()
        update_sql=f"""
                        update product set product_quantity = product_quantity + {product_quantity}
                        where product_id like '{product_id}'; 
                    """
        cursor.execute(update_sql)
    except Exception:
        db.rollback()
    else:
        db.commit()
        print("Quantity updated successfully !")
    finally:
        db.close()
 
def RegisterProduct(product_name,product_price,product_quantity,create_date):
    db,cursor = Connection()
     
    insert_sql = f""" insert into product(product_name,product_price,product_quantity,create_date) 
                    values('{product_name}','{product_price}','{product_quantity}','{create_date}');
                 """
                  
    search_sql = f""" select * from product 
                    where product_name like '{product_name}';
                """
    flag = 0 # used to check whether the new product details are already present in db or not
    try:
        cursor.execute(search_sql)
        rs = cursor.fetchall()
        if(len(rs)>0):
            flag=1
    except Exception:
        print("There is some error in databse connection!")
    else:
        if(flag==1):
            data = input("The product is already present inside the databse do you want to update the quantity (y/n) ? ")
            if(data == 'y' or data=='Y'):
                product_id = rs[0][0]
                # product_quantity = int(input("Enter the quantity to be added : ")) 
                # since rs is a tuple of ((data))
                 
                # quantity updation 
                UpdateQuantity(product_id, product_quantity)
        elif(flag==0):
            cursor.execute(insert_sql)
            print("Inserted successfully into the database")
            db.commit()
    finally:
        db.close()
# RegisterProduct('abc', '50', 10, '20/8/2018')
 
def GetProductDetails(product_id):
    try:
        db,cursor = Connection()
        search_sql =f"""
                        select * from product where product_id like {product_id};
                    """
        cursor.execute(search_sql)
        rs = cursor.fetchall() 
    except Exception:
        print("Error loading database")
    else:
        for x in rs:
            print(f"{'Product ID'.ljust(40)}{str(x[0]).ljust(40)}")
            print(f"{'Product Name'.ljust(40)}{x[1].ljust(40)}")
            print(f"{'Product Price'.ljust(40)}{x[2].ljust(40)}")
            print(f"{'Product Quantity Available'.ljust(40)}{x[3].ljust(40)}")
            print(f"{'Added'.ljust(40)}{x[4].ljust(40)}")
    finally:
        db.close()
        # return rs
 
# print("".center(80,'-'))
def DeleteProduct(product_id):
    db,cursor = Connection()
    delete_sql = f"delete from product where product_id={product_id};"
    try:
        cursor.execute(delete_sql)
        db.commit()
    except Exception:
        db.rollback()
        print("Some error in deleting the product")
    else:
        print("Product deleted successfully")
    finally:
        db.close()
 
def GetAllProducts():
    try:
        db,cursor = Connection()
        search_sql = """
                            select * from product;
                    """
        cursor.execute(search_sql)
        rs = cursor.fetchall()
    except Exception:
        print("Error in connection")
    else:
        print("Product ID".center(20) + "Product_Name".center(20) + "Product Quantity Available".center(20))
        for x in rs:
            print(f"{str(x[0]).center(20)}{x[1].center(20)}{str(x[3]).center(20)}")
    finally:
        db.close()
# GetAllProducts()