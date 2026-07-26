from Repository.database import Database
from Repository.skill_repository import SkillRepository
from Model.mentorclass import Mentor

class MentorRepository:
    def __init__(self,database : Database,skill_repository : SkillRepository)->None:
        self.database=database
        self.connection=database.connection
        self.cursor=database.cursor
        self.skill_repository=skill_repository
        
        
    def add_mentor(self,mentor:Mentor)->None:
        with self.connection:
            self.cursor.execute(""" 
                INSERT INTO mentors(name,email)
                VALUES(?,?)                                          
                """,
                (mentor.name,mentor.email)
                )
            mentor.mentor_id=self.cursor.lastrowid
        
            for skill in mentor.expertise:
                skill_id=self.skill_repository.get_or_create_skill(skill)
                self.cursor.execute(""" 
                INSERT INTO mentor_skills(skill_id,mentor_id)
                VALUES(?,?)
                """,
                (skill_id,mentor.mentor_id))

    def get_all_mentors(self)->list[Mentor]:
        self.cursor.execute(""" 
            SELECT mentor_id,name,email
            FROM mentors  
            """)     
        mentor_tuple_rows=self.cursor.fetchall()
        
        mentor_list_with_skills=[]
        
        for mentor_id,name,email in mentor_tuple_rows:
        
            self.cursor.execute(""" 
                SELECT skill_name
                FROM mentor_skills
                JOIN skills
                ON mentor_skills.skill_id=skills.skill_id        
                WHERE mentor_skills.mentor_id = ?
                """,
                (mentor_id,))
        
            skill_set={row[0] for row in self.cursor.fetchall()}
            
            mentor_list_with_skills.append(
                Mentor(
                name=name,
                email=email,
                expertise=skill_set,
                mentor_id=mentor_id
                
                )
            )
        return mentor_list_with_skills
        

