import functools

roles={
    "role":"admin"
}
def role_access(role):
    def outer(my_fun):
        @functools.wraps(my_fun)
        def wrapper(page):
            if role==roles.get("role"):
                return my_fun(page)
            
        return wrapper
    return outer
@role_access('admin')
def my_fun(page):
    return f"this is {page} dashboard"

print(my_fun('admin'))