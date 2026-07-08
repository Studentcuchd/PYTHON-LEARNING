dict1={
    "name":"parag","age":20,"salaray":1000
}
print(dict1)

# find of access using key
print(dict1["age"])

# add values 

dict1["location"]="karnal"
print(dict1)

# reassign
dict1["age"]=18
print(dict1)


# tuple of dictionary
tupple_dict=(
   {"name":"parag", "age":20},
   {"name":"Rohan", "age":90},
   {"name":"Kamal", "age":10}

)
print(tupple_dict)

# access value
print(tupple_dict[1]["name"])

# list to dict
list_items=[("parag",20),("rohan",18)]
dict_list=dict(list_items)
print(dict_list)