import requests
from basic_class import BasicClass


LINK = 'https://api.hh.ru/vacancies'

class HH_API(BasicClass):
    """Класс для скрайбинга сайта HH
    возвращает список вакансий
    вакансия в json формате"""

    def get_request(self, keyword: str, count: int):
        """
        Отправляет запрос на API HH и возвращает список вакансий.

        :param keyword: Ключевое слово для поиска вакансий.
        :param count: Количество вакансий для получения.
        :return: Список вакансий в формате JSON.
        """
        pages = int(count/1)  # Расчет количества страниц
        params = {
            'text': keyword,
            'page': 0,
            'per_page': 1
        }
        data = []
        for page in range(pages):
            params.update({'page': page})
            response = requests.get(LINK, params=params)
            if response.status_code == 200:  # Проверка успешности выполнения запроса
                data += response.json()['items']
            else:
                print(f"Ошибка при выполнении запроса. Статус код: {response.status_code}")

        return data
