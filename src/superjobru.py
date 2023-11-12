import os
import requests
from basic_class import BasicClass

LINK = "https://api.superjob.ru/2.0/vacancies"

class SuperJobAPI(BasicClass):
    """Класс для скрайбинга сайта SJ
    возвращает список вакансий
    вакансия в json формате"""

    def get_request(self, keyword: str, count: int):
        """
        Отправляет запрос на API SuperJob и возвращает список вакансий.

        :param keyword: Ключевое слово для поиска вакансий.
        :param count: Количество вакансий для получения.
        :return: Список вакансий в формате JSON.
        """
        pages = int(count) / 1  # Округляем вверх, чтобы учесть ограничение по количеству вакансий на странице
        api_key = os.getenv('Api_App_Id')
        headers = {
            'X-Api-App-Id': api_key}
        data = []

        for page in range(int(pages)):
            params = {
                'keyword': keyword,
                'page': page,
                'count': 1  # Ограничение по количеству вакансий на странице
            }

            response = requests.get(LINK, params=params, headers=headers)

            if response.status_code == 200:
                data += response.json().get('objects', [])
            else:
                print(f"Error {response.status_code}: {response.text}")

        return data
