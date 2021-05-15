import os
import pickle
from typing import List, Tuple

import pandas as pd
import pytest
from py._path.local import LocalPath
from sklearn.ensemble import RandomForestClassifier

from src.data.make_dataset import read_data
from src.entities import TrainingParams
from src.entities.feature_params import FeatureParams
from src.features.build_features import extract_target, build_transformer
from src.models.model_fit_predict import train_model, serialize_model


def test_train_model(
    train_dataset_path: str, categorical_features: List[str], numerical_features: List[str]
):
    params = FeatureParams(
        categorical_features=categorical_features,
        numerical_features=numerical_features,
        target_col="target",
    )
    data = read_data(train_dataset_path)
    target = extract_target(data, params)
    transformer = build_transformer(params)
    model = train_model(transformer, data, target, train_params=TrainingParams())
    assert model.predict(data).shape[0] == target.shape[0]


def test_serialize_model(tmpdir: LocalPath):
    expected_output = tmpdir.join("model.pkl")
    n_estimators = 10
    model = RandomForestClassifier(n_estimators=n_estimators)
    real_output = serialize_model(model, expected_output)
    assert real_output == expected_output
    assert os.path.exists
    with open(real_output, "rb") as f:
        model = pickle.load(f)
    assert isinstance(model, RandomForestClassifier)
