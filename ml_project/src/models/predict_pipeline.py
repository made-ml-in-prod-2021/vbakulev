import json
import logging
import sys
from argparse import ArgumentParser

import pandas as pd

from src.data import read_data, split_train_val_data
from src.entities.predict_pipeline_params import (
    PredictPipelineParams,
    read_predict_pipeline_params,
)

from src.features.build_features import extract_target, build_transformer
from src.models import (
    train_model,
    serialize_model,
    predict_model,
    evaluate_model,
    load_model,
)


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


DEFAULT_CONFIG_PATH = "ml_project/configs/predict_config.yaml"


def parse_arguments():
    parser = ArgumentParser(__doc__)
    parser.add_argument(
        "--config_path",
        help="path to predicting configuration .yml",
        default=DEFAULT_CONFIG_PATH
    )
    return parser.parse_args()


def predict_pipeline(predict_pipeline_params: PredictPipelineParams):
    logger.info("start predict pipeline")
    data = read_data(predict_pipeline_params.input_data_path)
    logger.info(f"input data.shape is {data.shape}")

    model = load_model(predict_pipeline_params.model_path)
    logger.info("Model loading has finished. ")

    predicts = predict_model(model, data)
    logger.info("Model predicting has finished. ")

    logger.info(f"Save prediction in {predict_pipeline_params.output_predict_path}")
    pd.DataFrame({"target": predicts}).to_csv(predict_pipeline_params.output_predict_path, index=False)
    logger.info("DONE!")


def predict_pipeline_command(config_path: str):
    params = read_predict_pipeline_params(config_path)
    predict_pipeline(params)


if __name__ == "__main__":
    args = parse_arguments()
    predict_pipeline_command(args.config_path)

