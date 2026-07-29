import string
list_ans=[]
for i in string.ascii_lowercase:
    with open(f"{i}.txt","r") as reader:
        list_ans.append(reader.read().strip("\n"))


print(list_ans)