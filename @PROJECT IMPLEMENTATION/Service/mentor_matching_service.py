from Repository.mentor_repository import MentorRepository
from Repository.problem_repository import ProblemRepository


class MentorMatchingService:
    def __init__(self,mentor_repository:MentorRepository,problem_repository:ProblemRepository) ->None:
        
        self.mentor_repository=mentor_repository
        self.problem_repository=problem_repository
            
    
    
    def find_matching_mentors(self,problem_id: int) ->list[dict]:
        problems=self.problem_repository.get_all_problems()
        mentors=self.mentor_repository.get_all_mentors()
        
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
                       "matched_skills":matched_skills,
                       "total_required_skills": len(entered_problem.req_skill)
                   }
               )
               
        matching_mentors.sort(lambda match : match['score'],reverse=True)
        return matching_mentors