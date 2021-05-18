online_inference
==============================

Cборка Docker-контейнера: 
~~~
docker build -t vbakulev/online_inference:v1 ./online_inference

docker login
docker push vbakulev/online_inference:v1
~~~

Загрузка и запуск Docker-контейнера: 
~~~
docker pull vbakulev/online_inference:v1
docker run -p 8000:8000 vbakulev/online_inference:v1
~~~


Самооценка
------------

0) Ветку назовите homework2, положите код в папку online_inference (+0)

1) Оберните inference вашей модели в rest сервис(вы можете использовать как FastAPI, так и flask, другие желательно не использовать, дабы не плодить излишнего разнообразия для проверяющих), должен быть endpoint /predict (+3)

2) Напишите тест для /predict (+3)

3) Напишите скрипт, который будет делать запросы к вашему сервису (+2)

4) Напишите dockerfile, соберите на его основе образ и запустите локально контейнер(docker build, docker run), внутри контейнера должен запускать сервис, написанный в предущем пункте, закоммитьте его, напишите в readme корректную команду сборки (+4)

5) Опубликуйте образ в https://hub.docker.com/, используя docker push (+2)

6) Напишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель (+1)

7) Проведите самооценку (+1)

8) Создайте пулл-реквест и поставьте label -- hw2 (+0)


Общее количество баллов: 16
