import json
import logging
import sys
from argparse import ArgumentParser

from src.data import read_data, split_train_val_data
from src.entities.train_pipeline_params import (
    TrainingPipelineParams,
    read_training_pipeline_params,
)

from src.features.build_features import extract_target, build_transformer
from src.models import (
    train_model,
    serialize_model,
    predict_model,
    evaluate_model,
)


DEFAULT_CONFIG_PATH = "ml_project/configs/train_log_reg_config.yaml"


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def parse_arguments():
    parser = ArgumentParser(__doc__)
    parser.add_argument(
        "--config_path",
        help="path to training configuration .yml",
        default=DEFAULT_CONFIG_PATH
    )
    return parser.parse_args()


def train_pipeline(training_pipeline_params: TrainingPipelineParams):
    logger.info(f"start train pipeline with params {training_pipeline_params}")
    data = read_data(training_pipeline_params.input_data_path)
    logger.info(f"data.shape is {data.shape}")

    train_df, val_df = split_train_val_data(
        data, training_pipeline_params.splitting_params
    )
    logger.info(f"train_df.shape is {train_df.shape}")
    logger.info(f"val_df.shape is {val_df.shape}")

    transformer = build_transformer(training_pipeline_params.feature_params)
    train_target = extract_target(train_df, training_pipeline_params.feature_params)

    model = train_model(
        transformer, train_df, train_target, training_pipeline_params.train_params
    )

    val_target = extract_target(val_df, training_pipeline_params.feature_params)
    predicts = predict_model(
        model,
        val_df,
    )

    metrics = evaluate_model(
        predicts,
        val_target,
    )

    with open(training_pipeline_params.metric_path, "w") as metric_file:
        json.dump(metrics, metric_file)
    logger.info(f"metrics is {metrics}")

    path_to_model = serialize_model(model, training_pipeline_params.output_model_path)

    return path_to_model, metrics


def train_pipeline_command(config_path: str):
    params = read_training_pipeline_params(config_path)
    train_pipeline(params)


if __name__ == "__main__":
    args = parse_arguments()
    train_pipeline_command(args.config_path)
