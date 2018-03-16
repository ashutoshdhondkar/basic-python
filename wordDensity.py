# word density

sentence = input("Enter a sentence : ").split(' ')
lengthOfSentence = len(sentence)
word = input("Enter a word whose density you need to find : ")
count=0
for x in sentence:
    if x==word:
        count+=1
print("The density of '",word,"' is ",count/lengthOfSentence)
