"""
A DAG definition file in Airflow, written in Python.
"""
from datetime import datetime, timedelta
from airflow.models import DAG  # Import the DAG class
from airflow.operators.bash_operator import BashOperator
from airflow.operators.sensors import TimeDeltaSensor

default_args = {
    'owner': 'you',
    'depends_on_past': False,
    'inparam': 'xxxyyyzzz',
    'start_date': datetime(2018, 1, 8),
}

dag = DAG(
    dag_id='anatomy_of_a_dag3',
    description="This describes my DAG",
    default_args=default_args,
    #schedule_interval=timedelta(days=1)
    schedule_interval='57 9 * * *',
    )   # This is a daily DAG.

# t0 and t1 are examples of tasks created by instantiating operators
t0 = TimeDeltaSensor(
    task_id='wait_60_seconds',
    delta=timedelta(seconds=60),
    dag=dag)

t1 = BashOperator(
    task_id='print_date_in_bash',
    bash_command='date',
    dag=dag)

t1.set_upstream(t0)
