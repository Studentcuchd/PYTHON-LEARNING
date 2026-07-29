from Repository.database import Database

from Repository.skill_repository import SkillRepository
from Repository.intern_repository import InternRepository
from Repository.mentor_repository import MentorRepository
from Repository.problem_repository import ProblemRepository

from Service.mentor_matching_service import MentorMatchingService

from App.app_functions import (
    print_menu,
    add_intern,
    view_interns,
    add_mentor,
    view_mentors,
    add_problem,
    view_problems,
    find_matching_mentors,
)






def main() -> None:
    database = Database("MatchingSystem.db")

    skill_repository = SkillRepository(database)

    intern_repository = InternRepository(database)


    mentor_repository = MentorRepository(
        database,
        skill_repository
    )

    problem_repository = ProblemRepository(
        database,
        skill_repository
    )

    matching_service = MentorMatchingService(
        mentor_repository,
        problem_repository
    )



    while True:

        print_menu()

        try:
            choice = int(input("\nEnter your choice= "))

            if choice == 1:
                add_intern(intern_repository)

            elif choice == 2:
                add_mentor(mentor_repository)

            elif choice == 3:
                add_problem(problem_repository,intern_repository)

            elif choice == 4:
                view_interns(intern_repository)

            elif choice == 5:
                view_mentors(mentor_repository)

            elif choice == 6:
                view_problems(problem_repository)

            elif choice == 7:
                find_matching_mentors(problem_repository,matching_service)

            elif choice == 8:
                database.close()
                print("\nThank you for using the system")
                break

            else:
                print("\nInvalid choice. Please try again")

        except ValueError:
            print("\nPlease enter a valid number")


if __name__ == "__main__":
    main()