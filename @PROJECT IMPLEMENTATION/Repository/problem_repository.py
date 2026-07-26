from Repository.database import Database
from Repository.skill_repository import SkillRepository
from Model.problemclass import Problem

class ProblemRepository:
    
    def __init__(self, databse: Database, skill_repository:SkillRepository) -> None:
        self.database=databse
        self.skill_repository=skill_repository
        
        self.connection=databse.connection
        self.cursor=databse.cursor
            
    def add_problem(self,problem:Problem)->None:
        with self.connection:
            self.cursor.execute(""" 
                INSERT INTO problems(intern_id,title,description) 
                VALUES(?,?,?)                
                """,
                (problem.intern_id,problem.title,problem.description))
            
            problem.problem_id=self.cursor.lastrowid
        
            for skill in problem.req_skill:
                skill_id=self.skill_repository.get_or_create_skill(skill)
                
                self.cursor.execute(""" 
                INSERT INTO problem_skills(skill_id,problem_id)
                VALUES(?,?)                 
                """,
                (skill_id,problem.problem_id) )
    def get_all_problems(self)->list[Problem]:
        self.cursor.execute(""" 
        SELECT problem_id,intern_id,title,description
        FROM problems
        """) 
        
        problems_rows=self.cursor.fetchall()
        
        problems_list=[]
        for problem_id,intern_id,title,description in problems_rows:
        
            self.cursor.execute(""" 
                SELECT skill_name FROM problem_skills
                JOIN skills
                ON problem_skills.skill_id=skills.skill_id
                WHERE problem_skills.problem_id = ? 
                """,
                (problem_id,))
            
            problem_set={row[0] for row in self.cursor.fetchall()}
            
            problems_list.append(
                Problem(
                title=title,
                description=description,
                req_skill=problem_set,
                intern_id=intern_id,
                problem_id=problem_id
                )
            )
        return problems_list