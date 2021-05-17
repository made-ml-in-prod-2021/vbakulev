import sys
import logging
import os

import random
import numpy as np
import pandas as pd
import requests


DATA_PATH = "./data/raw/heart.csv"
COUNT_REQUEST = 10


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def main():
    data = pd.read_csv(DATA_PATH)
    request_features = list(data.columns)
    list_idx = random.sample(range(data.shape[0]), COUNT_REQUEST)
    for i in list_idx:
        request_data = [
            x.item() if isinstance(x, np.generic) else x for x in data.iloc[i].tolist()
        ]
        logger.info(request_data)
        response = requests.get(
            "http://127.0.0.1:8000/predict/",
            json={"data": [request_data], "features": request_features},
        )
        logger.info(response.status_code)
        logger.info(response.json())


if __name__ == "__main__":
    main()
