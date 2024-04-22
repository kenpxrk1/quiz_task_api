# Тестовое задание quiz_api

### Требования: 

Реализовать на Python3 веб сервис (с помощью ***FastAPI*** или ***Flask***, например), выполняющий следующие функции:

1. В сервисе должно быть реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}.
2. После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) [https://jservice.io/api/random?count=1](https://jservice.io/api/random?count=1) указанное в полученном запросе количество вопросов.
3. Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки):
      - ID вопроса,
      - Текст вопроса,
      - Текст ответа,
      - Дата создания вопроса.
      
      В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
4. Ответом на запрос из п.1 должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

***!!! Было принято решение воспользоваться аналогичным API по адресу [https://quizapi.io/api/v1/questions](https://quizapi.io/api/v1/questions)

## Стек:

![FastAPI](https://img.shields.io/badge/FastAPI-0.110.2-cyan?style=flat&logo=FastAPI&logoColor=cyan)
![Python](https://img.shields.io/badge/Python-3.10-brightgreen?style=flat&logo=Python&logoColor=brightgreen)
![SqlAlchemy](https://img.shields.io/badge/SqlAlchemy-2.0.20-brightgreen?style=flat&logo=python&logoColor=brightgreen)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15.5-blue?style=flat&logo=postgresql&logoColor=blue)
![Docker](https://img.shields.io/badge/Docker_compose-grey?style=flat&logo=docker&logoColor=blue)

## Зависимости: 

- docker 

- docker-compose


## Инструкция по установке и запуску приложения: 

Клонируйте репозиторий:
```sh
$ git clone https://github.com/kenpxrk1/quiz-task-api
```

Запустите приложение из корневой папки с помощью docker-compose:

```sh
$ docker compose build
```

```sh
$ docker compose up
```


### После установки и запуска, приложение станет доступно по адресу: 

`http://127.0.0.1:9999/docs`

