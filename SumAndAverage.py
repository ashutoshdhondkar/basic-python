#program to print average and sum of 10 numbers

n=int(input("Enter number of terms: "))
print("Enter numbers: ")
num1=int(input())
sumNo=num1
for i in range(1,n):
    num=int(input())
    sumNo=sumNo+num

print("The sum is : ",sumNo)

avg=sumNo/n

print("The average is : ",avg)
