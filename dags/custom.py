import logging

from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
#from airflow.operators import MyFirstOperator

log = logging.getLogger(__name__)

class MyFirstOperator(BaseOperator):

    @apply_defaults
    def __init__(self, my_operator_param, *args, **kwargs):
        self.operator_param = my_operator_param
        super(MyFirstOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info("Hello WorldXXXXXXXXXXXXXXX!")
        log.info('operator_param: %s', self.operator_param)

class MyFirstPlugin(AirflowPlugin):
    name = "my_first_plugin"
    operators = [MyFirstOperator]


dag = DAG('my_test_dag', description='Another tutorial DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

dummy_task = DummyOperator(task_id='dummy_task', dag=dag)

operator_task = MyFirstOperator(my_operator_param='This is a test.',
                                task_id='my_first_operator_task', dag=dag)
operator_task2 = MyFirstOperator(my_operator_param='This is a test2.',
                                task_id='my_first_operator_task2', dag=dag)

operator_task3 = MyFirstOperator(my_operator_param='This is a test3.',
                                task_id='my_first_operator_task3', dag=dag)

dummy_task >> operator_task
operator_task >> operator_task2
operator_task2 >> operator_task3
