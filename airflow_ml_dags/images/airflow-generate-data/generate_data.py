import os

from argparse import ArgumentParser
import random

import pandas as pd

DATASET_SIZE = 100
SEED = 42


MIN_FEATURE_1, MAX_FEATURE_1 = 10, 100
MIN_FEATURE_2, MAX_FEATURE_2 = 1, 200
MIN_FEATURE_3, MAX_FEATURE_3 = 50, 500
MIN_FEATURE_4, MAX_FEATURE_4 = 1, 23
MIN_FEATURE_5, MAX_FEATURE_5 = 4, 70
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
        "feature_1": [random.randint(MIN_FEATURE_1, MAX_FEATURE_1) for _ in range(DATASET_SIZE)],
        "feature_2": [random.randint(MIN_FEATURE_2, MAX_FEATURE_2) for _ in range(DATASET_SIZE)],
        "feature_3": [random.randint(MIN_FEATURE_3, MAX_FEATURE_3) for _ in range(DATASET_SIZE)],
        "feature_4": [random.randint(MIN_FEATURE_4, MAX_FEATURE_4) for _ in range(DATASET_SIZE)],
        "feature_5": [random.randint(MIN_FEATURE_5, MAX_FEATURE_5) for _ in range(DATASET_SIZE)],
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
