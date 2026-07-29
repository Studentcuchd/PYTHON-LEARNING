

a=["1", 1, "1", 2]
result=[]
[result.append(x) for x in a if x not in result]

print(result)


print(list(set(a)))