### Комментарий
Поскольку счетчиков не существует, для тестирования создана отдельная таблица SimulateCounter, где хранятся id счётчиков и их показания.
Через api счетчики добавляются и удаляются в таблицу Counter.
Показания снимаются каждые M секунд с помощью celery и хранятся в таблице CounterValue

### Описание проекта

Система учета электроэнергии на предприятии, на на котором установлено N пассивных счетчиков электроэнергии, каждый из счетчиков
возвращает по протоколу http (метод GET) следующие данные в формате JSON: {"id":"<id>",
"A":"50","kW":"44325"}, где
```
id – счетчика;
A – текущий ток (кол-во Ампер) потребления сети;
kW – суммарное потребление энергии (Киловатт) за все время работы.
```
Все счетчики находятся в одной сети (диапазон адресов 127.0.0.1:9000 - 127.0.0.1:65000)

### Стек технологий
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=696eb6&color=070b40)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=696eb6&color=070b40)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=696eb6&color=070b40)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=696eb6&color=070b40)](https://www.docker.com/)
![Celery](https://img.shields.io/badge/Celery-5.0-yellow)
![Redis](https://img.shields.io/badge/Redis-6.2-red)


### Авторы
Евгений Семашкевич. SemashkevichEA@yandex.ru


### Запуск проекта локально
Ссылка на скачивание проекта:
```
git@github.com:YauheniSA/test_electricity_meters_api.git
```

Cоздать и активировать виртуальное окружение:

```BASH
python -m venv venv
```

```BASH
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```BASH
python -m pip install --upgrade pip
```

```BASH
pip install -r requirements.txt
```

Выполнить миграции:

```BASH
python manage.py migrate
```

Запустить проект:

```BASH
python3 manage.py runserver
```

Запустить redis в контейнере docker:

```BASH
docker run -d -p 6379:6379 redis
```

Запустить celery worker:

```BASH
celery -A test_enterprise worker -l INFO --pool=solo
```

Запустить celery beat:

```BASH
celery -A test_enterprise beat -l INFO
```

После этого api для тестирования будет доступно по ссылке

```
http://127.0.0.1/
```


### Работа с API:

Добваление счётчика:
`POST http://127.0.0.1:8000/counter/`
```JSON
{
  "id": 66666,
  "port": 10102
}
```

Удаление счётчика:
`DELETE http://127.0.0.1:8000/counter/<id>/`


Получение актуальных показаний счетчика:
`GET http://127.0.0.1:8000/counter-data/<id>/`
Пример ответа:
```JSON
{
    "id": 44,
    "A": 21,
    "kW": 23
}
```


Получение статистики по счётчику за указнные период времени:
`GET http://127.0.0.1:8000/counter-archive/?counter_id=44&timestamp<2023-08-12 15:16:03.218952`
Пример ответа:
```JSON
[
    {
        "timestamp": 20,
        "A": 21,
        "kW": 23
    },
    {
        "timestamp": 44,
        "A": 21,
        "kW": 23
    },


]
```
