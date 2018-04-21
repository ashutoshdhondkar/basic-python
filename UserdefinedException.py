# program to study userdefined exception
class MyException(Exception):   # inherited from Exception class
    def __init__(self):
        self.message = " Number is same "

class valueLarge(MyException):
    def __init__(self):
        self.message = "Value too large"

class valueSmall(MyException):
    def __init__(self):
        self. message = "Value too small"


num = 10

try:
    ip = int(input("Enter an integer : "))
    if(ip < num):
        raise valueSmall # raise the exception
    elif(ip > num):
        raise valueLarge
    else:
        raise MyException
except valueSmall as e:
    print(e.message)

except valueLarge as e:
    print(e.message)

except MyException as e:
    print(e.message)
