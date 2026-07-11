class custom_car_error(TypeError):
    def __init__(self,message,code):
        super().__init__(f"Error is {message} , with code = {code}")
        self.code=code
            
        
class Garge_parent():
    def __init__(self,name,model):
        self.name=name 
        self.model=model
        
    def __repr__(self):
        return f"Car{self.name},{self.model}"
        

class car:
    def __init__(self):
        self.car_list=[]
        
    def __len__(self):
        return len(self.car_list)
    
    def add_car(self,cars_obj):
        if not isinstance(cars_obj,Garge_parent):
            raise custom_car_error(message="Enter you car object",code=2001)
        self.car_list.append(cars_obj)
    

parent_obj=Garge_parent("BMW","2021")

try:
    car_obj=car()
    car_obj.add_car(parent_obj)
    
    # for error use 
    # car_obj.add_car("fiesta")
    
    
    print(len(car_obj))
except custom_car_error as e:
    print(e)
finally:
    print("full code")