# given  a list of employee name,employee salary and appraisal pointers;
# calculate hike given to each employee.
#store the data in dictionary

n=int(input("Enter number of employees : "))
emp_name=[]
emp_sal=[]
emp_ptr=[]
print("Enter employee name,their salary and appraisal pointers")
for i in range(n):
    emp_name.append(input("Enter name of emp : " ))
    emp_sal.append(float(input("Enter salary of emp : ")))
    emp_ptr.append(float(input("Enter appraisal pointer of emp: ")))

def calculateHike(name,sal,ptr):
    if(ptr>=4.7):
        tempptr=15
    elif(ptr>=4.3 and ptr<=4.6):
        tempptr=13
    elif(ptr>=4 and ptr<=4.2):
        tempptr=10
    elif(ptr>=3.5 and ptr<4):
        tempptr=4
    elif(ptr<3.5):
        tempptr=0

    salaryHike=sal+sal*(tempptr/100)
    return name,sal,ptr,salaryHike

Dictionary={name:[sal,ptr,newSal] for name,sal,ptr,newSal in map(calculateHike,emp_name,emp_sal,emp_ptr)}

print(Dictionary)
