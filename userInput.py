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