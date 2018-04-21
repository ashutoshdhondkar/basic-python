fp = open('DataStored.txt','r')
content = fp.read().split('\n')
lines = len(content)

words = 0
letters = 0
for x in content:
    cont = x.split(' ')
    words = words + len(cont)
    for x in cont:
        letters = letters + len(x)

fp.close()
print("Number of lines {}".format(lines))
print("Number of words {}".format(words))
print("Number of letters {}".format(letters))
