dict1={
    "a":[i for i in range(1,11)],
    "b":[i for i in range(11,21)],
    "c":[i for i in range(21,31)]
}


for key,value in dict1.items():
    print(f"{key} has values {value}")