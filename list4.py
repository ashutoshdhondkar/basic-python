'''
we wish to display only those words from the sentence that do not occur in a set of excluded words(like: this,and ,is,not).
The set of excluded words would be maintained in your code and the sentence is input from keyboard.
We have to display all words that do not exist in this set and we have to take care that multiple occurring words are displayed only once
'''

sentence=input("Enter a string :")
sentenceList=sentence.split(' ')        #converted string into list
excludedList=['this','and','is','not']      # created a list of excluded words

unique=[]   # created an empty list which will contain all unique words

for x in sentenceList:
    if (x not in excludedList) and (x not in unique) :
        unique.append(x)

# created a list of unique words


string=' '.join(unique)

print("The modified string : ",string)

