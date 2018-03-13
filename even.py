#program to generate the first 'n' even numbers

n=int(input("Enter number of terms : "))
for x in range(n+1):
    if x%2 == 0:
        print(x)
