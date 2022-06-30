### Описание проекта:

Проект позволяет интегрировать сайт Yatube в API-веб сервис для обмена данными в формате JSON.

### Инструкция для установки:
```
git clone git@github.com:lanazzk/api_final_yatube.git
```

```
cd yatube_api/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры запросов и ответов API:

## Получение публикаций
Получить список всех публикаций.
# _эндпойнт: /api/v1/posts/
# GET:

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
## Создание публикации
Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
# _эндпойнт: http://127.0.0.1:8000/api/v1/posts/
# POST

{
  "text": "string",
  "image": "string",
  "group": 0
}
## Получение публикации по id.
# _эндпойнт: http://127.0.0.1:8000/api/v1/posts/{id}/
# GET
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
