list1=[1,2,3,4,5]

for i,j in enumerate(list1):
    print(i,j)
    
       
# more examples
# we can create a list of this also
new_list=[(i,j) for i,j in enumerate(list1,start=1)]
print(new_list)


new_dict={i:j for i,j in enumerate(list1)}
print(new_dict)

new_list_test=[1,3,4,5,5]
print(list(enumerate(new_list_test,start=2)))