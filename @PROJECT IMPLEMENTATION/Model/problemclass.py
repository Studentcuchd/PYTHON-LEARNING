class Problem:
    def __init__(self,
        title :str,
        description :str,
        req_skill : set[str],
        intern_id : int,
        problem_id :int|None=None        
) ->None:
        self.title=title
        self.description=description
        self.req_skill=req_skill
        self.intern_id=intern_id
        self.problem_id=problem_id

        


