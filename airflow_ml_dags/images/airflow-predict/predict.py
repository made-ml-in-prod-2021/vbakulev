import os
import pickle
from argparse import ArgumentParser

import pandas as pd


def parse_arguments():
    parser = ArgumentParser(__doc__)
    parser.add_argument(
        "--input_dir",
        help="directory for input data.csv",
    )
    parser.add_argument(
        "--input_model",
        help="directory for saving training model",
    )
    parser.add_argument(
        "--output_dir",
        help="directory for save prediction target",
    )
    return parser.parse_args()


def predict(input_dir: str, input_model: str, output_dir: str):
    path_data_csv = os.path.join(input_dir, "data.csv")
    data_df = pd.read_csv(path_data_csv)

    path_input_model = os.path.join(input_model, "model.pkl")
    with open(path_input_model, "rb") as fin:
        clf = pickle.load(fin)

    predict_target = clf.predict(data_df)
    predict_df = pd.DataFrame({"target": predict_target})

    os.makedirs(output_dir, exist_ok=True)
    path_output_predict = os.path.join(output_dir, "predictions.csv")
    predict_df.to_csv(path_output_predict, index=False)


if __name__ == '__main__':
    args = parse_arguments()
    predict(args.input_dir, args.input_model, args.output_dir)
