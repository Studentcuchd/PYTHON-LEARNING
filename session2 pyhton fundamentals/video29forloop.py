# normal for loop
for i in range(10):
    print(i)
print("start from 4")
# start and stop
for i in range(4,10):
    print(i)
    
# start stop and step

print("odd form 1 to 10")
for i in range(1,10,2):
    print(i)
    

# for loop on list

print("list1")
list1=[1,2,3,4,5]
for i in list1:
    print(i)
    
# on dictionary
movie=[
    {"Ttile":"YJHD","Date":"28-09-2001"},
    {"Ttile":"WAR","Date":"28-09-2002"}
]

for i in movie:
    print(i["Ttile"])
    print(i["Date"])
    
    