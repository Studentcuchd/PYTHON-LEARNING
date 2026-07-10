class details:
    # Class variable shared by everyone
    current_company="Watchguard"
    # instance method
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        print("Your name=",self.name)
        print("Salary=",self.salary)
        print("company=",self.company)
        
# class method
    @classmethod
    def change_name(cls,new_name):
        cls.current_company=new_name
    
    