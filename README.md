# async requests

Сервис с двумя веб приложениями
1. producer - Имеет 4 API (/first /second /third /fourth)
2. fetcher - центральный endpoint /fetch-async

Поведение API Producer:
1. /first Нормальный ответ
2. /second Простой 5 сек
3. /third Нормальный ответ
4. /fourth Ответ с ошибкой 500 Internal Server Error

Fetcher выполняет запросы асинхронно по 4 api с условиями:
 - игнорирует запросы со временем выполнения > 2 cек
 - игнорирует ошибки

Порты:
 - fetcher 7070:7070
 - reducer 8080:8080

> Producer запускает 4 воркера!  

### Запуск

- Клонируем проект `git clone`
- В директории с репозиторием`docker-compose build`
- Выполняем `docker-compose up -d`
- По завершении работы отключаем `docker-compose down`

[/fetch-async](https://127.0.0.1:7070/fetch-async)
[/first](https://127.0.0.1:8080/first)
[/second](https://127.0.0.1:8080/second)
[/third](https://127.0.0.1:8080/third)
[/four](https://127.0.0.1:8080/four)
