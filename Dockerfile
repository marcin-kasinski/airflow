FROM puckel/docker-airflow
# supervisord setup                       
#RUN apt-get update && apt-get install -y supervisor                       
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# Airflow setup
#ENV AIRFLOW_HOME=/app/airflow
ENV TZ=Europe/Warsaw

USER root

RUN pip install docker \
    && pip install kubernetes \
    && pip install psycopg2-binary \
    #http://<your_airflow_host_and_port>/admin/metrics/ \
    && pip install airflow-exporter \
    && apt-get update \
    && apt-get install -y tzdata \
    && sed -i -e 's/default_timezone = utc/default_timezone = Europe\/Warsaw/g' /usr/local/airflow/airflow.cfg

USER airflow

#RUN pip install prometheus_client \
#    && pip install airflow-exporter

ENV TZ=Europe/Warsaw
#RUN pip install apache-airflow                       
#COPY /dags/response_rate_etl.py $AIRFLOW_HOME/dags/
#RUN airflow initdb
#EXPOSE 8080
#CMD ["/usr/bin/supervisord"]