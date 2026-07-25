class Mentor:
    def __init__(self,
        name : str,
        email :str, 
        expertise :set[str],
        mentor_id :int|None=None
        ) ->None:
        
        self.name=name 
        self.email=email
        self.expertise=expertise 
        self.mentor_id=mentor_id
        
        
    def add_skill(self, skill : str)->None:
        self.expertise.add(skill.strip().lower())
    