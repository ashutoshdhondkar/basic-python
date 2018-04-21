# piglatin code

import re
word = input("Enter a word : ")

pattern = re.compile("[aAeEiIoOuU]")

m = pattern.match(word) # match will compare only first word then proceed
if(m):
    print("Begins with a vowel")
    print("Piglatin word : {}".format(word+'way'))

else:
    print("Begins with consonent")
    s = pattern.search(word).start()
    print(s)
    after = word[s:]
    before = word[0:s]
    print("piglatin word :{}".format(after + before+'ay'))
