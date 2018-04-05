#Wap to check whether an input number is multiple of 5 and is greater than 17
'''
#without comprehension
ip=int(input("Enter a number : "))
if(ip%5==0) and (ip>17):
    print("Satisfied")
else:
    print("Not satisfied")

        
'''
# with comprehension

def check(num):
    if(num%5==0 and num>17):
        return True
    else:
        return False

lis=[10,15,20,17,30,18]
nl=[x for x in filter(lambda x: True if(x%5==0 and x>17) else False,lis)]
print(nl)







