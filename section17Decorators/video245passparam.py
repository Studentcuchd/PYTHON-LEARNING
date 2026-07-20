import functools

def decor(greet):
    
    @functools.wraps(greet)
    def wrapper(num):
            return greet(num)
    return wrapper

@decor
def greet(num):
    for i in range(num):
        print("hi parag")
        
greet(3)