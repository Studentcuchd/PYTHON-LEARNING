def fun_name(name):
    print(f"your name is ={name}")

fun_name("parag")


# default arguments 
def def_arg(name="Default vale"):
    print(f"hi {name}")
    
def_arg("parag")
def_arg()


# keyword paragmeter
def key_para(name,age):
    print(f"your name {name} and age {age}")
    
key_para(age=18,name="Parag")
key_para(18,"Parag")