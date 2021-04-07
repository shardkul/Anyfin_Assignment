"""
Code that goes along with the Airflow located at:
"""
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta

# Load SQL query for Task 5 
query_path = '/usr/local/airflow/dags/sql/task_5.sql'
query = open(query_path,'r').read()

# Load Public key used for encryting email ID's
key_path = '/usr/local/airflow/dags/key/public.key'
pub_key = open(key_path,'r', encoding='utf-16').read()

# Adding public key to the query for encryption
final_query = query.format(pub_key)

with DAG(
    "task_4_n_5",
    start_date=datetime(2021, 4, 4),
    max_active_runs=1,
    schedule_interval= '0 0 * * *') as dag:


    task_4 = PostgresOperator(
        task_id='refresh_dataset',
        postgres_conn_id = 'postgreSQL',
        sql='sql/task_4.sql'
        )

    task_5 = PostgresOperator(
        task_id='encrypt_email_data',
        postgres_conn_id = 'postgreSQL',
        sql=final_query
        )

    [task_4,task_5]



