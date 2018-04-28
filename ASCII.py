# program to get ascii value

while(True):
    print("****Main Menu****")
    print("1: To get Ascii value of particular character")
    print("2: To print character from Ascii value")
    print("3: EXIT")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        char = input("Enter a character : ")
        print("The ASCII value is : {}".format(ord(char)))
    elif(choice==2):
        asc = int(input("Enter ASCII value: "))
        print("The character is : {}".format(chr(asc)))
    else:
        exit()

