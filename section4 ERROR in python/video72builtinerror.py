# index error
list1=[1,2,3]
print(list1[5])


# keyerror
dict1={
    "Name":"Parag",
    "age":16
}

print(dict1["Salary"])



# Name error
print(nameerror)


#  Attribute error
list1=[1,2,3,4]
list2=[3,4,5]
list1.intersection(list2)


# # not implemented error
class error_check:
    def __init__(self,name):
        self.name=name
    def display(self):
        raise NotImplemented("This is a error featre not there")
    
obj1=error_check("Parag")
obj1.display()


# TabError
def fun():
	return "Hello"   # <-- This line starts with a TAB

    print("World")   # <-- This line starts with 4 SPACES



# type error
print("5"+2)



# Value error
a=int("abx")
