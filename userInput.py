#---------------------------------------------------------------
#a program that changes the europe lift convention to that of USA
inp = input("what is your Europe lift destination: ")
try:
    UsDest = int(inp) + 1
        
except:
    UsDest = -1
    
print("Your destination is: ", UsDest)

if UsDest == -1:
    print("Wrong Value")
    
#------------------------------------------------------
def add(*args):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_
    
out = add(1,2,3,4,5,6,7,8,9)
print("soulution: ", out)