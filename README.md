### Description of project:
  This project allowed integrate web-site Yatube into API-web service for changing of data in JSON format.
  

### Installation:
```
git clone git@github.com:lanazzk/api_final_yatube.git
```

```
cd yatube_api/
```

Create and activate virtual environment:

```
python -m venv env
```

```
For macOS or Linux: source venv/bin/activate, for Windows: source venv/Scripts/activate
```

Install dependencies from requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Execute migrations:

```
python manage.py migrate
```

Launch project:

```
python manage.py runserver
```

# Examples of API requests:

## Get all publictions with pagination:

### _url: /api/v1/posts/

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

## Create publication
Create publication. Anonimous requests not allowed.

### _url: /api/v1/posts/

**POST:**
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

## Get publication.
### _url: /api/v1/posts/{id}/

**GET:**
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

## Get comments.
### _url: /api/v1/posts/{post_id}/comments/

**GET:**
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

## Followers

### _url: /api/v1/follow/

**GET:**
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
