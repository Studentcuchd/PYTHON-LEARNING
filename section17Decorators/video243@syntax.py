def outer(fun):
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
    Passing fun doc
    """
    return f"This is passing fun"

print(passing_fun())

