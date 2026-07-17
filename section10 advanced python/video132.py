acc={
    "checking":100.30,
    "saving":100.50
}
#typing

def add_balance(amount:float,type="checking")->float:
    acc[type]+=amount
    return acc[type]


add_balance(120.40)
print(acc["checking"])

add_balance(200,"saving")
print(acc["saving"])