# function that takes file name as parameter and returns a list of words that are
#contained in it,taking care that multiple occuring words are given only once


fname=input("Enter name of file : ");

def countOccurrence(fname):
    f=open(fname,"r")
    # open the file in read mode
    unique=[]   #created an empty list for feeding unique words
    sen=[]
    for line in f:
        # this for loop is for each line in f
        sen=line.split()
        # spliting each line in a list called sen
        for word in sen:
            # for each word in sen
            if word not in unique:
                # if tha word is not in unique list append that word to unique
                # bsically we are doing this to avoid occurrence of multiple
                # occurrence of a single word
                unique.append(word)

    return(unique)
        

print("The list of words is: \n",countOccurrence(fname))
