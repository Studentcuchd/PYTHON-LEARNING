tuple1=(1,2,3,4,5)
tuple2=(5,)

# adding item directly not possible two ways

# using list
print(f"befor={tuple1}")

list1=list(tuple1)
list1.append(6)
tuple1=tuple(list1)
print(f"after update={tuple1}")


# using tuple addition
tuple1+=tuple2
print(f"adding tuple+tuple={tuple1}")