# class my_custom_error(Exception):
#     pass
# raise my_custom_error("My custom error")


# # my_custom_error()


# class my_custom_error(TypeError):
#     def __init__(self,message,code):
#         super().__init__(f"Error message: {message} with status code {code}")
#         self.code=code
        
        
# raise my_custom_error(message="This is the error",code=404)
        
        
        
#doc string 

class docstring_error(Exception):
    
    """
    This method is giving a particular code
    """
    def __init__(self,codes,messages):
        super().__init__(f"code={codes}, message={messages}")
        self.codes=codes
        
err= docstring_error(messages="This is message",codes=404)
# print doc string content
print(err.__doc__)