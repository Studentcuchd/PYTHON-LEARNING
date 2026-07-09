list1=[1,2,3,4,5]
list2=[100,200,300,400,500]

tuple1=(2000,1000,2000,3000,4000)

tuple2=(1,2,3,4,5,6,7,8)

new_list=list(zip(list1,list2))
print(new_list)

new_tuple=tuple(zip(list1,list2,tuple1))
print(new_tuple)


new_dict=dict(zip(list1,list2))
print(new_dict)


new_set=set(zip(tuple2,new_tuple))
print(new_set)


# transpose of matrix
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

tranpose_matrix=list(zip(*matrix))
print(tranpose_matrix)


