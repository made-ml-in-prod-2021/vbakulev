from typing import List

import numpy as np
import pandas as pd
import pytest

from src.data.make_dataset import read_data
from src.entities.feature_params import FeatureParams
from src.features.build_features import extract_target, build_transformer


@pytest.fixture
def feature_params(
    categorical_features: List[str],
    numerical_features: List[str],
    target_col: str,
) -> FeatureParams:
    params = FeatureParams(
        categorical_features=categorical_features,
        numerical_features=numerical_features,
        target_col=target_col,
    )
    return params


def test_extract_features(feature_params: FeatureParams, dataset_path):
    data = read_data(dataset_path)
    target = extract_target(data, feature_params)
    assert all(data[feature_params.target_col] == target)


def test_build_transformer(
    feature_params: FeatureParams, dataset_path,
):
    data = read_data(dataset_path)
    transformer = build_transformer(feature_params)
    transformer.fit(data)
    features = transformer.transform(data)
    assert not pd.isnull(features).any()
