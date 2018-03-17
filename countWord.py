#make a function that inputs a string and a word and returns how many times the
#word occured in sentence

def countWord(text,word):
    l=[]
    l=text.split(' ')
    return l.count(word)    

sentence=input("Enter a text: ")
word=input("enter a word that is to be counted: ")
print("the word has occured ",countWord(sentence,word)," times")
