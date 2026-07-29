import string
with open("ex44.txt","w") as writer:
    for i,j,k in zip(string.ascii_lowercase[0::3],string.ascii_lowercase[1::3],string.ascii_lowercase[2::3]):
        writer.write(i+j+k+"\n")