reader=open("section5 Filehandling/textfiles/video86_csv_data.txt","r")
csv_reader=reader.readlines()

print(csv_reader)

# here i got some \n after each line so to remove this we use strip

line_stripping=[line.strip() for line in csv_reader]

# ab back slash n ht gya hoga 

print(line_stripping)


# ab hume name age uni first heading remove krni h
# ṭo we use [1:] slicing
line_stripping=line_stripping[1:]
print(line_stripping)


# print line by line here we have a lot of , so we use split for this
for i in line_stripping:
    line_by_list=i.split(",")  #meri first line aagyi
    name=line_by_list[0]
    age=line_by_list[1]
    university=line_by_list[2]
    degree=line_by_list[3]
    print(f"Your name {name} and you are {age} y/0 studying in {university} and degree {degree}")    
    
    
# add data to a csv file
list_data=["Parag",18,"Cu","Computer science"]
with open("section5 Filehandling/textfiles/video86_csv_data.txt","a") as writer_csv:
    writer_csv.write(",".join(list_data))