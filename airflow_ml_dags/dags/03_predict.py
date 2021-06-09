from datetime import timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

INPUT_DIR = "/data/raw/{{ ds }}"
INPUT_MODEL = Variable.get("trained_model_path")
OUTPUT_DIR = "/data/prediction/{{ ds }}"


default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "03-predict",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(30),
) as dag:

    predict = DockerOperator(
        image="airflow-predict",
        command=f"--input_dir {INPUT_DIR} --input_model {INPUT_MODEL} --output_dir {OUTPUT_DIR}",
        network_mode="bridge",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        volumes=["/home/vovan/MADE/ML-IN-PROD/vbakulev/airflow_ml_dags/data:/data"],
    )

    predict
