from urllib.parse import quote

class Vacancy:
    """Класс для работы с вакансиями
    приводит их к единому формату и добавлены магические методы
    для сортировки вакансий по уровню заработной платы
    """
    def __init__(self, job_name: str, salary: int, description: int, link: str, salary_currency: str):
        """
        Создает экземпляр класса Vacancy.

        :param job_name: Название вакансии.
        :param salary: Заработная плата.
        :param description: Описание вакансии.
        :param link: Ссылка на вакансию.
        :param salary_currency: Валюта заработной платы.
        """
        self.job_name = job_name
        self.salary = salary
        self.salary_currency = salary_currency
        self.description = description
        self.link = link

    def __eq__(self, other):
        """
        Проверяет, равна ли заработная плата данной вакансии заработной плате другой вакансии.

        :param other: Другая вакансия.
        :return: True, если заработная плата равна, иначе - False.
        """
        if isinstance(other, Vacancy):
            return self.salary == other.salary

    def __gt__(self, other):
        """
        Проверяет, является ли заработная плата данной вакансии больше заработной платы другой вакансии.

        :param other: Другая вакансия.
        :return: True, если заработная плата больше, иначе - False.
        """
        if isinstance(other, Vacancy):
            return self.salary > other.salary

    def __lt__(self, other):
        """
        Проверяет, является ли заработная плата данной вакансии меньше заработной платы другой вакансии.

        :param other: Другая вакансия.
        :return: True, если заработная плата меньше, иначе - False.
        """
        if isinstance(other, Vacancy):
            return self.salary < other.salary

    def __str__(self):
        """
        Возвращает строковое представление вакансии.

        :return: Строковое представление вакансии.
        """
        return f'Вакансия: {self.job_name}\n'\
               f'Описание вакансии: {self.description}\n'\
               f'Заработная плата: {self.salary} {self.salary_currency}\n'\
               f'Ссылка на вакансию: {self.link}\n'

    def to_dict(self):
        """
        Преобразует вакансию в словарь.

        :return: Словарь, представляющий вакансию.
        """
        return {
            'job_name': self.job_name,
            'salary': self.salary,
            'salary_currency': self.salary_currency,
            'description': self.description,
            'link': quote(self.link)}
