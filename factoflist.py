def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


def factoflist(a,b):
    d={x:fact(x) for x in range(a,b+1)}
    return d


l={}
l=factoflist(2,6)
print(l)
# same thing bt put it into dictonary
