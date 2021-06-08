import os
import pickle
from argparse import ArgumentParser

import pandas as pd

from sklearn.linear_model import LogisticRegression


def parse_arguments():
    parser = ArgumentParser(__doc__)
    parser.add_argument(
        "--input_dir",
        help="directory for model_train_data.csv",
    )
    parser.add_argument(
        "--output_model",
        help="directory for save training model",
    )
    return parser.parse_args()


def train_model(input_dir: str, output_model: str):
    path_train_data_csv = os.path.join(input_dir, "model_train_data.csv")
    train_data_df = pd.read_csv(path_train_data_csv)

    clf = LogisticRegression()
    clf.fit(train_data_df.iloc[:, :-1], train_data_df.iloc[:, -1])

    os.makedirs(output_model, exist_ok=True)
    path_output_model = os.path.join(output_model, "model.pkl")
    with open(path_output_model, "wb") as fout:
        pickle.dump(clf, fout)


if __name__ == '__main__':
    args = parse_arguments()
    train_model(args.input_dir, args.output_model)
