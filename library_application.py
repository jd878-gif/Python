from datetime import datetime, timedelta
book_list=[
    {
        "isbn_no" : 1,
        "title" : "Magic",
        "author" : "ABC",
        "publisher" : "XY",
        "years_of_publication" : 2,
        "is_borrowed" : False,
        # "borrowed_by" : None

    }
]

member_list = [
    {
        "member_id" : 101,
        "name" : "Bob",
        "age" : 30,
        "email" : "bob123@gmail.com",
        "years_of_experience" : 2,
        "borrowed_books" : []
    }
]

def display_books(book_list):
    for book in book_list:
        print(book)



def search_book(book_list,book_id,book_title,book_author):
    for book in book_list:
        if book.get("isbn_no") == book_id:  
            return book 
        if book.get("title") == book_title:
            return book
        if book.get("author") == book_author:
            return book
    return None
    

def insert_book(book_list):
        
    print(f"isbn_no: {book_list['isbn_no']}")
    print(f"title: {book_list['title']}")
    print(f"author: {book_list['author']}")
    print(f"publisher: {book_list['publisher']}")
    print(f"years_of_publication: {book_list['years_of_publication']}")

def delete_book(book_list,id):
    for i, book in enumerate(book_list):
        if book.get("isbn_no") == id:
            del book_list[i]  
            return True
    return False

def borrow_book(book_list,member_id,member_list,book_id):
    
    found_member = None
    for member in member_list:
        if member.get("member_id") == member_id:
            found_member = member
            break

    if found_member is None:
        print("Member is not registered:")
        return False
    
    found_book = None    
    for book in book_list:
        if book.get("isbn_no") == book_id:
            found_book = book
            break

    if found_book is None:
        print("Book is not available")
        return False
        
    if found_book.get("is_borrowed")==True:
        print("Book is already borrowed")
        return False
    
    
        
    found_book["is_borrowed"]= True
    # found_book["borrowed_by"] = member_id
    found_member["borrowed_books"].append({
    "book_id": book_id,
    "borrowed_date": "2026-03-20"
})

    print("book borrowed successfully")
    return True

# def return_book(book_list,member_id,member_list,book_id):
#     found_member = None
#     for member in member_list:
#         if member.get("member_id") == member_id:
#             found_member = member
#             break

#     if found_member is None:
#         print("Member not registered:")
#         return False
#     found_book = None    
    
#     for book in book_list:
#         if book.get("isbn_no") == book_id:
#             found_book = book
#             break

#     if found_book is None:
#         print("Book not found")
#         return False
        
#     if found_book.get("is_borrowed")==True:
#         print("Book returned successfully")
#         return True
    
#     if found_book.get("borrowed_by") != member_id:
#         print("This member did not borrow the book")
#         return False

        
#     found_book["is_borrowed"]= False
#     found_book["borrowed_by"] = None

#     print("book returned successfully")
#     return True

def return_book(book_list, member_id, member_list, book_id):

    found_member = None
    for member in member_list:
        if member.get("member_id") == member_id:
            found_member = member
            break

    if found_member is None:
        print("Member not registered")
        return False
    
    found_book = None
    for book in book_list:
        if book.get("isbn_no") == book_id:
            found_book = book
            break

    if found_book is None:
        print("Book not found")
        return False

    borrowed_list = found_member.get("borrowed_books", [])

    book_found_in_member = None
    for item in borrowed_list:
        if item["book_id"] == book_id:
            book_found_in_member = item
            break

    if book_found_in_member is None:
        print("This member did not borrow this book")
        return False

    borrowed_list.remove(book_found_in_member)

    found_book["is_borrowed"] = False

    print("Book returned successfully")
    return True

def display_members(member_list):
     for member in member_list:
         print(member)

def get_due_date(borrowed_date_str):
    borrowed_date = datetime.strptime(borrowed_date_str, "%Y-%m-%d")
    due_date = borrowed_date + timedelta(days=7)
    return due_date

