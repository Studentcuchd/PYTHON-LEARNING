class calculate_avg:
    def __init__(self,name):
        self.name=name
        self.salary=[]
        
    @property
    def avg_sal(self):
        return sum(self.salary)/len(self.salary)
    
obj_parag=calculate_avg("Parag")
obj_parag.salary.append(1000)
obj_parag.salary.append(1000)

print(obj_parag.name)
print(obj_parag.avg_sal)