import os
import requests

from flask import Flask, jsonify
from concurrent.futures import ThreadPoolExecutor


URL = os.environ.get('PRODUCER_URL', 'http://0.0.0.0:8080')
app = Flask(__name__)


def get(url):
    try:
        data = []
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            data = response.json()
    except requests.exceptions.RequestException:
        data = []

    return data


@app.route('/fetch-async', methods=['GET'])
def fetch_async():
    """
    Получаемое значение:
    [
        {
            "name": "Test ...",
            "id": ...,
            "file": "..."
        },
        ...
    ]

    Задача реализова через потоки. Из за наличия GIL
    выполнение не является параллельным, вместо этого
    постоянно переключается контекст. Идея в том, что
    запросы отправляются единовременно при запуске
    потоков.

    Затем, я дожидаюсь всех ответов от сервера и отправляю
    в ответе сортированные данные
    :return:
    """
    urn = [
        f'{URL}/first',
        f'{URL}/second',
        f'{URL}/third',
        f'{URL}/fourth'
    ]
    with ThreadPoolExecutor() as executor:
        features = executor.map(get, urn)

        results = []
        for data in features:
            results.extend(data)

        results.sort(key=lambda item: item['id'])
        return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
