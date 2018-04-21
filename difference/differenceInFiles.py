# program to find common lines in two text files and store them in third file

fp1 = open('file1.txt','r')
fp2 = open('file2.txt','r')

list1 = fp1.read().split('\n')
list2 = fp2.read().split('\n')

print(list1)
print(list2)

commonLines = []
flag = 0
for x in list1:
    for y in list2:
        if(x == y):
            flag = 1
            commonLines.append(y)

if(flag == 0):
    commonLines.append("There is no line common between these two files")

fp1.close()
fp2.close()

fp1 = open('difference.txt','w')
fp1.writelines(commonLines)
fp1.close()
