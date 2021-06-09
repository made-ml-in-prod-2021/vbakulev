def test_train(default_DAG):
    dag = default_DAG.dags["02-train"]
    assert dag is not None
    assert len(dag.tasks) == 4
