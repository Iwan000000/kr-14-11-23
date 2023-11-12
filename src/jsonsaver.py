import json
import os


class JsonSaver:
    """Класс для работы с файлами
    сохраняет, выводит и удаляет вакансии"""
    def __init__(self, filename):
        """
        Инициализация объекта JsonSaver.

        :param filename:Имя файла для работы с вакансиями.
        """
        self.__filename = filename

    @property
    def file(self):
        """
        Возвращает имя файла.

        :return: Имя файла.
        """
        return self.__filename

    @file.setter
    def file(self, name):
        """
        Устанавливает имя файла.

        :param name: Новое имя файла.
        """
        self.__filename = name

    def __str__(self):
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта
        """
        with open(self.__filename, 'r', encoding='utf-8') as f:
            data = f.readlines()
            objects = [json.loads(obj) for obj in data]
            return str(objects)

    def writer_data(self, data):
        """
        Записывает данные в файл.

        :param data: Данные для записи.
        """
        with open(self.__filename, 'a', encoding='utf-8') as f:
            json.dump(data.to_dict(), f, ensure_ascii=False)
            f.write('\n')#разделяет сохраннёные вакансии пустой строко


    def get_vacancies(self, keyword): #выводит вакансии, если пустая строка, то выведет все, если есть ключевое слово, то выведет по нему
        """
        Возвращает вакансии.

        :param keyword: Ключевое слово для поиска вакансий.
        :return: Список вакансий.
        """
        vacancies = []
        with open( self.__filename, 'r', encoding='utf-8') as f:

            for item in f:
                vacancy = json.loads(item)
                if keyword is None or keyword in vacancy.get('job_name', ''):
                    vacancies.append(vacancy)
        return vacancies


    def delete_vacancy(self, keyword):
        """
        Удаляет вакансии по ключевому слову, или удаляют все при введении пустой строки

        :param keyword: Ключевое слово для фильтрации вакансий
        :return: None
        """
        if keyword is None or keyword.strip() == '':
            open(self.__filename, 'w').close()
        else:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            with open(self.__filename, 'w', encoding='utf-8') as f:
                for line in lines:
                    vacancy = json.loads(line)
                    if keyword not in vacancy.get('job_name', ''):
                        json.dump(vacancy, f, ensure_ascii=False)
                        f.write('\n')

    def update_vacancy(self, keyword, new_data):
        """
        Обновляет данные о вакансии.

        :param keyword: Ключевое слово для поиска вакансии, которую нужно обновить.
        :param new_data: Новые данные для обновления.
        """
        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = [json.loads(line) for line in file if line.strip()]

        updated_data = [item if keyword not in item['job_name'] else new_data for item in data]

        with open(self.__filename, 'w', encoding='utf-8') as file:
            for item in updated_data:
                json.dump(item, file, ensure_ascii=False)
                file.write('\n')
