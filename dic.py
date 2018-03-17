#from an input sentence,build a dictionary of words along with their frequency.
#display the words in sorted order along with their count

sentence=input("enter a text: ").split(' ')
d={}
for x in sentence:
    d.setdefault(x,sentence.count(x))
l=list(d.items())
l.sort()
print(l)
