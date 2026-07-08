given_user="Parag"
input_user=input("enter your name=")

if given_user==input_user:
    print("login gurantee")
else:
    print("Unauthorized user")
    
# elif and nested if

a=10
if a>5:
    print("yes 5")

if a>9:
    print("yes 9")
    

a=20
if a>5 and a<25:
    print("in first if")    
elif a>19 and a>15:
    print("in elif")
else:
    print("hogya nhi else")