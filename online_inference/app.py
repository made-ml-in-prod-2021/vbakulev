import sys
import logging
import os
import pickle
from typing import List, Optional

import uvicorn
from fastapi import FastAPI
from sklearn.pipeline import Pipeline

from src.entities.app_params import read_app_params
from src.models.utils import (
    load_object,
    make_predict,
)
from src.models.app_data import (
    HeartModel,
    HeartResponse,
)


CONFIG_PATH = "configs/app_config.yaml"


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


model: Optional[Pipeline] = None
app = FastAPI()


@app.get("/")
def main():
    return "Hello! This is model for predict Heart Disease UCI"


@app.on_event("startup")
def load_model():
    global model
    params = read_app_params(CONFIG_PATH)
    if params.model_path is None:
        err = f"PATH_TO_MODEL {params.model_path} is None"
        logger.error(err)
        raise RuntimeError(err)

    model = load_object(params.model_path)


@app.get("/health")
def health() -> bool:
    return not (model is None)


@app.get("/predict", response_model=List[HeartResponse])
def predict(request: HeartModel):
    return make_predict(request.data, request.features, model)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000)
