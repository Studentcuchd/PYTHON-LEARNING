acc={
    "checking":900.4,
    "saving":203.4
}

def add_bal(amount,type):
    acc[type]+=amount
    return acc[type]

transction=[
    (-102.2,"checking"),
    (202.2,"checking"),
    (-220.2,"checking"),
    (102.2,"checking"),
    (-109.2,"checking"),
    (600.2,"checking")
]
for i in transction:
    # a=i[0]
    # b=i[1]
    # print(add_bal(a,b))
    
    # alternative way
    print(add_bal(*i))
    
class users:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    def __repr__(self):
        return f"Username:{self.username} , Password:{self.password}"
    
user_list=[
    {"username":"parag.bajaj","password":"Parag@watch"},
    {"username":"deepika","password":"deepika@google"} 
]


# user_data=[users(i["username"],i["Password"]) for i in user_list]    

user_data=[users(**i) for i in user_list]
for i in user_data:
    print(i)