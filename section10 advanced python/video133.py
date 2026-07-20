# using default mutable objects now jen is a hlder of ron also so it is a issue
def acc_detail(type:str,name:str,acc_holders=[]):
    print(id(acc_holders))
    acc_holders.append(name)
    
    return {
        "type":type,
        "name":name,
        "acc_holders":acc_holders
    }
    
a1=acc_detail("Checking","rolf")
print(a1)

a2=acc_detail("saving","jen")
print(a2)



# ways to fix it
print("way 1 no use of default values pass in argument")

def acc_detail1(type:str,name:str,acc_holders):
    print(id(acc_holders))
    acc_holders.append(name)
    
    return {
        "type":type,
        "name":name,
        "acc_holders":acc_holders
    }
    
a1=acc_detail1("Checking","rolf",[])
print(a1)

a2=acc_detail1("saving","jen",[])
print(a2)
    
# use NONE as a default value
 
print("way 2 none as a default value")

def acc_detail2(type:str,name:str,acc_holders=None):
    # if not acc_holders:
    if acc_holders is None:
        acc_holders=[]
    print(id(acc_holders))
    acc_holders.append(name)
    
    return {
        "type":type,
        "name":name,
        "acc_holders":acc_holders
    }
    
a1=acc_detail2("Checking","rolf")
print(a1)

a2=acc_detail2("saving","jen")
print(a2)