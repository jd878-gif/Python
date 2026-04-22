import pandas as pd

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:jeet1108@localhost/library_db")

print("Connection successful!")

books_df = pd.read_sql("SELECT * FROM book", engine)


members_df = pd.read_sql("SELECT * FROM member", engine)

books_df['status'] = books_df['is_borrowed'].apply(lambda x: 'borrowed' if x==1 else 'Available')


merge_df = books_df.merge(members_df, left_on='borrowed_by', right_on='member_id', how='left')


books_df['borrowed_by'] = books_df['borrowed_by'].fillna('Not borrowed') 

final_df = merge_df[['isbn_no', 'title', 'author', 'publisher', 'status', 'name', 'email']]

print(merge_df)
print(final_df)

final_df.to_csv('library_report.csv', index=False)
print("Saved to CSV successfully!")

final_df.to_sql('library_report', engine, if_exists='replace', index=False)
print("Saved to MySQL successfully!")
