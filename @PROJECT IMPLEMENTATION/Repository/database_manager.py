import sqlite3


from Model.internclass import Intern
from Model.mentorclass import Mentor
from Model.problemclass import Problem


class DataBaseManager:
  
  def __init__(self,db_name):
    self.connection=sqlite3.connect(db_name)
    self.connection.execute("PRAGMA foreign_keys = ON")
    self.cursor=self.connection.cursor()    
    self.create_tables() 
    
  def create_tables(self) ->None:
    with self.connection:
      self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS interns(
          intern_id INTEGER PRIMARY KEY AUTOINCREMENT, 
          name TEXT NOT NULL,
          email TEXT NOT NULL UNIQUE);                      
      """)
      
      self.cursor.execute("""  
        CREATE TABLE IF NOT EXISTS mentors(
          mentor_id INTEGER PRIMARY KEY AUTOINCREMENT, 
          name TEXT NOT NULL,
          email TEXT NOT NULL UNIQUE
      );                             
                          
      """)
      
      self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS skills(
          skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
          skill_name TEXT NOT NULL UNIQUE 
      );
      """)
      
      self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS problems(
          problem_id INTEGER PRIMARY KEY AUTOINCREMENT,
          intern_id INTEGER NOT NULL,
          title TEXT NOT NULL,
          description TEXT NOT NULL,
          
          FOREIGN KEY(intern_id) REFERENCES interns(intern_id) 
      );
      """)
      self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS mentor_skills(
          skill_id INTEGER NOT NULL,
          mentor_id INTEGER NOT NULL,
          
          PRIMARY KEY(skill_id,mentor_id),
          
          FOREIGN KEY (skill_id) REFERENCES skills(skill_id),
          FOREIGN KEY (mentor_id) REFERENCES mentors(mentor_id)
      );
      """)
      
      self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS problem_skills(
          skill_id INTEGER NOT NULL,
          problem_id INTEGER NOT NULL,
          
          PRIMARY KEY(skill_id,problem_id),
          
          FOREIGN KEY (skill_id) REFERENCES skills(skill_id),
          FOREIGN KEY (problem_id) REFERENCES problems(problem_id)
      );
      """)
    
    
      
  def add_intern(self,intern:Intern) ->None:
    with self.connection:
      self.cursor.execute(
        """ 
        INSERT INTO interns(name,email) 
        VALUES(?,?)
        """,
        (intern.name,intern.email)
        )
      intern.intern_id=self.cursor.lastrowid
  
  
          
  def get_or_create_skill(self,skill_name :str)->int:
    skill_name=skill_name.strip().lower()
    
    self.cursor.execute("""
        SELECT skill_id FROM skills
        WHERE skill_name=?
        """,
        (skill_name,))
    skill_row=self.cursor.fetchone()
    if skill_row:
        return skill_row[0]
  
    self.cursor.execute(""" 
        INSERT INTO skills(skill_name) 
        VALUES (?)
        """,
        (skill_name,)
        )
    return self.cursor.lastrowid
  
  
  
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
        skill_id=self.get_or_create_skill(skill)
        self.cursor.execute(""" 
          INSERT INTO mentor_skills(skill_id,mentor_id)
          VALUES(?,?)
          """,
          (skill_id,mentor.mentor_id))
    
  
  
  def add_problem(self,problem:Problem)->None:
    with self.connection:
      self.cursor.execute(""" 
         INSERT INTO problems(intern_id,title,description) 
         VALUES(?,?,?)                
        """,
        (problem.intern_id,problem.title,problem.description))
      problem.problem_id=self.cursor.lastrowid
      
      for skill in problem.req_skill:
        skill_id=self.get_or_create_skill(skill)
        
        self.cursor.execute(""" 
          INSERT INTO problem_skills(skill_id,problem_id)
          VALUES(?,?)                 
          """,
          (skill_id,problem.problem_id) )
  
  
  def close(self) ->None:
    self.connection.close() 
  
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
  
  
  def get_all_interns(self)->list[Intern]:
    
    interns_list=[]
    
    self.cursor.execute("""
      SELECT intern_id,name,email
      FROM interns
      """)
    intern_tuple_rows=self.cursor.fetchall()
    
    for intern_id,name,email in intern_tuple_rows:
      interns_list.append(Intern(
        name=name,
        email=email,
        intern_id=intern_id
      ))
    return interns_list
    
  
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
  
    
    