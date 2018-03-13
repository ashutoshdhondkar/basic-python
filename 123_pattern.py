'''
1
1 2
1 2 3
1 2 3 4
'''
#write a program to print above pattern

n=int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
