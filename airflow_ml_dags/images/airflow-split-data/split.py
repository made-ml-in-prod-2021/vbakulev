import os

from argparse import ArgumentParser

import pandas as pd
from sklearn.model_selection import train_test_split


def parse_arguments():
    parser = ArgumentParser(__doc__)
    parser.add_argument(
        "--input_dir",
        help="directory for preprocessing train_data.csv",
    )
    return parser.parse_args()


def split_data(input_dir: str):
    path_train_data_csv = os.path.join(input_dir, "train_data.csv")
    train_data_df = pd.read_csv(path_train_data_csv)

    model_train_df, model_val_df = train_test_split(train_data_df, test_size=0.3)

    path_model_train_csv = os.path.join(input_dir, "model_train_data.csv")
    path_model_val_csv = os.path.join(input_dir, "model_val_data.csv")

    model_train_df.to_csv(path_model_train_csv, index=False)
    model_val_df.to_csv(path_model_val_csv, index=False)


if __name__ == '__main__':
    args = parse_arguments()
    split_data(args.input_dir)
