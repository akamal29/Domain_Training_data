from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define the Python function to be executed
def print_hello():
    print("Hello, Airflow!")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2025, 1, 6),  # Replace with your start date
}

# Create the DAG object
dag = DAG(
    'simple_hello_airflow',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval='@daily',  # Runs every day
)

# Define the task
hello_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

# Set the task to run
hello_task