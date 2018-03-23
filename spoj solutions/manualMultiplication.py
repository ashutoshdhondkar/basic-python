# manual multiplication

num1=int(input("Enter num1 : "))
num = input("Enter num2 : ")
num2=[int(x) for x in list(num)]
# store the second number in the form of list

addition=0  
deci=10 

print(num1)
print("*",num)

if(len(num2)==1):   #if num2 is a 1 digit number
    temp=num1 * num2[len(num2)-1]
    print("-"*8)
    print(temp)
else:   #if num2 is  multidigit number
    print("-"*8)
    for x in range(len(num2)):
        temp = num1 * num2[len(num2) -x-1]
        temp=temp*(deci**x);
        print(" "*(len(num2)-x-1),temp)
        addition += temp

    print("-"*8)
    print(addition)

    
'''
output:

Enter num1 : 123
Enter num2 : 321
123
* 321
--------
   123
  2460
 36900
--------
39483

'''
