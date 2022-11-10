from hh_ru_vacancies import predict_rub_salary_hh, get_all_language_vacancies_hh
from super_job_vacancies import predict_rub_salary_sj, get_all_language_vacancies_sj


def get_average_language_salaries(predict_salary, vacancies, amount_of_vacancies):
    total_salary = 0
    vacancies_processed = 0
    for vacancy in vacancies:
        salary = predict_salary(vacancy)
        if salary:
            total_salary += salary
            vacancies_processed += 1
    average_salary = None
    if vacancies_processed:
        average_salary = int(total_salary / vacancies_processed)
    salaries_details = {
        'vacancies_found': amount_of_vacancies,
        'vacancies_processed': vacancies_processed,
        'average_salary': average_salary
    }
    return salaries_details


def get_salary_info(get_all_language_vacancies, predict_rub_salary):
    languages = ['python', 'c', 'c#', 'c++', 'java', 'JavaScript', 'ruby', 'go', '1c']
    salary_info = {}
    for language in languages:
        vacancies, amount_of_vacancies = get_all_language_vacancies(language)
        salary_info[language] = get_average_language_salaries(predict_rub_salary, vacancies, amount_of_vacancies)
    return salary_info

def get_salary_statistics_sj():
    return get_salary_info(get_all_language_vacancies_sj, predict_rub_salary_sj)

def get_salary_statistics_hh():
    return get_salary_info(get_all_language_vacancies_hh, predict_rub_salary_hh)

