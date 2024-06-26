from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner':'krishna',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='my_first_dag_v3',
    default_args=default_args,
    description='This is my first dag',
    start_date=datetime(2024,5,5,2),
    schedule_interval='@daily'
) as dag:
    task1=BashOperator(
        task_id='first_task',
        bash_command="echo Hi i am krishna"
    )
    task2=BashOperator(
        task_id='second_task',
        bash_command="echo i am the second task and will run after task1"
    )
    task3=BashOperator(
        task_id='third_task',
        bash_command="echo i am third task, i will run with task2"
    )
    task1.set_downstream(task2)
    task1.set_downstream(task3)

    # task1>>task2
    # task1>>task3
    # task1>>[task2,task3]