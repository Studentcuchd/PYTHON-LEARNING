list1=[1,2,3,4,5,6,7]
even=[i for i in list1 if i%2==0]

print(even)


# name matching

input_string=input("enter name=")
string_list=["Parag","Rohan","Vishal"]
lower_letter=[i.lower() for i in string_list]
if input_string.lower() in lower_letter:
    print(f"yes {input_string.upper()} exist in list")
else:
    print("not exist")




# extra 

# tuple comprehension  not possible simply we get generator and then we convert it into tuple
tuple1=(1,2,3,4,5)
tuple_new_gen=(i*i for i in tuple1)
print(tuple_new_gen)  #generator object bnjega

tuple_convert_gen=tuple(i*i for i in tuple1)
print(tuple_convert_gen)


