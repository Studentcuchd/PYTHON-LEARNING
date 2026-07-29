from Model.internclass import Intern
from Model.mentorclass import Mentor
from Model.problemclass import Problem

from Repository.intern_repository import InternRepository
from Repository.problem_repository import ProblemRepository
from Repository.mentor_repository import MentorRepository

from Service.mentor_matching_service import MentorMatchingService


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
 
 
    
def add_intern(intern_repository:InternRepository) -> None:
    name=input("enter your name=")
    email=input("enter you eamil=")
    intern_obj=Intern(name,email)
    intern_repository.add_intern(intern_obj)
    print("Intern Added successfully")

    

def view_interns(intern_repository:InternRepository) ->None:
    interns_list=intern_repository.get_all_interns()
     
    if not interns_list:
        print("No intern found please add intern")
        return
    
    print("\n")    
    print("Interns")
    print("\n")
    
    for intern in interns_list:
        print(f"ID= {intern.intern_id}")
        print(f"Name= {intern.name}")
        print(f"Email= {intern.email}")
        print("\n") 
 
        

def add_mentor(mentor_repository:MentorRepository) -> None:
    name=input("enter your name=").strip()
    email=input("enter you eamil=").strip()
    
    skill_set=set()
    total_skills=int(input("Enter total number of skills you have="))
    print("\n Enter your skills one by one \n")
    for i in range(total_skills):
        skill_input=input(f"Enter your skill=")
        if skill_input:
            skill_set.add(skill_input)

    mentor_obj=Mentor(name,email,skill_set)
    mentor_repository.add_mentor(mentor_obj)
    
    print("Mentor added successfully.")   




def view_mentors(mentor_repository:MentorRepository) -> None:
    mentor_list=mentor_repository.get_all_mentors()
    
    if not mentor_list:
        print("No Mentor found Please add a mentor")
        return 
    
    print("\n")
    print("Mentors")
    print("\n")
       
    for mentor in mentor_list:
        print(f"ID= {mentor.mentor_id}")
        print(f"Name= {mentor.name}")
        print(f"Email= {mentor.email}")
        print(f"Skills= {','.join(mentor.expertise)}")
        print("\n")
        


        
def add_problem(problem_repository: ProblemRepository,intern_repository:InternRepository) -> None:
    interns_list= intern_repository.get_all_interns()
    if not interns_list:
        print("No intern found please add intern")
        return
    
    view_interns(intern_repository)
    
    intern_id=int(input("Enter Your Intern ID="))
    
    valid_intern=False
    
    for intern in interns_list:
        if intern.intern_id==intern_id:
            valid_intern=True
            break
    
    if not valid_intern:
        print("Invalid Intern id")
        return
    
    title = input("Enter Problem Title= ")
    description = input("Enter Problem Description= ")
    
    required_skills=set()
    
    total_skills = int(input("Enter total required skills= "))
    
    print("\n")
    print("Enter required skills one by one")
    print("\n")
    
    for i in range(total_skills):
        skill=input(f"Enter skill=")

        if skill:
            required_skills.add(skill)
    
    
    problem_obj = Problem(
        title,
        description,
        required_skills,
        intern_id
    )

    problem_repository.add_problem(problem_obj)

    print("Problem added successfully.")





def view_problems(problem_repository: ProblemRepository) -> None:

    problem_list = problem_repository.get_all_problems()

    if not problem_list:
        print("No problems found.")
        return
    
    print("\n")
    print(" Problems")
    print("\n")

    for problem in problem_list:
        print(f"Problem ID = {problem.problem_id}")
        print(f"Title= {problem.title}")
        print(f"Description= {problem.description}")
        print(f"Intern ID= {problem.intern_id}")
        print(f"Required Skills= {', '.join(problem.req_skill)}")
        print("\n")
  
  
        
        

def find_matching_mentors(problem_repository: ProblemRepository,matching_service: MentorMatchingService) -> None:
    problem_list = problem_repository.get_all_problems()

    if not problem_list:
        print("No Problem in the list please add problem")
        return   
    
    view_problems(problem_repository)
    problem_id=int(input("Pleease enter id of your problem="))
    
    matching_mentors_list=matching_service.find_matching_mentors(problem_id)
    
    if not matching_mentors_list:
        print("No match found")
        return
    
    print("\n")
    print("Matching Mentors")
    print("\n")

    for match in matching_mentors_list:
        
        mentor=match['mentor']
        print(f"Mentor id= {mentor.mentor_id}")
        print(f"Mentor name= {mentor.name}")
        print(f"Mentor email= {mentor.email}")
        print(f"Total matched skills= {match['score']} / {match['total_required_skills']}")
        print(f"Matched skills name= {",".join(match['matched_skills'])}")
        
        

