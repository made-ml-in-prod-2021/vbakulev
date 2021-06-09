def test_generate_data(default_DAG):
    dag = default_DAG.dags["01-generate-data"]
    assert dag is not None
    assert len(dag.tasks) == 1
