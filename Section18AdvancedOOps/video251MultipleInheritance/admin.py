from user import userdetail
from databasefile import database
from savetodb import savtodatabase
class admin_class(userdetail,savtodatabase):
    def __init__(self,username,password,access):
        super().__init__(username,password)
        self.access=access
        
    def __repr__(self):
        return f"Admin {self.username} , access {self.access}"
    
    def dict_convert(self):
        return {
            "username":self.username,
            "Password":self.password,
            "Access": self.access
        }
        

        