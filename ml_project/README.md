ml_project
==============================

Installation: 
~~~
python -m venv .venv
source .venv/bin/activate
pip install -e .
~~~
Usage:
~~~
python ml_project/train_pipeline.py configs/train_model_config.yaml
python ml_project/predict_pipeline.py configs/predict_config.yaml
~~~

Test:
~~~
pytest tests/
~~~

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    |
    ├── configs            <- configuration model in .yaml
    |
    ├── data
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    |
    ├── results            <- result of model prediction
    |
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- code to download or generate data
    │   │
    │   ├── entities           <- code to model entities
    │   │
    │   ├── features       <- code to turn raw data into features for modeling
    │   │
    │   ├── models         <- code to train models and then use trained models to make
    |
    ├── tests                <- Source code for tests.

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
