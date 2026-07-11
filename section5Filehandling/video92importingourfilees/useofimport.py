import fileoperations
list1=["Parag","Rohan"]
fileoperations.write_to_file(str(list1),"importing92.txt")

print(fileoperations.readfile("importing92.txt"))
