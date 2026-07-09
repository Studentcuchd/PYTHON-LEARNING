list1=[1,2,3,4,5]
a,*b,c=list1
print(a)
print(*b)
print(c)

# normal way to print list of uple
detail=[("parag",25),("annie",18)]
for i in detail:
    print(i)
    
# list and tuple using destructuring

detail=[("parag",25),("annie",18)]
for name,age in detail:
    print(name,age)

    
