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
# Примеры запросов и ответов API:

## Получение публикаций
Получить список всех публикаций с пагинацией.
### _эндпойнт: /api/v1/posts/
**GET:**
```
{
    "count": 7,
    "next": null,
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=10",
    "results": [
        {
            "id": 6,
            "author": "user1",
            "text": "text3",
            "pub_date": "2022-06-30T12:09:17.996467Z",
            "image": null,
            "group": null
    }
}
```
## Создание публикации
Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
### _эндпойнт: http://127.0.0.1:8000/api/v1/posts/
**POST**
```
{
    "id": 9,
    "author": "user1",
    "text": "text5",
    "pub_date": "2022-06-30T12:13:24.117423Z",
    "image": null,
    "group": null
}
```
## Получение публикации по id.
# _эндпойнт: http://127.0.0.1:8000/api/v1/posts/{id}/
**GET**
```
{
    "id": 3,
    "author": "admin",
    "text": "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs",
    "pub_date": "2022-06-27T19:48:50.448219Z",
    "image": null,
    "group": 1
}
```
## Получение всех комментариев к публикации.
# _эндпойнт: http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
**GET**
```
[
    {
        "id": 2,
        "author": "user1",
        "post": 2,
        "text": "comment2",
        "created": "2022-06-27T19:59:07.043435Z"
    },
    {
        "id": 4,
        "author": "admin",
        "post": 2,
        "text": "Test",
        "created": "2022-06-27T20:09:54.268625Z"
    }
]
```
## Подписки
Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.Возможен поиск по подпискам по параметру search
# _эндпойнт: http://127.0.0.1:8000/api/v1/follow/
**GET**
```
[
    {
        "id": 1,
        "user": "user1",
        "following": "admin"
    },
    {
        "id": 3,
        "user": "user1",
        "following": "user2"
    }
]
```
