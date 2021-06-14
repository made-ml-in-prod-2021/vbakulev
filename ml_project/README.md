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


--------

Самооценка

0) Назовите ветку homework1 (+1)
0) Положите код в папку ml_project (+0)
0) В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе. В общем, описание что именно вы сделали и для чего, чтобы вашим ревьюерам было легче понять ваш код. (+2)
1) Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (+2)
2) Проект имеет модульную структуру (+2)
3) Использованы логгеры (+2)
4) Написаны тесты на отдельные модули и на прогон всего пайплайна(+3)
5) Для тестов генерируются синтетические данные, приближенные к реальным (+3)
6) Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (+3)
7) Используются датаклассы для сущностей из конфига, а не голые dict (+3)
9) Обучите модель, запишите в readme как это предлагается (+3)
10) Напишите функцию predict, которая примет на вход артефакт/ы от обучения, тестовую выборку (без меток) и запишет предикт, напишите в readme как это сделать (+3)

Проведите самооценку, опишите, в какое колво баллов по вашему мнению стоит оценить вашу работу и почему (+1)

Общее количество баллов 28 * 0,65 = 18,2
