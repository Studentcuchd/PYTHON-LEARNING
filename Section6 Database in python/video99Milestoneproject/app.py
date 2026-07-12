# menu 
from utils.database import add_book,delete_books,list_books,read_books
def menu():
    user_input=input("Enter your choice=")

    while user_input!="q":
        if user_input=="a":
            add_books_app()
            
        elif user_input=="l":
            list_books_app()
            
        elif user_input=="r":
            read_books_app()
            
        elif user_input=="d":
            delete_book_app()
            
        elif user_input=="q":
            break
        else:
            print("enter a valid input please")
        user_input=input("Enter your choice=")



def add_books_app():
    name=input("enter name of book=")
    author=input("enter name of author=")
    add_book(name,author)
            
def list_books_app():
    books=list_books()
    for i in books:
        print(i)

def read_books_app():
    name=input("Enter name of book=")
    read_books(name)

def delete_book_app():
    name=input("Enter book name for deletion=")
    delete_books(name)


            
menu()