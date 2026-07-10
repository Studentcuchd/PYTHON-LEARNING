class student:
    pass
s1=student()
s1.name="Parag"

print(s1.name)


# use of constructor __init__

class details: 
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=sum(marks)
    
    def getvalue(self):
        return self.name,self.age,self.marks
    
s1=details("Parag",18,[10,20,30,40])
print(s1.getvalue())

s2=details("rohan",20,[10,10,10,10,10])
print(s2.getvalue())


# to get only one value
print(s1.getvalue()[0])
