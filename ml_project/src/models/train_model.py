import pickle
from typing import Dict, Union

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

from src.entities.train_params import TrainingParams


SklearnClassifierModel = Union[LogisticRegression, RandomForestClassifier]


def train_model(
    features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
) -> SklearnClassifierModel :
    if train_params.model_type == "LogisticRegression":
        model = LogisticRegression()
    elif train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(
            n_estimators=100, random_state=train_params.random_state
        )
    else:
        raise NotImplementedError()
    model.fit(features, target)
    return model


def predict_model(
    model: SklearnClassifierModel, features: pd.DataFrame, use_log_trick: bool = True
) -> np.ndarray:
    predicts = model.predict(features)
    return predicts


def evaluate_model(
    predicts: np.ndarray, target: pd.Series, use_log_trick: bool = False
) -> Dict[str, float]:
    return {
        "roc_auc": roc_auc_score(target, predicts),
    }


def serialize_model(model: SklearnClassifierModel, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output
