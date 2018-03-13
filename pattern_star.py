'''
*
* *
* * *
* * * *
'''
#program to print above pattern

n=int(input("Enter number of rows: "))

for x in range(n):
    for k in range(x+1):
        print("* ",end=" ")
    print("\n")

