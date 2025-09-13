FROM apache/airflow:3.0.6
ADD requirements.txt .
RUN pip install -r requirements.txt