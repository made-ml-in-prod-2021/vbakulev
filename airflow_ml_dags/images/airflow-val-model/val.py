import os
import json
import pickle
from argparse import ArgumentParser

import pandas as pd

from sklearn.metrics import roc_auc_score


def parse_arguments():
    parser = ArgumentParser(__doc__)
    parser.add_argument(
        "--input_dir",
        help="directory for model_valn_data.csv",
    )
    parser.add_argument(
        "--input_model",
        help="directory for saving training model",
    )
    parser.add_argument(
        "--output_metric",
        help="directory for save metrics for validation madel",
    )
    return parser.parse_args()


def val_model(input_dir: str, input_model: str, output_metric: str):
    path_val_data_csv = os.path.join(input_dir, "model_val_data.csv")
    val_data_df = pd.read_csv(path_val_data_csv)

    path_input_model = os.path.join(input_model, "model.pkl")
    with open(path_input_model, "rb") as fin:
        clf = pickle.load(fin)

    predicts = clf.predict(val_data_df.iloc[:, :-1])
    target = val_data_df.iloc[:, -1]
    clf_metric = {"roc_auc": roc_auc_score(target, predicts)}

    path_output_metric = os.path.join(output_metric, "metric.json")
    with open(path_output_metric, "w") as fout:
        json.dump(clf_metric, fout)


if __name__ == '__main__':
    args = parse_arguments()
    val_model(args.input_dir, args.input_model, args.output_metric)
