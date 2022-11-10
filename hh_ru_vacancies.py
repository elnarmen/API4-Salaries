import requests
from salary_statistics_functions import predict_rub_salary


def predict_rub_salary_hh(vacancy, currency, salary_from, salary_to):
    if not vacancy['salary']:
        return None
    salary_details = vacancy['salary']
    return predict_rub_salary(
        salary_details, currency,
        salary_from, salary_to
    )


def get_all_language_vacancies_hh(language, superjob_api_key=None):
    url = 'https://api.hh.ru/vacancies'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    page = 0
    pages_number = 1
    moscow_area = 1
    month_period = 30
    all_vacancies = []
    vacancies_found = 0
    while page < pages_number:
        params = {
            'text': f'name:Программист {language}',
            'area': moscow_area,
            'period': month_period,
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
