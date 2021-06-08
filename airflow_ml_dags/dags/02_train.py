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
        "02-train",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=days_ago(30),
) as dag:
    processed_data = DockerOperator(
        image="airflow-processed-data",
        command="--input_dir /data/raw/{{ ds }} --output_dir /data/processed/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-processed-data",
        do_xcom_push=False,
        volumes=["/home/vovan/MADE/ML-IN-PROD/vbakulev/airflow_ml_dags/data:/data"],
    )

    split_data = DockerOperator(
        image="airflow-split-data",
        command="--input_dir /data/processed/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-split-data",
        do_xcom_push=False,
        volumes=["/home/vovan/MADE/ML-IN-PROD/vbakulev/airflow_ml_dags/data:/data"],
    )

    train_model = DockerOperator(
        image="airflow-train-model",
        command="--input_dir /data/processed/{{ ds }} --output_model /data/models/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-train-model",
        do_xcom_push=False,
        volumes=["/home/vovan/MADE/ML-IN-PROD/vbakulev/airflow_ml_dags/data:/data"],
    )

    val_model = DockerOperator(
        image="airflow-val-model",
        command="--input_dir /data/processed/{{ ds }} --input_model /data/models/{{ ds }} --output_metric /data/models/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-val-model",
        do_xcom_push=False,
        volumes=["/home/vovan/MADE/ML-IN-PROD/vbakulev/airflow_ml_dags/data:/data"],
    )

    processed_data >> split_data >> train_model >> val_model
