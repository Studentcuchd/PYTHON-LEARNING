d = {"a": 1, "b": 2, "c": 3}
sum1=0
for i in d.values():
    sum1+=i
    
print(sum1)

print(sum(d.values()))