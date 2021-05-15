import os
from typing import List

from py._path.local import LocalPath

from src.models.train_pipeline import train_pipeline
from src.entities import (
    TrainingPipelineParams,
    SplittingParams,
    FeatureParams,
    TrainingParams,
)


def test_train_e2e(
    tmpdir: LocalPath,
    train_dataset_path: str,
    categorical_features: List[str],
    numerical_features: List[str],
    target_col: str,
):
    expected_output_model_path = tmpdir.join("model.pkl")
    expected_metric_path = tmpdir.join("metrics.json")
    params = TrainingPipelineParams(
        input_data_path=train_dataset_path,
        output_model_path=expected_output_model_path,
        metric_path=expected_metric_path,
        splitting_params=SplittingParams(val_size=0.2, random_state=42),
        feature_params=FeatureParams(
            numerical_features=numerical_features,
            categorical_features=categorical_features,
            target_col=target_col,
        ),
        train_params=TrainingParams(model_type="RandomForestClassifier"),
    )
    real_model_path, metrics = train_pipeline(params)
    assert metrics["roc_auc"] > 0
    assert metrics["accuracy"] > 0
    assert metrics["precision"] > 0
    assert metrics["recall"] > 0
    assert metrics["f1"] > 0
    assert os.path.exists(real_model_path)
    assert os.path.exists(params.metric_path)
