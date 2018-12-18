from admin import RegisterAdmin,CheckAdminLogin
from product import *
from datetime import datetime
from customer import *
from buying import *
# import pandas as pd

today_date = datetime.now()
today_date = str(today_date.day)+"."+str(today_date.month) + "." +str(today_date.year)
# print(today_date)
def customer_arena():
    print("Customer Sign Up".center(80,'-'))
    customer_name = input("Enter name : ").lower()
    customer_contact = input("Enter your contact : ")
    customer_address = input("Enter address : ")
    customer_type = input("Enter requirements(s/i) :")
    customer_email = input("Enter email address : ")
    register_date = today_date
    RegisterCustomer(customer_name, customer_contact, customer_address, customer_type, customer_email, register_date)

def main():
    while(True):
        print("Welcome To MDS".center(80,'*'))
        print("1 : admin")
        print("2 : Customer")
        print("3 : Register with us")
        print("4 : Close")
        choice = int(input("Enter your choice >>>"))
        if(choice == 1):
            print("admin login".center(80,'-'))
            username = input("Username : ").strip()
            password = input("Password : ").strip()
            status = CheckAdminLogin(username,password)
            if(status):
                print(f"Welcome {username}".center(80))
                while(True):
                    print("admin dashboard".center(80,'-'))
                    print("1: Insert new product")
                    print("2: Delete product")
                    print("3: View all registered products")
                    print("4: Add new customer")
                    print("5: Remove Customer")
                    print("6: All customers")
                    print("7: Customer details")
                    print("8: Log out")
                    choice = int(input("Enter your choice >>>"))
                    print("".center(80,'-'))
                    if(choice == 1):
                        product_name = input("Enter product name : ")
                        product_price = int(input("Enter product price : "))
                        product_quantity = int(input("Enter product quantity : "))
                        
                        RegisterProduct(product_name,product_price,product_quantity,today_date)
                    elif(choice == 2):
                        print("products".center(80,'-'))
                        GetAllProducts()
                        print("".center(80,'-'))
                        product_id = int(input("Enter product id to be deleted : "))
                        DeleteProduct(product_id)
                    elif(choice == 3):
                        print("products registered".center(80,'-'))
                        GetAllProducts()
                        print("".center(80,'-'))
                    elif(choice == 4):
                        customer_arena()
                    elif(choice == 5):
                        customer_id = int(input("Enter customer id to be deleted : "))
                        DeleteCustomer(customer_id)
                    elif(choice==6):
                        print("Registered customers".center(80,'-'))
                        GetAllCustomers()
                        print("".center(90))
                    elif(choice==7):
                        customer_id = int(input("Enter customer id : "))
                        CustomerPersonalDetails(customer_id)
                        ViewMyBuyingDetails(customer_id)
                    elif(choice == 8):
                        print("Logged out successfully")
                        print("".center(80,'-'))
                        break
            else:
                print("Invalid credentials entered")
        elif(choice == 2):
            print("customer login".center(80,'-'))
            customer_name = input("Enter your name : ").strip()
            customer_contact = input("Enter your contact number : ").strip()
            status,customer_id = CheckCustomerLogin(customer_name,customer_contact)
            if(status):
                print(f"Welcome {customer_name}".center(80))
                while(True):
                    print("customer dashboard".center(80,'-'))
                    print("1: Place an order")
                    print("2: View my buying details")
                    print("3: Generate my CSV")
                    print("4: Log out")
                    choice = int(input("Enter your choice >>>"))
                    if(choice==1):
                        print("Products".center(80,'-'))
                        GetAllProducts()
                        print("".center(80,'-'))
                        product_id = int(input("Enter product ID :"))
                        print("Product Details".center(80,'-'))
                        GetProductDetails(product_id)
                        print("".center(80))
                        if(input("Do you want to place an order(y/n): ").lower()=='y'):
                            PlaceOrder(customer_id, product_id,today_date)
                            # perform operations on  buying db
                        else:
                            print("Order Cancelled")
                    elif(choice==2):
                        ViewMyBuyingDetails(customer_id)
                    elif(choice==3):
                        pass
                        # generate a CSV
                    elif(choice==4):
                        print("Logged out successfully")
                        print("".center(80,'-'))
                        break
            else:
                print("Invalid credentials entered")
        elif(choice == 3):
            print("1: Register as admin")
            print("2: Register as customer")
            choice = int(input("Enter your choice >>>"))
            if(choice == 1):
                print("Admin Sign up".center(80,'-'))
                name = input("1: Enter name : ")
                username = input("2: Enter username : ")
                password = input("3: Enter password : ")
                contact_no = input("4: Enter contact number : ")
                register_date = today_date
                RegisterAdmin(name,username,password,contact_no,register_date)
            elif(choice == 2):
                customer_arena()
        elif(choice == 4):
            print("Thanks for using our service".center(80,'-'))
            break
        else:
            print("Invalid choice")
        
if __name__ == '__main__':
    main()