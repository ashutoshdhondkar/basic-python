from database import Connection

def PlaceOrder(customer_id,product_id,create_date):
    buying_quantity = int(input("Enter quantity : "))
    search_sql = f"select product_quantity,product_price from product where product_id = {product_id};"
    # product_quantity,product_price
    db,cursor = Connection()
    #print(create_date)
    try:
        cursor.execute(search_sql)
        rs = cursor.fetchall()
        product_price = int(rs[0][1])
        # print(product_price)
        # print(f"Type of product id : {type(rs[0][0])}")
        if(int(rs[0][0]) >= buying_quantity):
            insert_sql = f"""insert into buying(customer_id,product_id,
                        buying_quantity,total_bill,buying_date)
                        values({customer_id},{product_id},{buying_quantity},{product_price*buying_quantity},
                        '{create_date}'
                        );
                        """
            cursor.execute(insert_sql)
            update_sql = f"""update product set product_quantity =  product_quantity - {buying_quantity}
                            where product_id = {product_id};
                        """
            cursor.execute(update_sql)
            db.commit()
            print("Added to your cart!!")
        else:
            print("Out of Stock")
    except Exception as e:
        print(e)
        db.rollback()
    else:
        db.close()
        
# PlaceOrder(4,12,'23.8.2018')

def ViewMyBuyingDetails(customer_id):
    search_sql = f"select * from buying where customer_id = {customer_id}"
    db,cursor = Connection()
    total_bill = 0
    try:
        cursor.execute(search_sql)
        rs = cursor.fetchall()
    except Exception:
        print("Sorry unable to connect to database")
    else:
        print("Buying details".center(0,'-'))
        print("Product Name".center(20) + "buying Quantity".center(20) + "Price (Rs.)".center(20) +"Buying date".center(20))
        for x in rs:
            search_sql = f"select product_name from product where product_id = {x[2]};"
            cursor.execute(search_sql)
            product_name = cursor.fetchall()[0][0]
            print(f"{product_name.center(20)}{str(x[3]).center(20)}{str(x[4]).center(20)}{x[5].center(20)}")
            total_bill += int(x[4])
        print("".center(80,'-'))
        print(f"Your Total bill is Rs. {total_bill}".center(80))
    finally:
        db.close()
# ViewMyBuyingDetails(4)
            
def GenerateCSV():
    pass