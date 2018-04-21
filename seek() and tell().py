# program to demonstrate seek() and tell() in file handling
# tell() gives us the current position of file pointer
# seek() takes the file pointer to specified position

fp= open("my temperature.txt",'r')
print("The file pointer is at : {} ".format(fp.tell()))
content = fp.read(13)
    # read upto 13 th bit
print(content,end = ' ')

#print("The file pointer is now pointing at {}".format(fp.tell()))
content = fp.readline()
print(content)
fp.seek(0)  # take the pointer back to 0 th bit
content = fp.readline()
print("The contents after taking the pointer back to 0th bit : \n")
print(content)
