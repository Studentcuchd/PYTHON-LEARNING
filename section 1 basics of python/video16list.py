list1=[1,2,3,4,"parag"]
print(list1)

list2_nested=[[1,2000],[2,1000],[3,10000]]
print(list2_nested)

print(f"length of both strings={len(list1)} and nested={len(list2_nested)}")

list1.append(5)
print(list1)
list2_nested.append([4,1090])
print(list2_nested)
list2_nested.append(3)
print(list2_nested)


# remove method
list1.remove("parag")
print(list1)
list2_nested.remove([4,1090])
print(list2_nested)

list2_nested.remove([2,1000])
print(list2_nested)