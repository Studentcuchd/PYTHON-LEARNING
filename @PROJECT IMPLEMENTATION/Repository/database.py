import sqlite3


class Database:
  
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
  def close(self)->None:
    self.connection.close()