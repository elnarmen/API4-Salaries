import requests


def predict_rub_salary_hh(vacancy: dict):
    if not vacancy['salary']:
        return None
    salary_details = vacancy['salary']
    if salary_details['currency'] != 'RUR':
        return None
    if salary_details['from'] and salary_details['to']:
        return (salary_details['from'] + salary_details['to']) / 2
    if salary_details['to']:
        return salary_details['to'] * .8
    elif salary_details['from']:
        return salary_details['from'] * 1.2
    return None

def get_all_language_vacancies_hh(language: str):
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


