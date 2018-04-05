# we have two text files article.txt and ignore.txt
#load the words of ignore.txt into a set as the words to be ignored
#now we have to build a dictionary of words along with their frequencies as they occur in article.txt after exccluding the ignored words
#The final result should be stored word list which do not occur in the ignore word list
#and we wish to get their frequencies and density(frequency/total words)*100)

article=open("article.txt","r")

ignore=open("ignore.txt","r")

articleList=article.read().split(' ')
ignoreList=ignore.read().split(',')

uniqueArticleList=[]

#create a list of words that are in article.txt with no repetition of words
for x in articleList:
    if(x not in ignoreList):
        if(x not in uniqueArticleList):
            uniqueArticleList.append(x)
    

def evaluate(unique):
    return unique,articleList.count(unique)



dictionary={x:count for x,count in map(evaluate,uniqueArticleList)}
print(dictionary)


dictionary={x:count for x,count in map(evaluate,uniqueArticleList)}
keyList=[]
density=[]

for each in dictionary.keys():
    keyList.append(each)
keyList.sort()
for each in keyList:
    density.append((dictionary[each] *100/len(articleList)))

print(density)

