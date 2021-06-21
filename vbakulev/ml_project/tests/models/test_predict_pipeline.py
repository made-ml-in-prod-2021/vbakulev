import os
from typing import List

from py._path.local import LocalPath

from src.data import read_data
from src.models import load_model
from src.models.predict_pipeline import predict_pipeline
from src.entities import (
    SplittingParams,
    FeatureParams,
    PredictPipelineParams,
)

def test_predict(
    dataset_path: str,
):
    params = PredictPipelineParams(
        input_data_path=dataset_path,
        model_path="ml_project/models/model_log_reg.pkl",
        output_predict_path="ml_project/results/test_predict.csv"
    )
    predicts = predict_pipeline(params)
    assert os.path.exists(params.output_predict_path)
    assert len(predicts) > 0