def is_overdue(borrowed_date_str):
    today = datetime.now()
    due_date = get_due_date(borrowed_date_str)
    return today > due_date

def calculate_fine(borrowed_date_str):
    today = datetime.now()
    due_date = get_due_date(borrowed_date_str)

    if today <= due_date:
        return 0

    days_late = (today - due_date).days
    fine = days_late * 10
    return fine

def check_member_fines(member):
    total_fine = 0

    for book in member.get("borrowed_books", []):
        borrowed_date = book["borrowed_date"]
        fine = calculate_fine(borrowed_date)

        if fine > 0:
            print(f"Book ID {book['book_id']} fine: {fine}")
            total_fine += fine

    print("Total fine:", total_fine)
    return total_fine



# New Search Method:
def search_member(member_list,user_id):
    for member in member_list:
        if member.get("member_id") == user_id:  
            return member 
    return None

def insert_member(member_list):
                
    print(f"member_id: {member_list['member_id']}")
    print(f"name: {member_list['name']}")
    print(f"age: {member_list['age']}")
    print(f"email: {member_list['email']}")
    print(f"years_of_expeience: {member_list['years_of_experience']}")

def delete_member(member_list,id):
            for i, member in enumerate(member_list):
                if member.get("member_id") == id:
                    del member_list[i]  
                    return True
            return False

while True:
    print("\n Hit 1 for Search Book")
    print("\n Hit 2 for Insert Book")
    print("\n Hit 3 for Delete Book")
    print("\n Hit 4 for borrow a book?")
    print("\n Hit 5 for return a book?")
    print("\n Hit 6 for Search Member")
    print("\n Hit 7 for Insert Member")
    print("\n Hit 8 for Delete Member")
    print("\n Hit 9 for Exit")
    

    operation = input("Hey! What do uou want to perform today from the given options? ")
    
    if operation == "1":

    
        try:
            choice = int(input("Search By (1:Id, 2:Title, 3:Author):"))
            if choice == 1:

                book_id = int(input("Enter isbn_no of the book:"))
                result = search_book(book_list,book_id,book_author=None,book_title=None)
                if result:
                    print(f"Book found: ID={result['isbn_no']}, Name = {result['title']}, author_name = {result['author']}, publisher_name = {result['publisher']}, yop = {result['years_of_publication']}")
                else:
                    print(f"No book found with ID {book_id}.")
            
            elif choice == 2:
                title = input("Enter a title of the book:")
                result = search_book(book_list,book_id=None,book_title=title,book_author=None)
                if result:
                    print(f"Book found: ID={result['isbn_no']}, Name = {result['title']}, author_name = {result['author']}, publisher_name = {result['publisher']}, yop = {result['years_of_publication']}")
                else:
                    print(f"No book found with Title {title}.")
            
            elif choice == 3:
                name = input("Enter author name of the book:")
                result = search_book(book_list,book_id=None,book_title=None,book_author=name)
                if result:
                    print(f"Book found: ID={result['isbn_no']}, Name = {result['title']}, author_name = {result['author']}, publisher_name = {result['publisher']}, yop = {result['years_of_publication']}")
                else:
                    print(f"No book found with Author Name {name}.")
            else:
                print("Enter a valid choice")

            
        except ValueError:
            print("Enter a valid value!")
    
    elif operation == "2":
        user_data={}  
        user_data["isbn_no"] = int(input("Enter isbn_no for the book:"))   
        user_data["title"] = input("Enter title for the book:")
        user_data["author"] = input("Enter author_name for the book:")
        user_data["publisher"] = input("Enter publisher_name for the book:")
        user_data["years_of_publication"] = int(input("Enter years of publication for the book:"))
        user_data["is_borrowed"] = False
        user_data["borrowed_by"] = None

        duplicate_found = False
        for book in book_list:
            if user_data["isbn_no"]==book["isbn_no"]:
                duplicate_found = True
                break
        if duplicate_found:
            print("You can't insert the book as the id for the book that you entered is already exist:")
        else:
            insert_book(user_data)
            book_list.append(user_data)
            print(book_list)
    
    elif operation == "3":
        try:
            book_id = int(input("Enter a isbn_no of the book that you want to delete:"))
        except ValueError:
            print("Enter a valid value!")

        print(delete_book(book_list,book_id))
        display_books(book_list)
    
    elif operation == "4":
        member_id = int(input("Enter the member_id"))
        book_id = int(input("Enter the isbn_no for the book that you want to borrow"))
        max_book = 2
        found_member = None
        for member in member_list:
            if member.get("member_id") == member_id:
                found_member = member
                break
        if found_member is None:
            print("Member not found!")
        elif len(found_member["borrowed_books"]) >= max_book:
            print("You can't borrow more than 2 books!")
        else:
            borrow_book(book_list, member_id, member_list, book_id)
        
    
    elif operation == "5":
        member_id = int(input("Enter the member_id"))
        book_id = int(input("Enter the isbn_no for the book that you want to return"))
        return_book(book_list,member_id,member_list,book_id)

        member = found_member  
        check_member_fines(member) 

    elif operation == "6":
        try:
            user_id = int(input("Enter a id of the memebr that you want to search:"))
            result = search_member(member_list,user_id)
            if result:
                print(f"Member found: ID={result['member_id']}, Name = {result['name']}, age = {result['age']}, email = {result['email']}, yoe = {result['years_of_experience']}")
            else:
                print(f"No member found with ID {user_id}.")
        except ValueError:
            print("Enter a valid value!")

        search_member(member_list,user_id)
        
    elif operation == "7":            

        user_data={}  
        user_data["member_id"] = int(input("Enter member_id for the member:"))   
        user_data["name"] = input("Enter name for the member:")
        user_data["age"] = input("Enter age for the member:")
        user_data["email"] = input("Enter email for the member:")
        user_data["years_of_experience"] = int(input("Enter years of experience for the member:"))

        print(insert_member(user_data))
        member_list.append(user_data)
        print(member_list)

    elif operation == "8":    
        try:
            user_id = int(input("Enter a member_id that you want to delete:"))
        except ValueError:
            print("Enter a valid value!")

        print(delete_member(member_list,user_id))
        display_members(member_list)
    
    
    elif operation == "9":
        break
    else:
        print("Sorry! Invalid choice")


