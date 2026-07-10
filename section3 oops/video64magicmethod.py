# len, str, repr, getitems

class garge:
    def __init__(self):
        self.cars=[]
        
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self,i):
        return self.cars[i]
    
    def __str__(self):
        return f"name of car is <<{self.cars}"
    
    def __repr__(self):
        return f"car detail is {self.cars}"
    
# by defining len and get items we can use for loop now

s1=garge()
s1.cars.append("BMW")
s1.cars.append("Lambo")
s2=garge()
s2.cars.append("Maruti")


# get items
print(s1[0])
print(s1[1])

# get len
print(len(s1))
print(len(s2))

# printing all cars
for i in s1:
    print(i)
    
    
#without  __str__  output <__main__.garge object at 0x0000022FD5DE6F90>
print(s1)

# use of repr
print(repr(s1))
