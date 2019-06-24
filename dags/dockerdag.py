'''
sudo apt install -y docker-ce

sudo apt install -y docker-compose

sudo apt install -y python-pip

pip install apache-airflow
pip install docker


remove docker

To identify what installed package you have:

dpkg -l | grep -i docker

#Remove

sudo apt-get purge -y docker-engine docker docker.io docker-ce docker-compose golang-docker-credential-helpers docker-ce-cli python-dockerpty
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce docker-compose golang-docker-credential-helpers docker-ce-cli python-dockerpty


'''
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.docker_operator import DockerOperator

default_args = {
        'owner'                 : 'airflow',
        'description'           : 'Use of the DockerOperator',
        'depend_on_past'        : False,
        'start_date'            : datetime(2018, 1, 3),
        'email_on_failure'      : False,
        'email_on_retry'        : False,
        'retries'               : 1,
        'retry_delay'           : timedelta(minutes=5)
}

with DAG('docker_dag', default_args=default_args, schedule_interval="*/5 * * * *", catchup=False) as dag:
        t1 = BashOperator(
                task_id='print_current_date',
                bash_command='date'
        )

        t2 = DockerOperator(
                task_id='docker_command',
                #image='centos:latest',
                image='pythonrobot',                
                api_version='auto',
                auto_remove=True,
                #command="echo 'starting docker' && /bin/sleep 30",
                docker_url="unix://var/run/docker.sock",
                network_mode="bridge"
        )

        t3 = BashOperator(
                task_id='print_hello',
                bash_command='echo "hello world"'
        )

        t1 >> t2 >> t3
