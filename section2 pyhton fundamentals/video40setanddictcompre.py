# set comprehension
set1={1,2,3,4,5}
set_new={i*i for i in set1}
print(set_new)

# dict comprehension

dict1={
    "Parag":18,
    "rohan":20
}
#swap key value
new_dict={value:key for key,value in dict1.items()}
print(new_dict)


# dict using list count frequency
list1=[1,2,3,4,5,5,1,2,3,5,6]
freq={i:list1.count(i) for i in list1}
print(freq)




# set comprehension code
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# find common using set
friend_set={name.lower() for name in friends}
guets_set={name.lower() for name in guests}

intersection_set=friend_set.intersection(guets_set)
print(intersection_set)

# i want each in uppercase
uppercase_set={i.upper() for i in intersection_set}
print(uppercase_set)