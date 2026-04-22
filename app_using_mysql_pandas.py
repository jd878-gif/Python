import matplotlib.pyplot as plt

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:jeet1108@localhost/library_db")

print("Connection successful!")

books_df = pd.read_sql("SELECT * FROM book", engine)


members_df = pd.read_sql("SELECT * FROM member", engine)

print("\n ALL BOOKS ")
print(books_df)

print("\n ALL MEMBERS ")
print(members_df)

print("\n TOTAL BOOKS ")
print(f"Total books: {len(books_df)}")

print("\n BORROWED VS AVAILABLE ")
print(books_df['is_borrowed'].value_counts())

print("\n BOOKS BY PUBLISHER ")
print(books_df.groupby('publisher')['title'].count())

print("\n BOOKS BY AUTHOR ")
print(books_df.groupby('author')['title'].count())

print("\n BORROWED BOOKS DETAILS ")
borrowed_books = books_df[books_df['is_borrowed'] == 1]
print(borrowed_books)

print("\n AVAILABLE BOOKS ")
available_books = books_df[books_df['is_borrowed'] == 0]
print(available_books)

print("\n MOST EXPERIENCED MEMBER ")
print(members_df.loc[members_df['years_of_experience'].idxmax()])

print("\n AVERAGE MEMBER AGE ")
print(f"Average age: {members_df['age'].mean():.1f}")

print("\n MEMBER WHO BORROWED ")
borrowed_with_member = books_df[books_df['is_borrowed'] == 1].merge(
    members_df, 
    left_on='borrowed_by', 
    right_on='member_id'
)
print(borrowed_with_member[['title', 'name', 'email']])

print("\n BORROWING PERCENTAGE ")
borrow_percentage = (len(borrowed_books) / len(books_df)) * 100
print(f"Borrowing rate: {borrow_percentage:.1f}%")

books_df.groupby('author')['title'].count().plot(
    kind = 'line',
    title = 'Book title by author',
    color = ['blue', 'yellow'],
    xlabel = 'author',
    ylabel = 'Count'
)
plt.tight_layout()
plt.savefig('books_by_author.png')
plt.show()

books_df['is_borrowed'].value_counts().plot(
    kind = 'bar',
    title = 'borrowed vs Available books',
    color = ['red', 'green'],
    xlabel = '0=Availble, 1=Not Availble',
    ylabel = 'Count'
)
plt.tight_layout()
plt.savefig('borrowed vs not borrowed.png')
plt.show()

books_df.groupby('publisher')['title'].count().plot(
    kind = 'pie',
    title = 'Books by publisher',
    autopct = '%1.1f%%'
    
)
plt.tight_layout()
plt.savefig('books_by_publisher.png')
plt.show()

print(f"Total Books: {len(books_df)}")
print(f"Total Members: {len(members_df)}")
print(f"Books Borrowed: {len(borrowed_books)}")
print(f"Books Available: {len(available_books)}")
print(f"Borrowing Rate: {borrow_percentage:.1f}%")