class Book:
    def __init__(self,isbn_no,title,author,publisher,years_of_publication):
        self.isbn_no = isbn_no
        self.title = title
        self.author = author
        self.publisher = publisher
        self.years_of_publication = years_of_publication
        self.is_borrowed = False
        self.borrowed_by = None

    def __str__(self):
        return f"isbn_no: {self.isbn_no},title:{self.title},author:{self.author},publisher:{self.publisher},years_of_publication:{self.years_of_publication}"
    
class Member:
    def __init__(self,member_id,name,age,email,years_of_experience):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.email = email
        self.years_of_experience = years_of_experience

    def __str__(self):
        return f"memebr_id: {self.member_id},name:{self.name},age:{self.age},email:{self.email},years_of_experience:{self.years_of_experience}"
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def Insert_Book(self,book):
        self.books.append(book)
    
    def Search_Book(self,book_id,book_title,book_author):
        for book in self.books:
            if book.isbn_no == book_id:  
                return book
            if book.title == book_title:  
                return book
            if book.author == book_author:
                return book 
        return None
    
    def Delete_Book(self,id):
        for i, book in enumerate(self.books):
            if book.isbn_no == id:
                del self.books[i]  
                return True
        return False
    
    def borrow_book(self,member_id,book_id):
    
        found_member = None
        for member in self.members:
            if member.member_id == member_id:
                found_member = member
                break

        if found_member is None:
                print("Member is not registered:")
                return False
    
        found_book = None    
        for book in self.books:
            if book.isbn_no == book_id:
                found_book = book
                break

        if found_book is None:
                print("Book is not available")
                return False
        
        if found_book.is_borrowed == True:
            print("Book is already borrowed")
            return False
        
        found_book.is_borrowed = True
        print("Book is borrowed successfully, Thank you!")
        return True
    
    def return_book(self,member_id,book_id):
        found_member = None
        for member in self.members:
            if member.member_id == member_id:
                found_member = member
                break

        if found_member is None:
            print("Member not registered:")
            return False
        
        found_book = None    
    
        for book in self.books:
            if book.isbn_no == book_id:
                found_book = book
                break

        if found_book is None:
            print("Book not found")
            return False
        
        if found_book.is_borrowed==True:
            print("Book returned successfully")
            return True
    
        if found_book.borrowed_by != member_id:
            print("This member did not borrow the book")
            return False

        
        found_book.is_borrowed= False
        found_book.borrowed_by = None

        print("book returned successfully")
        return True

    
    
    def Display_Book(self):
        if not self.books:
            print("There is no book available")
            return
        print("Library Catalogue:")
        for book in self.books:
            print(book)

  

    def Insert_Member(self,member):
        self.members.append(member)
    
    def Search_Member(self,member_id):
        for member in self.members:
            if member.member_id == member_id:  
                return member 
        return None
    
    def Delete_Member(self,id):
        for i, member in enumerate(self.members):
            if member.member_id == id:
                del self.members[i]  
                return True
        return False
    
    def Display_Member(self):
        if not self.members:
            print("There is no member available")
            return
        print("Member Catalogue:")
        for member in self.members:
            print(member)

