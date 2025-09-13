# import the libraries
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
# This makes scheduling easy
from datetime import datetime

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'rainu',
    'start_date': datetime(2025, 9, 1),
    'email': ['dummyeamils'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'myfirstdag',
    default_args=default_args,
    description='My first DAG',
    schedule=timedelta(days=1),
)

# define the tasks

# define the first task

extract = BashOperator(
    task_id='extract',
    bash_command='cut -d":" -f1,3,6 /etc/passwd > /home/airflow/extracted-data.txt',
    dag=dag,
)

# define the second task
transform_and_load = BashOperator(
    task_id='transform',
    bash_command='tr ":" "," < /home/airflow/extracted-data.txt > /home/airflow/transformed-data.csv',
    dag=dag,
)

# task pipeline
extract >> transform_and_load