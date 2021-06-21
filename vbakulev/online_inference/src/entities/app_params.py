from dataclasses import dataclass, field
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class AppParams:
    model_path: str = field(default="online_inference/models/model.pkl")


AppParamsSchema = class_schema(AppParams)


def read_app_params(path: str) -> AppParams:
    with open(path, "r") as input_stream:
        schema = AppParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
