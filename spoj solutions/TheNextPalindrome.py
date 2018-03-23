# a number k is given as an input
# output the next smallest palindrome larger than k

def isPalindrome(num):
    val=num     # copy the number into val
    rev=0;
    while(val!=0):
        rev = rev * 10 + (val%10)
        val = val //10
    if(rev == num):
        return True
    else:
        return False


def NextSmallestPalindrome(num):
    while(1):
        num += 1
        if(isPalindrome(num)):
            break
    return num
            
    

testCases = int(input("Enter a number of test Cases: "))

l=[int(x) for x in input("Enter numbers : ").split(' ')]
print("\n")
for x in l:
    print(NextSmallestPalindrome(x))
    
