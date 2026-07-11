import json
with open("section5 Filehandling/textfiles/video89file.json","r") as reader_json:
    your_json_data=json.load(reader_json)
    

print(your_json_data)  #print whole data 
# index based search
# print(your_json_data["key"][0])





# writing a file in json
list_detail=[
    {
        "Name":"Parag",
        "age":16
    },
]

with open("section5 Filehandling/textfiles/video89writingfile","a") as file:
    json.dump(list_detail,file,indent=4)
    
    
    
# use of dumps and dump main difference

# dump 

diff_dump=[
    {
        "Name":"Parag",
        "age":16
    },
]

print("\n")

print("-------------------printing diff between dump and dumps----------")
with open("section5 Filehandling/textfiles/video89_dump","w") as file:
    result=json.dump(list_detail,file,indent=4)

print("dump return value=",result)
print("return value of dump_type=",type(result))


print("\n")
print("dumps")

diff_dumps=[
    {
        "Name":"Parag",
        "age":16
    },
]

with open("section5 Filehandling/textfiles/video89_dumps","w") as file:
    result=json.dumps(list_detail)

print("dumps return value=",result)
print("return value of dumps_type=",type(result))

