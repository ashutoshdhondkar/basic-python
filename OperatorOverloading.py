class Arithmetic:
    def __init__(self,num):
        self.num = num
    
    def __add__(self,obj):
        return (self.num + obj.num)
    
    def __sub__(self,obj):
        return (self.num - obj.num)
    
    def __mul__(self,obj):
        return (self.num * obj.num)
    
    def __truediv__(self,obj):
        return (self.num / obj.num)


obj1 = Arithmetic(10)
obj2 = Arithmetic(20)

print("\n Addition : {} ".format(obj1 + obj2))
print("\n Subtraction : {}".format(obj1 - obj2))
print("\n Multiplication : {}".format(obj1 * obj2))
print("\n Division : {} ".format(obj1 / obj2))