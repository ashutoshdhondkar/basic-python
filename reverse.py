'''
take ip as string and print it in reverse order
eg=ran a cat

opp=cat a ran
'''
str1=input("Enter a string ")
a=[]
a=str1.split()
a.reverse()
str1=' '.join(a)
print(str1)
