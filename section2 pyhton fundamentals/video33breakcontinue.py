grades=["a","b","f","c+"]
print("break stop")
# break
for i in grades:
    if(i=="f"):
        print("stop this fail grade")
        break
    print(i)
    
print("continue skip ")
# continue is use to skip 
for i in grades:
    if(i=="f"):
        print("skipping fail grade")
        continue
    print(i)