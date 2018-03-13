# input a sentence and input a word. we have to find how many times the word
# occured in sentence

sentence = input("Enter a string : ")
# taking a sentence from the user
sentenceList=sentence.split(' ')
# creating a new list using split on the basis of white spaces
word=input("Enter a word :")

print("The word : ",word," has appeared ",sentenceList.count(word)," time(s) in the entered string")

# list.count(word) returns how many times the 'word' has appeared in 'list'
