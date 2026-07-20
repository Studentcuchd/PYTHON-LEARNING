class database:
    content={"users":[]}
    
    @classmethod
    def add_data(cls,data):
        cls.content['users'].append(data)
        
    @classmethod
    def remove(cls,finder):
        cls.content['users']=[i for i in cls.content['users'] if not finder(i)]
        
    @classmethod
    def find_user(cls,finder):
        return [i for i in cls.content['users'] if finder(i)]