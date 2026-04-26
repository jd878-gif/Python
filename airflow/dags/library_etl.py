from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

import pandas as pd
from sqlalchemy import create_engine

default_args = {
    'owner' : 'jeet',
    'retries' : 1,
    'retry_delay' : timedelta(minutes=3),
    'email_on_failure' : False
}


DB_URL = "mysql+pymysql://root:jeet1108@host.docker.internal/library_db"

def extract(**context):
        print("extract starting..")
        engine = create_engine(DB_URL)

        books_df = pd.read_sql("Select * from book", engine)
        member_df = pd.read_sql("Select * from member", engine)

        context['ti'].xcom_push(key='books', value=books_df.to_json())
        context['ti'].xcom_push(key='members', value=member_df.to_json())
        return "extracted successfully"


def transform(**context):
    print("Transforming started..")
    book_json = context['ti'].xcom_pull(task_ids = 'extract_data', key = 'books')
    member_json = context['ti'].xcom_pull(task_ids = 'extract_data', key = 'members')

    books_df = pd.read_json(book_json)
    members_df = pd.read_json(member_json)

    books_df['status'] = books_df['is_borrowed'].apply(
         lambda x: 'Borrowed' if x==1 else 'Available'
    )

    merged_both = books_df.merge(members_df, left_on='borrowed_by', right_on='member_id', how='left')

    context['ti'].xcom_push(key='final_data', value=merged_both.to_json())
    return "Transformed successfully"

    
def load(**context):
    print("Loading started..")

    final_json = context['ti'].xcom_pull(task_ids = 'transform_data', key = 'final_data')

    final_df = pd.read_json(final_json)

    engine = create_engine(DB_URL)
    final_df.to_sql('library_report', engine, if_exists = 'replace', index = False)

    final_df.to_csv('/tmp/library_report.csv', index = False)

    return "loaded successfully"

    
def summary(**context):
    print("Summary:")

    final_json = context['ti'].xcom_pull(task_ids = 'transform_data', key = 'final_data')

    final_df = pd.read_json(final_json)

    total_books = len(final_df)
    borrowed_books = len(final_df[final_df['status']=='Borrowed'])
    available_books = len(final_df[final_df['status']=='Available'])
    borrow_rate = (borrowed_books/total_books)*100

    print(f"Total books: {total_books}")
    print(f"Borrowed books: {borrowed_books}")
    print(f"Available books: {available_books}")
    print(f"Borrow rate: {borrow_rate}")

    return "Summary completed successfully"


with DAG(
    dag_id='my_first_dag',
    default_args=default_args,
    description='My First Dag',
    start_date=datetime(2025, 1, 1),
    schedule='@daily',
    catchup=False
)as dag:
     
     extract_task = PythonOperator(
        task_id = 'extract_data',
        python_callable=extract
       
    )
     
     transform_task = PythonOperator(
          task_id = 'transform_data',
          python_callable=transform
          
     )

     load_task = PythonOperator(
          task_id = 'load_data',
          python_callable=load
          
     )

     summary_task = PythonOperator(
          task_id = 'summary_data',
          python_callable=summary
          
     )

     extract_task >> transform_task >> load_task >> summary_task


 

