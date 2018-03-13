Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> a='hello'
>>> a*3
'hellohellohello'
>>> (a+" ")*3
'hello hello hello '
>>> #getting value at particular index
>>> a[3]
'l'
>>> a[0]
'h'
>>> a[4]
'o'
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[5]
IndexError: string index out of range
>>> #using capitalise
>>> a.capitalize()
'Hello'
>>> a
'hello'
>>> b=a.capitalize()
>>> b
'Hello'
>>> a
'hello'
>>> #using count()
>>> a.count('l')
2
>>> a.count('q')
0
>>> a='hello world'
>>> a.count('o')
2
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a.count('c',6)
0
>>> a.count('o',6)
1
>>> a.count('l',5,8)	#count o from 5th to 8th index
0
>>> 
>>> #using len()
>>> a.count('l',4,len(a)-2)
0
>>> #using find()
>>> a.find('w')
6
>>> a.find('l')
2
>>> a.find('l',4)
9
>>> a.find('l',3,8)
3
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
30
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
30
10 is less than  20
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
30
10 is less than  20
>>> a=10
>>> b=20
>>> print("hello") if a<b else print("world")
hello
>>> #ternary operator used above
>>> #its not necessary to use : after definition
>>> if a<b
SyntaxError: invalid syntax
>>> #: is not imp in ternary opeartor ....correction in above written statement about :
>>> while a>0:
	print(a)
	a=a-1

10
9
8
7
6
5
4
3
2
1
>>> a=10
>>> b=5
>>> while a>0 and b>0:
	print("a =",a,"b= ",b)
	a=a-1
	b=b-1

a = 10 b=  5
a = 9 b=  4
a = 8 b=  3
a = 7 b=  2
a = 6 b=  1
>>> #range()
>>> range(10)
range(0, 10)
>>> for x in range(10):
	print(x)

0
1
2
3
4
5
6
7
8
9
>>> #range(10)goes from 0-9
>>> for x in range(2,10):
	print(x)

2
3
4
5
6
7
8
9
>>> for x in range(2,10,2):
	print(x)

2
4
6
8
>>> for x in range(21,2,-2):
	print(x)

21
19
17
15
13
11
9
7
5
3
>>> #it will always print 1 digit lesser than the specified value eg if 2 then it will print till 3
>>> a="Hello world"
>>> for x in a:
	print(x)

H
e
l
l
o
 
w
o
r
l
d
>>> #prints each letter of string
>>> for x in a:
	if x=='0':
		break
	else:
		print(x)

H
e
l
l
o
 
w
o
r
l
d
>>> for x in a:
	if x=='o':
		break
	else:
		print(x)

H
e
l
l
>>> for x in a:
	if x=='o':
		continue
	else:
		print(x)

H
e
l
l
 
w
r
l
d
>>> #taking input from user
>>> a=input()
welcome people
>>> ashutosh
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    ashutosh
NameError: name 'ashutosh' is not defined
>>> a=input("Enter string")
Enter string welcome people
>>> a
' welcome people'
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter no2
Enter no3
5
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter no1
Enter no2
Ener no:2.0
Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/first1.py", line 3, in <module>
    d=int(input("Ener no:"))
ValueError: invalid literal for int() with base 10: '2.0'
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter no1.0
Enter no2.0
Ener no:3
6.0
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter a number: 5199
count is 4
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter a number: 5199
count is 4
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter a number:1234555
Enter number which you want to trace:5

================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter a number:1233345
Enter number which you want to trace:3
The value  3 is repeated  3 times
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter total no of digits: 5
0
0
0
0
>>> 
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter total no of digits: 5
5
6
10
11
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter max limit : 10
0
1
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter max limit : 5
0
1
1
2
3
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter a number : 5
120
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter starting limit: 1
Enter ending limit :20
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter starting limit: 1 
Enter ending limit :10
>>> 1
1
>>> 1
1
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter starting limit: 1
Enter ending limit :5
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter starting limit: 1
Enter ending limit :10
2
3
4
5
6
7
8
9
10
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter starting limit: 1
Enter ending limit :10
3
4
5
6
7
8
9
10
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter starting limit: 1
Enter ending limit :10
5
6
7
8
9
10
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter starting limit: 1
Enter ending limit :10
3
4
5
6
7
8
9
10
>>> 
================= RESTART: C:/Users/Admin/Desktop/first1.py =================
Enter starting limit: 1
Enter ending limit :10
1
2
3
5
7
>>> 
