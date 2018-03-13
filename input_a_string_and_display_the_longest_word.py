#input a sentence and display the longest word

string=input("Enter a string :")
# the input is stored in variable string

list1=string.split(' ')
# the input string is converted into list on basic of white spaces

list2=[]    # this is a list of unique words

for x in list1:
    if x not in list2:
        list2.append(x)

longest = len(list2[0])
# here we have assumed that the first word of unique list is longest



for x in list2:
    if longest< len(x) :
        longest = x

print("The longest word in given string is : ",longest)
