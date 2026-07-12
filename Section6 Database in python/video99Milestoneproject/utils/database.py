# books=[]

# csv
# book_file="Section6 Database in python/textfiles/milstone.txt"


# JSON
import json
book_file="Section6 Database in python/textfiles/milstone_JSON.txt"



# def add_book(name,author):
#     books.append({"Name":name, "Author:":author, "Read":False})

# def read_books(name):
#     for book in books:
#         if book['Name']==name:
#             book['Read']=True

# def list_books():
#     return books

# """

# The only issue here is modifying a list while iterating over it, which can lead to skipped elements or unexpected behavior.
# def delete_books(name):
#     for book in books:
#         if book["Name"]==name:
#             books.remove(book)
# """

# # so we will use another that is list comprehension
# def delete_books(name):
#     # we have to use that global variable list
#     global books
#     books=[i for i in books if i["Name"]!=name]





# Part 2 save data in csv


# def add_book(name,author):
#     with open(book_file,"a") as writer_book:
#         writer_book.write(f"{name},{author}, False\n")
        

        

# def read_books(name):
#     book=list_books()
#     for i in book:
#         if i["Name"]==name:
#             i["Read"]=True
            
#             # update hogya ab firse jo list thi usko write krna pdega sara
#     with open(book_file,"w") as writer_book:
#         for i in book:
#             writer_book.write(f"{i['Name']},{i['Author']},{i['Read']}\n")
        
    
# def list_books():
#     books=[]
#     with open(book_file,"r") as reader:
#         for line in reader:
#             line=line.strip()
#             book=line.split(",")
#             books.append({
#                 "Name":book[0],
#                 "Author":book[1],
#                 "Read":book[2]
#             })           
#     return books


# def delete_books(name):
#     books=list_books()
#     for book in books:
#         if book["Name"]==name:
#             books.remove(book)
            
#     with open(book_file,"w") as writer:
#         for i in books:
#             writer.write(f"{i['Name']},{i['Author']},{i['Read']}\n")



# Part 3 json



""" 
[
    {
    data
    }
]

"""

# List all books

def list_books():
    with open(book_file,"r") as reader_file:
        return json.load(reader_file)

def _write_again(books):
    with open(book_file,"w") as writer:
        json.dump(books,writer,indent=4)    

def add_book(name,author):
    # suppose there are already books in my fiel so i want to append so pehle list kro books then dump
    books=list_books()
    books.append(
        {
            "Name":name,
            "Author":author,
            "Read":False
        }
    )
    _write_again(books)
       
def read_books(name):
    books=list_books()
    for book in books:
        if book["Name"]==name:
            book["Read"]=True
            
    _write_again(books)
    
    
def delete_books(name):
    books=list_books()
    # for book in books:
    #     if book["Name"]==name:
    #         books.remove(book)
    books=[book for book in books if book["Name"]!=name]
    
    _write_again(books)