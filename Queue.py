# program to implement queue data structure

class Queue:
    q = []
    front = -1
    rear = -1
    MAX = 5
    @classmethod
    def insert(cls,num):
        if(cls.rear == cls.MAX -1):
            print("overflow!")
        elif(cls.front == -1 and cls.rear == -1):
            cls.front = cls.rear = 0
            cls.q.append(num)
        else:
            cls.rear += 1
            cls.q.append(num)
        
    @classmethod    
    def delete(cls):
        if(cls.front == -1 or cls.front>cls.rear):
            print("underflow")
        else:
            val = cls.q[cls.front]
            cls.front += 1
            if(cls.front > cls.rear):
                cls.front = cls.rear = -1
            return val
    
    @classmethod
    def display(cls):
        if(cls.front == -1 or cls.front > cls.rear):
            print("Queue is empty")
        else:
            for i in range(cls.front,cls.rear +1):
                print(cls.q[i])
    
obj = Queue()            
while(1):
    print("1: Insert")
    print("2: Delete")
    print("3: Display")
    print("4: Exit")
    choice = int(input("Enter choice :"))
    if(choice == 1):
        num = int(input("Enter number to be inserted :"))
        obj.insert(num)
        
    elif(choice == 2):
        val = obj.delete()
        print("Deleted element : {}".format(val))
        
    elif(choice == 3):
        obj.display()
    
    elif(choice == 4):
        exit()