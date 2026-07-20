from abc import ABC, ABCMeta, abstractmethod


# class ABC(metaclass=ABCMeta):
#     pass
class vehicle(ABC):
    def __init__(self,brand):
        self.brand=brand
        
    @abstractmethod
    def start(self):
        print("Checking vehicle.....")
        
        
class car(vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        
    def start(self):
        super().start()
        print(f"{self.brand} car started")
        
class bike(vehicle):
    def __init__(self,brand):
        super().__init__(brand)
    
    def start(self):
        super().start()
        print(f"{self.brand} bike started")
        

car_obj=car("BMW")
bike_obj=bike("R15")

car_obj.start()
bike_obj.start()
        
    

