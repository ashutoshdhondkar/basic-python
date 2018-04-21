# program to demonstrate pickle
import pickle
class Emp:
    def __init__(self,name,prn):
        self.name = name
        self.prn = prn

    def Display(self):
        print(" ID : {}".format(self.prn))
        print("Name : {} ".format(self.name))

fp = open("pickle.dat","wb")
n=int(input("Enter number of employees : "))

for x in range(n):
    prn = input("Enter id : ")
    name = input("Enter name : ")
    e = Emp(name,prn)
    pickle.dump(e,fp)

fp.close()

fp = open("pickle.dat",'rb')
for x in range(n):
    e = pickle.load(fp)
    e.Display()

fp.close()
