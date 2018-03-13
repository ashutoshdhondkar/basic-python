'''
hi apple hello apple good apple
list1=[apple,good,hello,hi]
list2=[occurrence]
'''

str1=input("Enter a string : ")
a=str1.split(' ')
unique=[]
occurrence=[]
for x in a:
    if x not in unique:
        unique.append(x)

unique.sort()
for x in unique:
    count=0
    for val in a:
        if(x==val):
            count=count+1
    occurrence.append(count)

print(unique)
print(occurrence)
