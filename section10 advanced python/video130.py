# Advanced python
dict={
    "Parag":10,
    "rolf":12
}
print(id(dict)) #136719835027648
print(id(dict)) #136719835027648
print(id(dict)) #136719835027648

dict["rolf"]=8
print(id(dict)) #136719283230912


print(id(dict["Parag"])) #11645640



age=10
print(id(age))

age+=10
print(id(age))

age=age+10
print(id(age))
