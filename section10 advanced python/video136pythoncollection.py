"""   

1. Counter
2. defaultdict
3. ordereddict
4. namedtuple
5. deque


"""

"""  

1. Counter -> count things 

counter(list)
just liek map count the values


You can think of it as a dictionary where:

item -> frequency


Counter Methods

1. update() -> Adds counts from another iterable or mapping. Existing counts increase and new elements are added


2. elements() -> Returns an iterator over elements repeating each as many times as its count. Elements are returned in arbitrary order.


3. most_common() -> Returns a list of the n most common elements and their counts from the most common to the least. If n is not specified, it returns all elements in the Counter.


4. subtract() -> Subtracts element counts from another iterable or mapping. Counts can go negative.



"""
from collections import Counter

list1=[1,2,3,4,53,2,1,3,4]
counting=Counter(list1)
print(counting)

text="me and you"
text_counter=Counter(text)
print(text_counter)

print(f"m= {text_counter['m']}")


# update
prev=[1,2,3]
new_l=[1,2,2]

prev_c=Counter(prev)

prev_c.update(new_l)
print(prev_c)


print(list(prev_c.elements()))


list_ctr=Counter([1,2,2,2,3,3,3,3,3,4,4])
common=list_ctr.most_common(3)  #most_common(number_val) 1 dala to 1 hi highest freq aayega 
print(common)


list_val=[1,1,1,2,2,3,4]
subtract_list=[1,2,3,4,4]

count_l1=Counter(list_val)
count_l1.subtract(subtract_list)
print(count_l1)



print("\n")
print("\n")

# Defaultdict
from collections import defaultdict

user_details=[("Parag","cu"),("Rohan","MIT"),("Mayank","DU"),("Deepika","cu")]


# new_list=[]


new_list=defaultdict(list)
for name,place in user_details:
    
    """  
    instead of this we use defaultdict
    
        if name not in new_list:
        new_list[name]=[]
    
    """

    new_list[name].append(place)


print(new_list["Parag"]) 


# give empty list but i want to throw an error

# new_list.default_factory=int  #0

new_list.default_factory=None  #error

new_list.default_factory=str #space

print(new_list["Annie"])