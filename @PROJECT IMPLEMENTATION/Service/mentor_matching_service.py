from Repository.database_manager import DataBaseManager

class MentorMatchingService:
    def __init__(self,database : DataBaseManager) ->None:
        
        self.database=database  
    
    def find_matching_mentors(self,problem_id: int) ->list[dict]:
        problems=self.database.get_all_problems()
        mentors=self.database.get_all_mentors()
        
        entered_problem=None
        for problem in problems:
            if problem.problem_id==problem_id:
                entered_problem=problem
                break
        
        if entered_problem is None:
            return []
        
        matching_mentors=[]
        for mentor in mentors:
           matched_skills=entered_problem.req_skill & mentor.expertise
           score=len(matched_skills)
           
           if score>0:
               matching_mentors.append(
                   {
                       "mentor":mentor,
                       "score":score,
                       "matched_skills":matched_skills
                   }
               )
               
        matching_mentors.sort(
            key=lambda match : match['score'],
            
            reverse=True
        )
        return matching_mentors