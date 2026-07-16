import time
from concurrent.futures import ThreadPoolExecutor

def greeting(names):
    return f"Hi {names}"


list_names=["Parag","Rohan","Mayank"]

# without with statement

executor=ThreadPoolExecutor(max_workers=3)
submit=executor.map(greeting,list_names)

for i in submit:
    print(i)
    
    
    
def print_detail1(username,passw):
    return f"Username={username} , password={passw}"

with ThreadPoolExecutor(max_workers=1) as executor:
    result_v=executor.submit(print_detail1,"Parag.Bajaj","Parag@98")
    print(result_v.result())
    
    
    
