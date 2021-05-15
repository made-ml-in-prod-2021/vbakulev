import logging
import sys

from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from src.entities import SplittingParams


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def read_data(path: str) -> pd.DataFrame:
    logger.info(f"Reading dataset from {path}")
    data = pd.read_csv(path)
    logger.info("Dataset read successfully!")
    return data


def split_train_val_data(
    data: pd.DataFrame, params: SplittingParams
) -> Tuple[pd.DataFrame, pd.DataFrame]:

    logger.info(f"Split datasets into training and validation parts. The validation part is {params.val_size * 100} percent")
    train_data, val_data = train_test_split(
        data, test_size=params.val_size, random_state=params.random_state
    )
    logger.info(f"Dataset split successfully!")
    return train_data, val_data
