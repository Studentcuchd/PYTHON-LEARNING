def fun(filename):
    str_list=[]
    with open(filename,"r") as reader:
        str_list=reader.read().replace(',' , ' ').split()

    return len(str_list)


filename="ex36.txt"

print(fun(filename))