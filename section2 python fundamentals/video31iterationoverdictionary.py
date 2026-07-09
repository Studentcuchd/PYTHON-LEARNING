detail= {
    "rolf":25,
    "parag":21,
    "Rohan":20
}

print(detail["rolf"])


# iteration over keys
for key in detail:
    print(key)
    
# iteration over values
for value in detail.values():
    print(value)
    
# key and value
for key,value in detail.items():
    print(key,value)
    
    
# using while loop
details_while={
    "rolf":25,
    "parag":21,
    "Rohan":20
}
print("while loop key print")
# print key
key=list(details_while.keys())

i=0
while i<len(key):
    print(key[i],":",details_while[key[i]])
    i=i+1
  
  

print("printing values") 
# print values
i=0
value=list(details_while.values())
while i<len(value):
    print(value[i])
    i=i+1
    
    
print("ey value printing")
i=0
items=list(details_while.items())

while i<len(items):
    key,value=items[i]
    print(key,":",value)
    i=i+1