# given a  list of percentage of student, get a list of grades

# with comprehension
n=int(input("Enter number of students:"))
marks=[]

def calculate(x):
    if(x >= 75):
        return 'A+'
    elif(x>=60 and x<75):
        return 'A'
    elif(x>=50 and x<60):
        return 'B'
    else:
        return 'C'
       

for i in range(n):
    marks.append(int(input()))

grades=[x for x in map(calculate,marks)]

print(grades)
