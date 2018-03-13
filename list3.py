# display all the words that are contained in a sentence.
#words that come multiple times should be displayed only once

sentence=input("Enter a string :");
sentenceList=sentence.split(' ')
#converted string into list on basis of blank spaces

unique=[]   #creating a blank list which will contain all unique words

for x in sentenceList:
    if x not in unique:
        unique.append(x)

# this will create a list of unique words

string = ' '.join(unique)
# the join function is used to create a string

print("The updated string is : ",string)
