from abc import ABC, abstractmethod


class BasicClass(ABC):
    @abstractmethod
    def get_request(self, keywords, count):
        """
        Абстрактный метод для выполнения запроса и получения данных.

        :param keywords:Ключевые слова для поискового запроса.
        :param count:Количество результатов, которое необходимо получить.
        :return:Список данных, полученных в результате запроса.
        """
        pass
