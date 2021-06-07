import os

from argparse import ArgumentParser
import random

import pandas as pd

DATASET_SIZE = 10
SEED = 42

# NUMERICAL_FEATURES_PARAMS
MIN_AGE, MAX_AGE = 29, 77
MIN_TRESTBPS, MAX_TRESTBPS = 94, 200
MIN_CHOL, MAX_CHOL = 126, 564
MIN_THALACH, MAX_THALACH = 71, 202
MIN_OLDPEAK, MAX_OLDPEAK = 0., 6.2

# CATEGORICAL_FEATURES_PARAMS
LIST_SEX = [1, 0]
LIST_CP = [3, 2, 1, 0]
LIST_FBS = [1, 0]
LIST_RESTECG = 	[0, 1, 2]
LIST_EXANG = [0, 1]
LIST_SLOPE = [0, 2, 1]
LIST_CA = [0, 2, 1, 3, 4]
LIST_THAL =[1, 2, 3, 0]

# TARGET
LIST_TARGET = [0, 1]


def parse_arguments():
    parser = ArgumentParser(__doc__)
    parser.add_argument(
        "--output_dir",
        help="output directory for generated data",
    )
    return parser.parse_args()


def generate_data(output_dir: str):
    random.seed(SEED)
    df = pd.DataFrame({
        "age": [random.randint(MIN_AGE, MAX_AGE) for _ in range(DATASET_SIZE)],
        "sex": [random.choice(LIST_SEX) for _ in range(DATASET_SIZE)],
        "cp": [random.choice(LIST_CP) for _ in range(DATASET_SIZE)],
        "trestbps": [random.randint(MIN_TRESTBPS, MAX_TRESTBPS) for _ in range(DATASET_SIZE)],
        "chol": [random.randint(MIN_CHOL, MAX_CHOL) for _ in range(DATASET_SIZE)],
        "fbs": [random.choice(LIST_FBS) for _ in range(DATASET_SIZE)],
        "restecg": [random.choice(LIST_RESTECG) for _ in range(DATASET_SIZE)],
        "thalach": [random.randint(MIN_THALACH, MAX_THALACH) for _ in range(DATASET_SIZE)],
        "exang": [random.choice(LIST_EXANG) for _ in range(DATASET_SIZE)],
        "oldpeak": [random.uniform(MIN_OLDPEAK, MAX_OLDPEAK) for _ in range(DATASET_SIZE)],
        "slope": [random.choice(LIST_SLOPE) for _ in range(DATASET_SIZE)],
        "ca": [random.choice(LIST_CA) for _ in range(DATASET_SIZE)],
        "thal": [random.choice(LIST_THAL) for _ in range(DATASET_SIZE)],
        "target": [random.choice(LIST_TARGET) for _ in range(DATASET_SIZE)],
    })
    os.makedirs(output_dir, exist_ok=True)
    path_data_csv = os.path.join(output_dir, "data.csv")
    path_target_csv = os.path.join(output_dir, "target.csv")
    df.iloc[:, :-1].to_csv(path_data_csv, index=False)
    df.iloc[:, -1].to_csv(path_target_csv, index=False)


if __name__ == '__main__':
    args = parse_arguments()
    generate_data(args.output_dir)
