d = {"a": 1, "b": 2, "c": 3}
dict1={}
for key,val in d.items():
    if val<=1:
        dict1[key]=val
        
print(dict1)


d=dict((key,val) for key,val in d.items() if val<=1)
print(d)
