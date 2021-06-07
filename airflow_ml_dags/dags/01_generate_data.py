from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "01-generate-data",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:
    generate_data = DockerOperator(
        image="airflow-generate-data",
        command="--output_dir /data/raw/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-generate-data",
        do_xcom_push=False,
        volumes=["/home/vovan/MADE/ML-IN-PROD/vbakulev/airflow_ml_dags/data:/data"],
    )

    generate_data
