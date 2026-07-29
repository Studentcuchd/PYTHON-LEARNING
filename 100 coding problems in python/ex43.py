import string
with open("ex43.txt","w") as writer:
    for i,j in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]):
        writer.write(i+j+"\n")