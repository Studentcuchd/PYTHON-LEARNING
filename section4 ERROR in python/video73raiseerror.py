class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
        
    # we are creating repr because we are using the obj of this in my second class
    def __repr__(self):
        return f"Car{self.name},{self.model}"
        
class detail:
    def __init__(self):
        self.cars_list=[]
        
    def __len__(self):
        return len(self.cars_list)
        
    def add_car(self,cars):
        if not isinstance(cars,car):
            raise TypeError(f"Car `{cars.__class__.__name__}` object hi add hoga")
        self.cars_list.append(cars)
        

# this will give type error because we donot have any car created yet
car_obj=detail()
car_obj.add_car("bmw")


# create_car_obj=car("BMW","MODEL-2021")
# add_car_obj=detail()
# add_car_obj.add_car(create_car_obj)
# print(len(add_car_obj))
