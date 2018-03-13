'''
a=int(input("Enter a number:"))
b=int(input("Enter number which you want to trace:"))

count=0

while a!=0:
    if(a%10)==b:
        count=count+1
    a=a//10

print("The value ",b,"is repeated ",count,"times")'''
'''
a=int(input("Enter max limit : "))
b=0
c=1
print(b)
print(c)
sum1=b+c
while(sum1<a):
    print(sum1)
    b=c
    c=sum1
    sum1=b+c
'''
'''

a=int(input("Enter a number : "))
fact=1
for x in range(1,a+1):
    fact=fact*x

print(fact)
'''


a=int(input("Enter starting limit: "))
b=int(input("Enter ending limit :"))
for x in range(a,b+1):
    flag=0
    for k in range(2,x):
        if x%k == 0:
            flag=1
            break
    if flag==0:
        print(x)