my_library = Library()

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
                result = my_library.Search_Book(book_id,book_title=None,book_author=None)
                if result:
                    print(f"Book found: ID={result.isbn_no}, Name = {result.title}, author_name = {result.author}, publisher_name = {result.publisher}, yop = {result.years_of_publication}")
                else:
                    print(f"No book found with ID {book_id}.")
            
            elif choice == 2:
                title = input("Enter a title of the book:")
                result = my_library.Search_Book(book_id=None, book_title=title, book_author=None)
                if result:
                    print(f"Book found: ID={result.isbn_no}, Name = {result.title}, author_name = {result.author}, publisher_name = {result.publisher}, yop = {result.years_of_publication}")
                else:
                    print(f"No book found with Title {title}.")
            
            elif choice == 3:
                name = input("Enter author name of the book:")
                result = my_library.Search_Book(book_id=None,book_title=None, book_author=name)
                if result:
                    print(f"Book found: ID={result.isbn_no}, Name = {result.title}, author_name = {result.author}, publisher_name = {result.publisher}, yop = {result.years_of_publication}")
                else:
                    print(f"No book found with Author Name {name}.")
            else:
                print("Enter a valid choice")
        
        except ValueError:
            print("Enter a valid value!")

    elif operation == "2":
        isbn_no = int(input("Enter isbn_no for the book:"))   
        title = input("Enter title for the book:")
        author = input("Enter author_name for the book:")
        publisher = input("Enter publisher_name for the book:")
        years_of_publication = int(input("Enter years of publication for the book:"))
    
        new_book = Book(isbn_no,title,author,publisher,years_of_publication)

        duplicate_found = False
        for book in my_library.books:
            if new_book.isbn_no == book.isbn_no:
                duplicate_found = True
                break
        if duplicate_found:
            print("You can't insert the book as the id for the book that you entered is already exist:")
        else:
           my_library.Insert_Book(new_book)
           my_library.Display_Book()
            
    
    elif operation == "3":
        try:
            book_id = int(input("Enter a isbn_no of the book that you want to delete:"))
            print(my_library.Delete_Book(book_id))
            my_library.Display_Book()
        except ValueError:
            print("Enter a valid value!")

    
    elif operation == "4":
        try:
            member_id = int(input("Enter the member_id"))
            book_id = int(input("Enter the isbn_no for the book that you want to borrow"))
            max_book = 2
            start_count = 0
            for book in my_library.books:
                if book.borrowed_by==member_id:
                    start_count+=1
            if start_count>=max_book:
                print("Sorry! You can't borrow more than 2 books ")
            else:
                my_library.borrow_book(member_id,book_id)
        except ValueError:
            print("Enter a valid choice")
        
    
    elif operation == "5":
        member_id = int(input("Enter the member_id"))
        book_id = int(input("Enter the isbn_no for the book that you want to return"))
        my_library.return_book(member_id,book_id) 

    elif operation == "6":
        try:
            user_id = int(input("Enter a id of the memebr that you want to search:"))
            result = my_library.Search_Member(user_id)
            if result:
                print(f"Member found: ID={result.member_id}, Name = {result.name}, age = {result.age}, email = {result.email}, yoe = {result.years_of_experience}")
            else:
                print(f"No member found with ID {user_id}.")
        except ValueError:
            print("Enter a valid value!")

        my_library.search_member(user_id)
        
    elif operation == "7":            
  
        member_id = int(input("Enter member_id for the member:"))   
        name = input("Enter name for the member:")
        age = int(input("Enter age for the member:"))
        email = input("Enter email for the member:")
        years_of_experience = int(input("Enter years of experience for the member:"))

        new_member = Member(member_id,name,age,email,years_of_experience)

        my_library.Insert_Member(new_member)
        my_library.Display_Member()
        

    elif operation == "8":    
        try:
            user_id = int(input("Enter a member_id that you want to delete:"))
        except ValueError:
            print("Enter a valid value!")

        my_library.Delete_Member(new_member)
        my_library.Display_Member()
    
    
    elif operation == "9":
        break
    else:
        print("Sorry! Invalid choice")



    


# my_library.Insert_Book(Book("2000","ABC","Charles","J&J",12,None, None))
# my_library.Insert_Member(Member(101,"Frank",30,"fr123@gmail.com",4))
# # print(my_library.Search_Member(102))
# # print(my_library.Delete_Member(100))

# # print(my_library.Search_Book("2001"))
# # print(my_library.Delete_Book("2001"))
# print(my_library.borrow_book(101,"2000"))
# print(my_library.return_book(101,"2001"))

# my_library.Display_Book()
# my_library.Display_Member()

    