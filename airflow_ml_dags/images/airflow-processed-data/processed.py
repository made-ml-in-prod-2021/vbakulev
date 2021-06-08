import os

from argparse import ArgumentParser

import pandas as pd


def parse_arguments():
    parser = ArgumentParser(__doc__)
    parser.add_argument(
        "--input_dir",
        help="directory for data.csv and target.csv",
    )
    parser.add_argument(
        "--output_dir",
        help="output directory for preprocessing data",
    )
    return parser.parse_args()


def processed_data(input_dir: str, output_dir: str):
    path_data_csv = os.path.join(input_dir, "data.csv")
    path_target_csv = os.path.join(input_dir, "target.csv")
    data_df = pd.read_csv(path_data_csv)
    target_df = pd.read_csv(path_target_csv)

    os.makedirs(output_dir, exist_ok=True)
    train_data_df = pd.concat([data_df, target_df], axis=1)
    path_train_data_csv = os.path.join(output_dir, "train_data.csv")
    train_data_df.to_csv(path_train_data_csv, index=False)


if __name__ == '__main__':
    args = parse_arguments()
    processed_data(args.input_dir, args.output_dir)
