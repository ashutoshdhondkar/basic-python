# program to implement inheritance

class Employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def DisplayName(self):
        return '{} {} '.format(self.fname,self.lname)

    def DisplaySalary(self):
        return self.pay

class Developer(Employee):
    def __init__(self,fname,lname,pay,language):
        super().__init__(fname,lname,pay)
        self.language = language

    def DisplayLanguage(self):
        return self.language


obj = Developer('ashutosh','Dhondkar',50000,'python')

print("Full NAme : {} ".format(obj.DisplayName()))

print("Salary : {}".format(obj.DisplaySalary()))

print("programming Language : {}".format(obj.DisplayLanguage()))
