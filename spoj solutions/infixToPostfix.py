# program to convert an infix expression to postfix
# for this we are going to use stack data structure
# lets define a class that will simulate stack data structure

class StackDs:
    stack=[]
    top=-1  # currently top is pointing at -1 i.e. stack is empty
    def push(self,data):
        if(StackDs.top > 10):
            print("Stack overflow!")
        else:
            StackDs.top += 1    # incremented top by 1
            StackDs.stack.append(data)     #pushed the data into stack
        
    def pop(self):
        if(StackDs.top == -1):
            print("Stack underflow!")
        else:
            x= StackDs.stack.pop()
            # x holds the value that is to be popped
            # pop() deletes the last element of list permanently
            
            StackDs.top -= 1
            # decremented top by 1
            return x
    

def priority(op):
    # this function returns the priority of each operator
    if(op=='*' or op=='/' or op=='%'):
        return 1
    elif (op =='+' or op == '-'):
        return 0
    elif (op=='^'):
        return 2;

# let's create an object of class StackDs
ds=StackDs()    # object created

# program to evaluate infix to postfix
# we need two strings i.e. the infix and the postfix

infixExpression = input("Enter an infix expression : ").split(' ')
# we have converted the entered string into a list

#now create a empty list called postfix 
postfix=[]

for val in infixExpression:
    
    if(val == '('):
        ds.push(val)    # pushed the obening bracket blindly
        
    elif(val == ')'):
        while(StackDs.stack[StackDs.top] != '('):
            poppedItem = ds.pop()
            postfix.append(poppedItem)

        poppedItem = ds.pop()   # this statement ensures that '(' brace in stack gets removed
        # and place it outside the loop so that the loop condition won't get changed each time
        
              
    elif(val == '+' or val=='-' or val=='*' or val=='%' or val=='/' or val == '^'):
        if(StackDs.top == -1):  # if the stack is empty
            ds.push(val)
        elif(StackDs.stack[StackDs.top] == '('):
            ds.push(val)
        
        elif(priority(val)) < (priority(StackDs.stack[StackDs.top])):
            poppedItem = ds.pop()
            postfix.append(poppedItem)
            
        elif(priority(val)) >= priority(StackDs.stack[StackDs.top]):
            ds.push(val)
         
    else:
        postfix.append(val)
        
    print(postfix)
   
print(StackDs.top)     

while(StackDs.top != -1):
    #i.e. if the stack is not empty
    # then empty it by poping the elements of stack
    if(StackDs.stack[StackDs.top] == ')'):
        poppedItem=ds.pop()
    else:
        poppedItem=ds.pop()
        postfix.append(poppedItem)

result = ' '.join(postfix)
print(result)
    
    
    
    