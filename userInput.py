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
    sum = 0
    for i in args:
        sum += i
    return sum
    
out = add(1,2)
print("soulution: ", out)