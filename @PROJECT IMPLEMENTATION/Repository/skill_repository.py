from Repository.database import Database


class SkillRepository:

    def __init__(self, database: Database) -> None:
        self.database = database
        
        self.connection=database.connection
        self.cursor=database.cursor
        

    def get_or_create_skill(self, skill_name: str) -> int:
        skill_name = skill_name.strip().lower()

        with self.connection:

            self.cursor.execute(
                """
                SELECT skill_id
                FROM skills
                WHERE skill_name = ?
                """,
                (skill_name,)
            )

            skill_row = self.cursor.fetchone()

            if skill_row:
                return skill_row[0]

            self.cursor.execute(
                """
                INSERT INTO skills(skill_name)
                VALUES(?)
                """,
                (skill_name,)
            )

            return self.cursor.lastrowid