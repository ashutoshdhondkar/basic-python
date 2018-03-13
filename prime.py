#pogram to check whether the number entered is prime or not

num=int(input("Enter number : "))
for x in range(2,num):
    flag=0
    if num%x ==0:
        flag=1
        break
if flag ==0:
    print("The number ",num,"is prime number!")
else:
    print("The number ",num," is composite number!")
