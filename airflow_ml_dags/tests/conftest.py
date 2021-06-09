import pytest

from airflow.models import DagBag


@pytest.fixture()
def default_DAG():
    return DagBag(dag_folder="airflow_ml_dags/dags/")
