# create a class studentInfo
# create the following functions:
#   1. highest marks student info
#   2. Display all student name
#   3. Operator overloading to add student details


class studentInfo:
    def __init__(self):
        self.fp=open("DataStored.txt",'r')
        # reading data from files
        self.text=self.fp.read()
        self.data=self.text.split('\n')

        self.dictionary={rollno:{'name':name,'gender':gender,'marks':marks} for rollno,name,gender,marks in map(self.ConvertDict,self.data)}
        #   dictionary of student created   
            
        print(self.dictionary)
        
    
    def ConvertDict(self,data):
        self.ip=data.split(',')
        return self.ip[0],self.ip[1],self.ip[2],self.ip[3]

    def DisplayHighest(self):
        self.markList = []
        for x in self.dictionary:
            self.markList.append(self.dictionary[x]['marks'])

        self.maxMarks =max(self.markList)
        print(self.maxMarks)
    
        for x in self.dictionary:
            if(self.dictionary[x]['marks'] == self.maxMarks):
                print(self.dictionary[x])

    def DisplayNames(self):
        self.names=[]
        for x in self.dictionary:
            self.names.append(self.dictionary[x]['name'])

        print(self.names)

    def __add__(self,gradeList):
        for x in self.dictionary:
            if(int(self.dictionary[x]['marks']) > 60):
                self.dictionary[x]['grade'] = gradeList[0]
            elif(int(self.dictionary[x]['marks'] >40) and int(self.dictionary[x]['marks']) <= 60):
                self.dictionary[x]['grade'] = gradeList[1]
            else:
                self.dictionary[x]['grade'] = gradeList[2]

        print(self.dictionary)

                        
                                 
        
sts=studentInfo()

sts.DisplayHighest()
sts.DisplayNames()
gradeList=['A','B','F']
sts + gradeList
