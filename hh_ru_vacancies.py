import requests
import functools
import collections
import operator


def predict_rub_salary(vacancy: dict):
    if vacancy['salary'] is None:
        return None
    salary_details = vacancy['salary']
    if salary_details['currency'] != 'RUR':
        return None
    if salary_details['from'] and salary_details['to']:
        return (salary_details['from'] + salary_details['to']) / 2
    elif salary_details['from'] is None:
        return salary_details['to'] * .8
    elif salary_details['to'] is None:
        return salary_details['from'] * 1.2


def get_all_language_vacancies(language: str):
    url = 'https://api.hh.ru/vacancies'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    page = 0
    pages_number = 1
    all_vacancies = []
    vacancies_found = 0
    while page < pages_number:
        params = {
            'text': f'name:Программист {language}',
            'area': 1,
            'period': 30,
            'page': page,
        }
        page_responce = requests.get(url, params, headers=user_agent)
        page_responce.raise_for_status()
        page_payload = page_responce.json()
        pages_number = page_payload['pages']
        page += 1
        page_vacancies = page_payload['items']
        vacancies_found = page_payload['found']
        all_vacancies.extend(page_vacancies)
    return all_vacancies, vacancies_found


def get_average_language_salaries(vacancies, ammount_of_vacancies):
    total_salary = 0
    vacancies_processed = 0
    for vacancy in vacancies:
        salary = predict_rub_salary(vacancy)
        if salary:
            total_salary += salary
            vacancies_processed += 1
    average_salary = None
    if vacancies_processed:
        average_salary = int(total_salary / vacancies_processed)
    salaries_details = {
        'vacancies_found': ammount_of_vacancies,
        'vacancies_processed': vacancies_processed,
        'average_salary': average_salary
    }
    return salaries_details


languages = ['Python', 'C', 'Java', 'C++', 'C#', 'Visual Basic', 'JavaScript', 'PHP', 'Swift', 'Go', 'Kotlin', 'Solidity']
salary_statistics = {}
for language in languages:
    vacancies, ammount_of_vacancies = get_all_language_vacancies(language)
    salary_statistics[language] = get_average_language_salaries(vacancies, ammount_of_vacancies)

for k, v in salary_statistics:
    print(f'''Язык программирования: {k}.
    Вакансий найдено: {v['vacancies_found']}
    Вакансий обработано: {v['vacancies_processed']}
    Средняя зарплата: {v['average_salary']}''')

d = {'Python': {'vacancies_found': 1126, 'vacancies_processed': 273, 'average_salary': 199573},
     'C': {'vacancies_found': 1545, 'vacancies_processed': 539, 'average_salary': 183932},
     'Java': {'vacancies_found': 1406, 'vacancies_processed': 199, 'average_salary': 231611},
     'C++': {'vacancies_found': 863, 'vacancies_processed': 246, 'average_salary': 176242},
     'C#': {'vacancies_found': 727, 'vacancies_processed': 175, 'average_salary': 184329},
     'Visual Basic': {'vacancies_found': 22, 'vacancies_processed': 6, 'average_salary': 164500},
     'JavaScript': {'vacancies_found': 1979, 'vacancies_processed': 602, 'average_salary': 181361},
     'PHP': {'vacancies_found': 894, 'vacancies_processed': 385, 'average_salary': 166756},
     'Swift': {'vacancies_found': 209, 'vacancies_processed': 53, 'average_salary': 242726},
     'Go': {'vacancies_found': 438, 'vacancies_processed': 110, 'average_salary': 232594}}
