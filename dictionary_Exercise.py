# program to store roll,gender,marks,age in dictionary
# retrive data stored in a file


fp=open("DataStored.txt","r")
data=fp.read().split('\n')

# function that can be used to store thing into dicionary and
# can be used with map comprehension
def ConvertDict(inp):
    line=inp.split(',')
    roll_no=line[0]
    name=line[1]
    gender=line[2]
    marks=int(line[3])

    return roll_no,name,gender,marks


# function to calculate name of students who have secured marks greater than specified marks
def getHigherThan(num):
    # dictionary that will contain all the records bsed on rollno as a key
    dictionary={rollNo:{'name':name,'gender':gender,'marks':marks} for rollNo,name,gender,marks in map(ConvertDict,data)}
    print(dictionary)    
    toppers=[]
    for x in dictionary:
        if(dictionary[x]['marks']>num):
            toppers.append(dictionary[x]['name'])
    return toppers

    
print(getHigherThan(70))


fp.close()
