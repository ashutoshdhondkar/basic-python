# function that prints factorial of all numbers specified by user
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


def factoflist(a,b):
    d={x:fact(x) for x in range(a,b+1)}
    return d


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
l={}
l=factoflist(a,b)
print(l)
