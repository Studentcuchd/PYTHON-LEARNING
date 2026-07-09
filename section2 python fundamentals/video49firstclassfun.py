def fun():
    print("Hello")
    
variable_fun=fun
variable_fun()

# operation of grades avg total and top

avg=lambda marks: sum(marks)/len(marks)
top=lambda marks:max(marks)
total=lambda marks:sum(marks)

operations={
    "average":avg,
    "top":top,
    "total":total
}

marks=[
    [1,2,3,4,5],
    [3,4,5,6,7],
    [6,7,8,6,5]
]

for i in marks:
    op=input("enter operation=")
    operations_firstclass_fun=operations[op]
    print(operations_firstclass_fun(i))
