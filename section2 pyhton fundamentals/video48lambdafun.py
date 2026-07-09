# def calc_avg(grades):
#     return sum(grades)/len(grades)

# using lambda
calc_avg=lambda grades:sum(grades)/len(grades)

grades=[
    [10,10,10,10],
    [9,9,9,9],
    [10,8,9,7]
]

for i in grades:
    print(calc_avg(i))
    
    
    
# map 
numbers = [1, 2, 3, 4, 5]
result=list(map(lambda x:x*x,numbers))
print(result)
    
    
# filter
numbers = [1, 2, 3, 4, 5]
odd_val=list(filter(lambda x:x%2!=0,numbers))
print(odd_val)

# sorted
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_list=sorted(students,key=lambda x:x[1])
print(sorted_list)

# sorted based on string length
words = ["apple", "pie", "banana", "cherry"]
sorted_ans=sorted(words,key=lambda x:len(x))
print(sorted_ans)

# reverse
words = ["apple", "pie", "banana", "cherry"]
sorted_ans=sorted(words,key=lambda x:len(x), reverse=True)
print(sorted_ans)