def divide(dividend,divisor):
    if divisor==0:
        raise ZeroDivisionError("This is error")
    return dividend/divisor

total=1
def multiplication(*args):
    if len(args)==0:
        raise ValueError(f"You are having 0 elements")
    else:
        for i in args:
            total=total*i
            
    return total