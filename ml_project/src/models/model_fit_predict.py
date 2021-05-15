import logging
import sys

import pickle
from typing import Dict, Union

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    roc_auc_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from src.entities.train_params import TrainingParams


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


SklearnClassifierModel = Union[LogisticRegression, RandomForestClassifier]


def train_model(
        transformer: ColumnTransformer,
        features: pd.DataFrame,
        target: pd.Series,
        train_params: TrainingParams
) -> SklearnClassifierModel :

    logger.info(f"Create model {train_params.model_type} ...")
    if train_params.model_type == "LogisticRegression":
        model = LogisticRegression()
    elif train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(
            n_estimators=100, random_state=train_params.random_state
        )
    else:
        raise NotImplementedError()

    model = Pipeline([('transform_features', transformer),
                        ('clf_model', model)
                       ])
    logger.info(f"Model fit...")
    model.fit(features, target)
    return model


def predict_model(
    model: SklearnClassifierModel, features: pd.DataFrame
) -> np.ndarray:
    logger.info(f"Model predict...")
    predicts = model.predict(features)
    return predicts


def evaluate_model(
    predicts: np.ndarray, target: pd.Series
) -> Dict[str, float]:
    logger.info(f"Model evaluate...")
    return {
        "roc_auc": roc_auc_score(target, predicts),
        "accuracy": accuracy_score(target, predicts),
        "precision": precision_score(target, predicts),
        "recall": recall_score(target, predicts),
        "f1": f1_score(target, predicts),
    }


def serialize_model(
        model: SklearnClassifierModel,
        output: str,
) -> str:
    logger.info(f"Model serialize...")
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output


def load_model(
        model_path: str
) -> SklearnClassifierModel:
    logger.info(f"Model load...")
    with open(model_path, "rb") as mp:
        model = pickle.load(mp)
    return model
