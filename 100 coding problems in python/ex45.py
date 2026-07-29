import string

for i in string.ascii_lowercase:
    with open(f"{i}.txt","w") as writer:
        writer.write(i+"\n")
    