### Extra code for personal use:
# while True:
#     operation = input("Choose operation from exit, search_book, insert_book and delete_book ")
#     if operation == 'exit':
#         break
#     elif operation == 'search_book':
#         author_name = input("Enter author name for the book")
#         result = search_book(book_list,book_id)        
#     elif operation == 'insert_book':
#         result = insert_book(book_list)
#     else:
#         delete_book(book_list,id)

# display_books(book_list)

# def search_books(book_list):
#     for book in book_list:
#         if book['author'] == "ABC":
#             return book
    
#     return None

# x = search_books(book_list)
# print(x)

# search_book(book_list,book_id)
# display_books(book_list)

# def delete(book_list):
#     for book in book_list:
#         if book['author'] == "AB":
#             del book_list
#         return book
    
#     return None

# delete(book_list)
# display_books(book_list)

# # def search_member(member_list):
# #     for member in member_list:
# #         if member['member_id'] == 101:
# #             return member
    
# #     return None

# # x = search_member(member_list)
# # print(x)

# def delete_member(member_list):
#      for member in member_list:
#           if member['name'] == 'Bob':
#                del member_list
#                return member

# print(delete_member(member_list))
# display_members(member_list)

# def insert_member(member_list):
#             insert_mems = {
#                 "member_id" : 102,
#                 "name" : "Franklin",
#                 "age" : 35,
#                 "email" : "fr121@gmail.com",
#                 "years_of_experience" : 5
#             }

#             member_list.append(insert_mems)
#             return(member_list)

#         print(insert_member(member_list))

# Need to update in OOP
# Keep track of borrowing books (#3)