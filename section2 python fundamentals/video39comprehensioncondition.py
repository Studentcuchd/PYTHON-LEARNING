list1=[1,2,3,4,5,6,7]
even=[i for i in list1 if i%2==0]

print(even)

# nested list

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

common_list=[
    i.upper()
    for i in guests
    if i.lower() in [j.lower() for j in friends]
]
print(common_list)

