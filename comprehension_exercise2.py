# program to calculate cube of each number in list

'''
#without comprehension
List=[1,2,3,4,5,6,7,8,9,10]
cubelist=[]
for x in List:
    cubelist.append(x*x*x)

print(cubelist)
'''

# with comprehension
List=[1,2,3,4,5,6,7,8,9,10]

cubelist=[x for x in map(lambda x:x**3,List)]
print(cubelist)
