<<<<<<< HEAD
Чтобы развернуть airflow, предварительно собрав контейнеры
~~~
# для корректной работы с переменными, созданными из UI
export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")

docker compose up --build
~~~
Ссылка на документацию по docker compose up

https://docs.docker.com/compose/reference/up/
=======
Чтобы развернуть airflow, предварительно собрав контейнеры
~~~
# для корректной работы с переменными, созданными из UI
export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")

docker compose up --build
~~~
Ссылка на документацию по docker compose up

https://docs.docker.com/compose/reference/up/


Самооценка:

0) (0 баллов) Поднимите airflow локально, используя docker compose 

1) (5 баллов) Реализуйте dag, который генерирует данные для обучения модели. Вам важно проэмулировать ситуации постоянно поступающих данных
- записывайте данные в /data/raw/{{ ds }}/data.csv, /data/raw/{{ ds }}/target.csv

2) (10 баллов) Реализуйте dag, который обучает модель еженедельно, используя данные за текущий день. В вашем пайплайне должно быть как минимум 4 стадии:
- подготовить данные для обучения(например, считать из /data/raw/{{ ds }} и положить /data/processed/{{ ds }}/train_data.csv)
- расплитить их на train/val
- обучить модель на train (сохранить в /data/models/{{ ds }} 
- провалидировать модель на val (сохранить метрики к модельке)

3) (5 баллов) Реализуйте dag, который использует модель ежедневно 
- принимает на вход данные из пункта 1 (data.csv)
- считывает путь до модельки из airflow variables(идея в том, что когда нам нравится другая модель и мы хотим ее на прод 
- делает предсказание и записывает их в /data/predictions/{{ ds }}/predictions.csv

4) (10 баллов)вы можете выбрать 2 пути для выполнения ДЗ. 
- все даги реализованы только с помощью DockerOperator. 

5) (5 баллов) Протестируйте ваши даги

6) (1 балл) Самооценка 

Общее количество баллов: 36
>>>>>>> 7b5e59af19f9c1508124d5e498f656d22d2575da
