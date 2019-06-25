FROM puckel/docker-airflow
# supervisord setup                       
#RUN apt-get update && apt-get install -y supervisor                       
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# Airflow setup
#ENV AIRFLOW_HOME=/app/airflow
USER root
RUN pip install docker \
    && pip install kubernetes 
#    && pip install psycopg2-binary
USER airflow
#RUN pip install apache-airflow                       
#COPY /dags/response_rate_etl.py $AIRFLOW_HOME/dags/
#RUN airflow initdb
#EXPOSE 8080
#CMD ["/usr/bin/supervisord"]