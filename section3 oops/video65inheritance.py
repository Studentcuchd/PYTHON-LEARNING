class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.salary=[]
        
    def total_earn(self):
        return sum(self.salary)
# suppose i want to add my leave
class child(parent):
    def __init__(self,name,age,leave):
        super().__init__(name,age)
        self.leave=leave
        

childobj1=child("Parag",18,10)
childobj1.salary.append(10000)

print(childobj1.salary)
print(childobj1.name)
print(childobj1.leave)