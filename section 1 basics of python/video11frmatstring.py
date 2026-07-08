name="parag"
age=10
print(f"hi {name} you age is {age}")
# f string


# reassign then check 
age=12
print(f"hi {name} you age is {age}")

# ab ek var leke check krte h 

name="parag"
greet=f"hie {name} wassup"

print(greet)

# no change in name 
name="rohan"
print(greet)

# write greet again 
greet=f"hie {name} wassup"
print(f"updated change {greet}")


# use of .format()

# 1st normal way

name="parag"
print("hello {}".format(name))

# 2nd multiple add using arguments
print("hello {name} age={age} place={place}".format(name="parag",age=20,place="karnal"))

# 3rd indexing
print("age={0} name={2} place={1}".format(10,"karnal","parag"))