import pytest

from src.vacancy import Vacancy


def test_vacancy_equality():
    vacancy1 = Vacancy('Software Developer', 1000, 'Description 1', 'https://example.com/job1', 'USD')
    vacancy2 = Vacancy('Frontend Developer', 1500, 'Description 2', 'https://example.com/job2', 'USD')
    vacancy3 = Vacancy('Backend Developer', 1000, 'Description 3', 'https://example.com/job3', 'USD')

    assert vacancy1 == vacancy3  # Проверяем, что объекты vacancy1 и vacancy3 равны по зарплате

def test_vacancy_comparison():
    vacancy1 = Vacancy('Software Developer', 1000, 'Description 1', 'https://example.com/job1', 'USD')
    vacancy2 = Vacancy('Frontend Developer', 1500, 'Description 2', 'https://example.com/job2', 'USD')

    assert vacancy2 > vacancy1  # Проверяем, что объект vacancy2 имеет большую зарплату, чем у объекта vacancy1
    assert vacancy1 < vacancy2  # Проверяем, что объект vacancy1 имеет меньшую зарплату, чем у объекта vacancy2
