from Repository.database import Database
from Model.internclass import Intern

class InternRepository:
    
    def __init__(self,database:Database) -> None:
        self.database=database
        self.connection=database.connection
        self.cursor=database.cursor
        

    def add_intern(self,intern:Intern) ->None:
        with self.connection:
            self.cursor.execute(
                """ 
                INSERT INTO interns(name,email) 
                VALUES(?,?)
                """,
                (intern.name,intern.email)
                )
            intern.intern_id=self.database.cursor.lastrowid

    def get_all_interns(self)->list[Intern]:
        
        interns_list=[]
        
        self.cursor.execute("""
        SELECT intern_id,name,email
        FROM interns
        """)
        intern_tuple_rows=self.database.cursor.fetchall()
        
        for intern_id,name,email in intern_tuple_rows:
            interns_list.append(Intern(
            name=name,
            email=email,
            intern_id=intern_id
        ))
        return interns_list