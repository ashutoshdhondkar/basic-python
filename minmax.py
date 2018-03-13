#program to print max and min of 'n' numbers without using any data structure

print("*****MENU*****")
print("1: finding minimum of 'n' numbers")
print("2: finding maximum of 'n' numbers")
choice=int(input("enter your choice here>>>"))
print("***************")


if choice==2:
    n=int(input("Enter number of elements: "))
    print("enter numbers: ")
    maxNo=int(input(""))
    for i in range(1,n):
        num1=int(input())
        if num1>maxNo:
            maxNo=num1

    print("The max number is : ",maxNo)

elif choice==1:
    n=int(input("Enter number of elements :"))
    print("Enter numbers :")
    minNo=int(input())
    for i in range(1,n):
        num1=int(input())
        if num1<minNo:
            minNo=num1
    print("The min number is : ",minNo)
        

        
