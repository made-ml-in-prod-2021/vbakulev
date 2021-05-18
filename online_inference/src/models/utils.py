import sys
import logging
import pickle
from typing import List, Union, Optional

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

from src.models.app_data import (
    HeartModel,
    HeartResponse,
)


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def load_object(path: str) -> Pipeline:
    logger.info(f"Load model from path {path}")
    with open(path, "rb") as fin:
        model = pickle.load(fin)
    return model


def make_predict(
    data: List, features: List[str], model: Pipeline,
) -> List[HeartResponse]:
    data = pd.DataFrame(data, columns=features)
    logger.info(f"Make predict for data {data.to_string()}")
    data["target"] = np.zeros((len(data),), dtype=int)
    predicts = model.predict(data)

    return [
        HeartResponse(target=int(target)) for target in predicts
    ]
