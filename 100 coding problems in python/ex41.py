import string
with open("ex41.txt","w") as writer:
    for i in string.ascii_lowercase:
        writer.write(i +"\n")