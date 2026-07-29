import string
list_ans=[]
string1="python"
for i in string.ascii_lowercase:
    with open(f"{i}.txt","r") as reader:
        letter=reader.read().strip("\n")
        if letter in string1:
            list_ans.append(letter)


print(list_ans)