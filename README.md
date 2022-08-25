# Проект: API для YAMDB

# Авторы проекта
**Антон**: https://github.com/Antony8720  
**Никита**: https://github.com/nikitapatrakov  
**Алексей**: https://github.com/bainter  

## Описание:

Проект "API для YAMDB" представляет собой интерфейс для обмена данными с сервисом YAMDB.

Он позволяет получать различные наборы данных, хранящихся в базе данных сервиса YAMDB и создавать новые данные внутри сервиса.

## Установка:

Для установки проекта на локальной машине необходимо:

1. Клонировать репозиторий и перейти в него в командной строке:  
`git clone git@github.com:Antony8720/api_yamdb.git`  
`cd api_yamdb`

2. Cоздать и активировать виртуальное окружение:  
`python3 -m venv env`  
`source env/bin/activate`

3. Установить зависимости из файла requirements.txt:  
`python3 -m pip install --upgrade pip`  
`pip install -r requirements.txt`

4. Выполнить миграции:  
`python3 manage.py migrate`

5. Запустить проект:  
`python3 manage.py runserver`

## Примеры запросов к API:

#### Получение списка всех произведений: GET http://127.0.0.1:8000/api/v1/titles/

#### Пример ответа:
```
{
  [
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]
}
```
#### Добавление новой категории: POST http://127.0.0.1:8000/api/v1/categories/
```
{
  "name": "string",
  "slug": "string"
}
```
#### Пример ответа:
```
{
  "name": "string",
  "slug": "string"
}
```
#### Полная документация:  
Полная документация по API доступна по адресу http://127.0.0.1:8000/redoc после запуска сервера
