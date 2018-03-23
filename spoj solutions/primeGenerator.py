import math

def IsPrime(n):
    #this function will return true if the number is prime
    try:
        for i in range(2,int(math.sqrt(n))+1):
            flag=0
            if(n%i == 0):
                flag=1
                break
            
        if flag==0:
            return 1
        else:
            return 0
    except UnboundLocalError:
        return 0
        
testCases = eval(input ("Enter number of test cases: "))
l=[int(x) for x in input("Enter upper limit and lower limit for both the cases:").split(' ')]
# whatever is entered by user will be stored in form of list
for i in range(0,len(l),2):
    a=l[i]
    b=l[i+1]
    for prime in range(a,b+1):
        if prime == 2 or prime == 3:
            print(prime)
            continue
        if IsPrime(prime):
            print(prime)
    print("\n")
