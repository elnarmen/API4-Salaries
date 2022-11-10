import os
import requests


def get_all_language_vacancies_sj(language, superjob_api_key):
    url = 'https://api.superjob.ru/2.0/vacancies'
    page = 0
    pages_numper = 5  # если параметр count в запросе = 100, API выдаст только 5 страниц
    other_results = True
    all_vacancies = []
    vacancies_found = 0
    while page < pages_numper and other_results:
        params = {'town': 4,  # id Москвы
                  'catalogues': 48,  # id каталога "Разработка, программирование"
                  'count': 100,  # api запрещает запрашивать больше 100 вакансий
                  'page': page,
                  'keyword': language,
                  'period': 0,
                  }
        headers = {'X-Api-App-Id': superjob_api_key}
        page_response = requests.get(url, params, headers=headers)
        page_response.raise_for_status()
        decoder_response = page_response.json()
        all_vacancies.extend(decoder_response['objects'])
        vacancies_found = decoder_response['total']
        other_results = decoder_response['more']
        page += 1
    return all_vacancies, vacancies_found
