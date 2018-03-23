import msvcrt
print("Enter numbers:")
while(1):
    c=int(input(msvcrt.getch()))
    if c == 42:
        print(c)
        break
