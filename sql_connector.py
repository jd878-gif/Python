from library_application_using_OOP import Book, Member
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("library_application.db")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_book_table = """
CREATE TABLE IF NOT EXISTS book(
    isbn_no int Primary Key,
    title TEXT,
    author TEXT,
    publisher TEXT,
    years_of_publication int,
    is_borrowed int,
    borrowed_by int
);"""


create_member_table = """
CREATE TABLE IF NOT EXISTS member(
    member_id int Primary Key,
    name TEXT,
    age int,
    email TEXT,
    years_of_experience int
);"""


execute_query(connection, create_book_table)
execute_query(connection, create_member_table)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

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
                search_query_by_id = f"SELECT * FROM book WHERE isbn_no = {book_id}"
                result = execute_read_query(connection,search_query_by_id)
                if result:
                    print(f"Book found: ID={result[0][0]}, Name = {result[0][1]}, author_name = {result[0][2]}, publisher_name = {result[0][3]}, yop = {result[0][4]}")
                else:
                    print(f"No book found with ID {book_id}.")
            
            elif choice == 2:
                title = input("Enter a title of the book:")
                search_query_by_title = f"SELECT * FROM book WHERE title = '{title}'"
                result = execute_read_query(connection,search_query_by_title)
                if result:
                    print(f"Book found: ID={result[0][0]}, Name = {result[0][1]}, author_name = {result[0][2]}, publisher_name = {result[0][3]}, yop = {result[0][4]}")
                else:
                    print(f"No book found with Title {title}.")
            
            elif choice == 3:
                name = input("Enter author name of the book:")
                search_query_by_author = f"SELECT * FROM book WHERE author = '{name}'"
                result = execute_read_query(connection,search_query_by_author)
                if result:
                    print(f"Book found: ID={result[0][0]}, Name = {result[0][1]}, author_name = {result[0][2]}, publisher_name = {result[0][3]}, yop = {result[0][4]}")
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
    

        
        check_duplicate = f"SELECT  * FROM book WHERE isbn_no={isbn_no}" 
        result = execute_read_query(connection,check_duplicate)
        if result:
            print("You can't insert the book as the id for the book that you entered is already exist:")
        else:
           insert_book = f"""insert into book (isbn_no, title, author,publisher,years_of_publication) values({isbn_no}, '{title}', '{author}', '{publisher}',{years_of_publication})"""
           execute_query(connection,insert_book)

        select_book = "SELECT * from book"
        all_books = execute_read_query(connection, select_book)

        for book in all_books:
            print(book)

        
            
    
    elif operation == "3":
            try:
                book_id = int(input("Enter isbn_no of the book you want to delete:"))        
                exist_book = f"SELECT * FROM book where isbn_no={book_id}"
                result = execute_read_query(connection,exist_book)
                if result:
                    delete_book = f""" delete from book where isbn_no = {book_id}"""
                    execute_query(connection,delete_book)
                    select_book = "SELECT * from book"
                    all_books = execute_read_query(connection, select_book)

                    for book in all_books:
                        print(book)      
                else:
                    print("Book not found")
            except:
                print("Enter a valid value")
                

       

    
    elif operation == "4":
        try:
            count = 0
            member_id = int(input("Enter the member_id"))
            book_id = int(input("Enter the isbn_no for the book that you want to borrow"))
            exist_member = f"SELECT * FROM member where member_id={member_id}"
            member_result = execute_read_query(connection,exist_member)
         
            if not member_result:
                print("Member not registered")
            else:
                exist_book = f"SELECT * FROM book where isbn_no={book_id}"
                book_result = execute_read_query(connection,exist_book)
                if not book_result:
                    print("Book not found")
                else:
                    already_borrowed_book = f"SELECT * FROM book where isbn_no = {book_id} AND is_borrowed=1"
                    borrowed_result = execute_read_query(connection,already_borrowed_book)
                    if borrowed_result:
                        print("Book is already borrowed")
                    else:
                        count_books_borrowed = f"SELECT * FROM book where borrowed_by = {member_id}"
                        count_book_result = execute_read_query(connection,count_books_borrowed)
                        if len(count_book_result)>=2:
                            print("you can't borrow more than 2 books")
                        else:
                            update_book = f"update book set is_borrowed = 1, borrowed_by = {member_id} where isbn_no = {book_id}"
                            b_result = execute_query(connection,update_book)
                            print("book is borrowed successfully")

            
            
            
               
        except ValueError:
            print("Enter a valid choice")
        
    
    elif operation == "5":
        try:
            member_id = int(input("Enter the member_id"))
            book_id = int(input("Enter the isbn_no for the book that you want to return"))
            exist_member = f"SELECT * FROM member where member_id={member_id}"
            member_result = execute_read_query(connection,exist_member)
            
            if not member_result:
                print("Member not registered")
            else:
                exist_book = f"SELECT * FROM book where isbn_no={book_id}"
                book_result = execute_read_query(connection,exist_book)
                if not book_result:
                    print("Book not found")
                else:
                    borrowed_book_by_member = f"SELECT * FROM book where isbn_no = {book_id} AND borrowed_by = {member_id}"
                    borrowed_result_by_member = execute_read_query(connection,borrowed_book_by_member)
                    if not borrowed_result_by_member:
                        print("This member didn't borrow the book")
                    else:
                        update_book1 = f"update book set is_borrowed = 0, borrowed_by = Null where isbn_no = {book_id}"
                        update_book1_result = execute_query(connection,update_book1)
                        print("book returned successfully")
        except ValueError:
            print("Enter a valid choice")


    elif operation == "6":
        try:
            user_id = int(input("Enter a id of the memebr that you want to search:"))
            search_query_by_member_id = f"SELECT * FROM member WHERE member_id = {user_id}"
            result = execute_read_query(connection,search_query_by_member_id) 
            if result:
                print(f"Member found: ID={result[0][0]}, Name = {result[0][1]}, age = {result[0][2]}, email = {result[0][3]}, yoe = {result[0][4]}")
            else:
                print(f"No member found with ID {user_id}.")
        except ValueError:
            print("Enter a valid value!")

       
        
    elif operation == "7":            
  
        member_id = int(input("Enter member_id for the member:"))   
        name = input("Enter name for the member:")
        age = int(input("Enter age for the member:"))
        email = input("Enter email for the member:")
        years_of_experience = int(input("Enter years of experience for the member:"))

        check_duplicate_member = f"SELECT  * FROM member WHERE member_id={member_id}" 
        result = execute_read_query(connection,check_duplicate_member)
        if result:
            print("You can't insert the member as the id for the member that you entered is already exist:")
        else:
           insert_book = f"""insert into member (member_id, name, age, email, years_of_experience) values({member_id}, '{name}', {age}, '{email}',{years_of_experience})"""
           execute_query(connection,insert_book)

        select_member = "SELECT * from member"
        all_members = execute_read_query(connection, select_member)

        for member in all_members:
            print(member)
        

    elif operation == "8":    
        try:
            id = int(input("Enter member_id of the member you want to delete:"))        
            exist_member = f"SELECT * FROM member where member_id={id}"
            result = execute_read_query(connection,exist_member)
            if result:
                delete_member = f""" delete from member where member_id = {id}"""
                execute_query(connection,delete_member)
                select_member = "SELECT * from member"
                all_members = execute_read_query(connection, select_member)

                for member in all_members:
                    print(member)
            else:
                print("member not found")
        except:
            print("Enter a valid value")
    
    
    elif operation == "9":
        break
    else:
        print("Sorry! Invalid choice")



# select_book = "SELECT * from book"
# all_books = execute_read_query(connection, select_book)

# for book in all_books:
#     print(book)


# select_member = "SELECT * from member"
# all_members = execute_read_query(connection, select_member)

# for member in all_members:
#     print(member)

# delete_book = "Delete from book where isbn_no=1"
# execute_query(connection,delete_book)

# all_books = execute_read_query(connection, select_book)

# for book in all_books:
#     print(book)


# create_book = """
# INSERT OR IGNORE
#   book (isbn_no, title, author, publisher, years_of_publication, is_borrowed, borrowed_by)
# VALUES
#   (1, 'miracle','JD','J&J',10,0,Null),
#   (3, 'history of USA','John','J&D',50,0,Null),
#   (5, 'key ideas','Bob','D&J',3,0,Null);

# """
# execute_query(connection, create_book)

# create_member = """
# INSERT OR IGNORE
#   member (member_id, name, age, email, years_of_experience)
# VALUES
#   (101, 'Peter',23,'pt23@gmail.com',1),
#   (103, 'Eyan',26,'eyan31@gmail.com',5),
#   (105, 'Franklin',30,'fr53@gmail.com',3);
# """
# execute_query(connection, create_member)