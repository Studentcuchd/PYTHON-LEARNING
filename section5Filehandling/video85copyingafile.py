# open using with 
with open("section5 Filehandling/textfiles/video85people.txt","r") as file_name:
    print(file_name.read())
file_name.close()


print("\n")
print("------------------------------------------------")
print("applying loops on this")
print("------------------------------------------------")
print("\n")
# loop on file
with open("section5 Filehandling/textfiles/video85people.txt","r") as file_name:
    for i in file_name:
        print(i)
file_name.close()



# task of this video main

# ask the user a list of 3 friends
# for each friend, we all tell the user wheter they are nearby?
# for each nearby friend, we will save their name to "nearby_friends.txt



# Ask the user for a list of 3 friends

list_friends=[]
i=0
while i<3:
    str_name=input(f"Enter {i} name=")
    list_friends.append(str_name)
    i+=1
    

    
# Save only nearby friends
    
with open("section5 Filehandling/textfiles/video85friend.txt","w") as file_friends:
    for i in list_friends:
        
        a=input(f"If {i} is nearby (yes/no):")
        if a.lower()=="yes":
            file_friends.write(i+"\n")
    
    
    
    
# store friends and people common in nearbyfriends file


# 1 make a list of your people file   # Read people from the file

people=open("section5 Filehandling/textfiles/video85people.txt","r")
list_people=people.read().splitlines()

people.close()


# but in file_friends ==  we have no space
friends = open("section5 Filehandling/textfiles/video85friend.txt", "r")
list_friends = friends.read().splitlines()   #another way is list comprehension list_friends = [i.strip() for i in friends.readlines()]
friends.close()

set_people=set(list_people)
set_friends=set(list_friends)

list_common_friends=list(set_people.intersection(set_friends))

write_nearby=open("section5 Filehandling/textfiles/video85nearby.txt","w")
for i in list_common_friends:
    write_nearby.write(i+"\n")

write_nearby.close()