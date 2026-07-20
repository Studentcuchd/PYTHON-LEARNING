# user={
#     "username":"Parag",
#     "pass":12345
# }
# class mycustomerror(ValueError):
#     def __init__(self):
#         super().__init__("Not authenticated user")
 
 
# # decorator
   
# def outerfun(fun):
#     if user.get("username")=="Parag" and user.get("pass")==12345:
#         return fun
#     raise mycustomerror

# def fun():
#     return "Hi admin you are back"

# running_fun=outerfun(fun)
# print(running_fun())






# #-------------------Anther example---------------

user={
    "username":"Decor",
    "pass":123456
}
class mycustomerror(ValueError):
    def __init__(self):
        super().__init__("Not authenticated user is detected")
 
 
# decorator
   
def outerfun1(fun):
    def decofun():
        if user.get("username")=="Decor" and user.get("pass")==123456:
            return fun()
        raise mycustomerror
    return decofun

def fun():
    return "Hi admin you are back"


# running fun = decofun ke 
running_fun1=outerfun1(fun)
print(running_fun1())





