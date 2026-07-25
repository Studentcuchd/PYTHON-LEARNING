import functools

def outer(fun):
    @functools.wraps(fun)
    def wrapper():
    
        """  
        wrapper fun doc
        """
    
        print("hii this is wrapper")
        return fun()
    return wrapper


#the fun that you want to pass write @above

@outer
def passing_fun():
    
    """  
    Passing fun doc using wrap tool 
    """
    return f"This is passing fun"

print(passing_fun())

print(passing_fun.__name__)
print(passing_fun.__doc__)



