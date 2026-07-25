from Repository.database_manager import DataBaseManager
from Service.mentor_matching_service import MentorMatchingService

from Model.internclass import Intern
from Model.mentorclass import Mentor
from Model.problemclass import Problem


def print_menu() -> None:
    print("\n----------  Intern Mentor Matching System  ----------")
    print("1. Add Intern")
    print("2. Add Mentor")
    print("3. Add Problem")
    print("4. View Interns")
    print("5. View Mentors")
    print("6. View Problems")
    print("7. Find Matching Mentors")
    print("8. Exit")


def add_intern(database: DataBaseManager) -> None:
    name=input("enter your name=")
    email=input("enter you eamil=")
    intern_obj=Intern(name,email)
    database.add_intern(intern_obj)
    print("Intern Added successfully")



def view_interns(database: DataBaseManager) ->None:
    interns_list=database.get_all_interns()
     
    if not interns_list:
        print("No intern found Please add Intern")
        return
    
    print("\n------ Interns ------")
    
    for intern in interns_list:
        print(f"ID= {intern.intern_id}")
        print(f"Name= {intern.name}")
        print(f"Email= {intern.email}")
        
        print("**********************************************\n")
        

        
        
        

def add_mentor(database: DataBaseManager) -> None:
    name=input("enter your name=")
    email=input("enter you eamil=")
    
    skill_set=set()
    total_skills=int(input("Enter total number of skills you have="))
    print("......Enter your skills one by one......")
    for i in range(total_skills):
        skill_input=input(f"Enter your {i+1} skill=").strip()
        if skill_input:
            skill_set.add(skill_input)

    mentor_obj=Mentor(name,email,skill_set)
    database.add_mentor(mentor_obj)
    
    print("Mentor added successfully.")   
        


def view_mentors(database: DataBaseManager) -> None:
    mentor_list=database.get_all_mentors()
    
    if not mentor_list:
        print("No Mentor found Please add a mentor")
        return 
    
    print("\n------ Mentors ------")
       
    for mentor in mentor_list:
        print(f"ID= {mentor.mentor_id}")
        print(f"Name= {mentor.name}")
        print(f"Email= {mentor.email}")
        print(f"Skills= {','.join(mentor.expertise)}")
        print("**********************************************\n")

    
    
    
        

           

def add_problem(database: DataBaseManager) -> None:
    interns_list=database.get_all_interns()
    if not interns_list:
        print("No intern found Please add Intern")
        return
    
    view_interns(database)
    
    intern_id=int(input("Enter Your Intern ID="))
    
    valid_intern=False
    
    for intern in interns_list:
        if intern.intern_id==intern_id:
            valid_intern=True
            break
    
    if not valid_intern:
        print("Invalid Intern id")
        return
    
    title = input("Enter Problem Title= ").strip()
    description = input("Enter Problem Description= ").strip()
    
    required_skills=set()
    
    total_skills = int(input("Enter total required skills: "))
    
    print("\n")
    print("Enter required skills one by one")
    print("\n")
    
    for i in range(total_skills):
        skill=input(f"Enter {i+1} skill=").strip()

        if skill:
            required_skills.add(skill)
    
    
    problem_obj = Problem(
        title,
        description,
        required_skills,
        intern_id
    )

    database.add_problem(problem_obj)

    print("Problem added successfully.")




def view_problems(database: DataBaseManager) -> None:

    problem_list = database.get_all_problems()

    if not problem_list:
        print("No problems found.")
        return

    print("\n------ Problems ------")

    for problem in problem_list:
        print(f"Problem ID = {problem.problem_id}")
        print(f"Title= {problem.title}")
        print(f"Description= {problem.description}")
        print(f"Intern ID= {problem.intern_id}")
        print(f"Required Skills= {', '.join(problem.req_skill)}")
        print("**********************************************\n")


def find_matching_mentors(database :DataBaseManager, matching_service: MentorMatchingService) -> None:
    problem_list = database.get_all_problems()

    if not problem_list:
        print("No Problem posted right now please add problem")
        return   
    
    view_problems(database)
    problem_id=int(input("Pleease enter id of your problem="))
    
    matching_mentors_list=matching_service.find_matching_mentors(problem_id)
    
    if not matching_mentors_list:
        print("No match found")
        return
    
    print("\n***Matching Mentors***")
    
    for match in matching_mentors_list:
        
        mentor=match['mentor']
        print(f"Mentor id= {mentor.mentor_id}")
        print(f"Mentor name= {mentor.name}")
        print(f"Mentor email= {mentor.email}")
        print(f"Total Number of matched skills= {match['score']} / {match['total_required_skills']}")
        print(f"Matched skills= {",".join(match['matched_skills'])}")
        
        print("\n*********************************************\n")
        


def main() -> None:

    database = DataBaseManager("DataofClass.db")

    matching_service = MentorMatchingService(database)

    while True:

        print_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                add_intern(database)

            elif choice == 2:
                add_mentor(database)

            elif choice == 3:
                add_problem(database)

            elif choice == 4:
                view_interns(database)

            elif choice == 5:
                view_mentors(database)

            elif choice == 6:
                view_problems(database)

            elif choice == 7:
                find_matching_mentors(database,matching_service)

            elif choice == 8:
                database.close()
                print("\nThank you for using the system.")
                break

            else:
                print("\nInvalid choice. Please try again.")

        except ValueError:
            print("\nPlease enter a valid number.")


if __name__ == "__main__":
    main()