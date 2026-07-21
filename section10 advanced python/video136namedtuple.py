from collections import namedtuple

named_tuple=namedtuple("named_tuple",["name","age"])

tuple_val=named_tuple("Parag",19)

print(tuple_val.name)
print(tuple_val.age)

