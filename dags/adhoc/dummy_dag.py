"""
dummy_dag: Example BashOperator DAG

This DAG runs three sequential Bash tasks.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'rainu',
    'start_date': datetime(2025, 9, 1),
    'email': ['your email'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='dummy_dag',
    default_args=default_args,
    description='My first DAG',
    schedule=timedelta(minutes=2),
    catchup=False,
    tags=['example'],
    max_active_runs=1,
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='sleep 1',
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command='sleep 2',
    )

    task3 = BashOperator(
        task_id='task3',
        bash_command='sleep 3',
    )

    task1 >> task2 >> task3