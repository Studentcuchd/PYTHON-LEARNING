from collections import defaultdict

my_company="watchgaurd"
list_myemp=["Karan","Lalit"]

other_emp=[("Parag","Apple"),("Rohan","Google")]

new_dict_emp=defaultdict(lambda:my_company)

for name,place in other_emp:
    new_dict_emp[name]=place
    
for i in list_myemp:
    new_dict_emp[i]
    
for key,val in new_dict_emp.items():
    print(f"{key} works at {val}")
    
