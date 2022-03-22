# async requests

Сервис с двумя веб приложениями
1. producer - Имеет 4 API (/first /second /third /fourth)
2. fetcher - центральный endpoint /fetch-async

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