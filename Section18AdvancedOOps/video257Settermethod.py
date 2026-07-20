class Segment:
    def __init__(self,departure,destination):
        self.departure=departure
        self.destination=destination
        
        
class flight:
    def __init__(self,segment_list):
        self.segment_list=segment_list
        
        
    #donot want to show internal implementation
    
    @property
    def departure_point(self):
        return self.segment_list[0].departure
    
    #Change value using setter
    @departure_point.setter
    def departure_point(self,val):
        dest=self.segment_list[0].destination
        self.segment_list[0]=Segment(departure=val,destination=dest)
        
    def __repr__(self):
        list_flghts=[self.segment_list[0].departure,self.segment_list[0].destination]
        
        for i in self.segment_list[1:]:
            list_flghts.append(i.destination)
            
        return "->".join(list_flghts)
            

            
segment_obj1=Segment("Delhi","Chandigarh")
segment_obj2=Segment("Chandigarh","Australia")
segment_obj3=Segment("Australia","India")

flight_obj=flight([segment_obj1,segment_obj2,segment_obj3])


print(flight_obj)

print("\n")

print("Changing value using setter")

print("\n")

flight_obj.departure_point="mumbai"

print(flight_obj)


print("\n"," value getting ","\n")

print(flight_obj.departure_point)