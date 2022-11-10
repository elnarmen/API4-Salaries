import os
from dotenv import load_dotenv
from terminaltables import AsciiTable
from hh_ru_vacancies import get_all_language_vacancies_hh, predict_rub_salary_hh
from super_job_vacancies import get_all_language_vacancies_sj
from salary_statistics_functions import get_all_languages_salary, predict_rub_salary


def get_table(title, salary_statistics):
    salary_table = [['Язык программирования',
                     'Вакансий найдено',
                     'Вакансий обработано',
                     'Средняя зарплата']]
    salary_table.extend(
        [[language_name,
          salary_details['vacancies_found'],
          salary_details['vacancies_processed'],
          salary_details['average_salary']]
         for language_name, salary_details in salary_statistics.items()])
    table_instance = AsciiTable(salary_table, title)
    return table_instance.table


def main():
    load_dotenv()
    title_hh = 'HaedHunter Moscow'
    title_sj = 'SuperJob Moscow'
    superjob_api_key = os.getenv('SUPERJOB_API_KEY')
    salary_statistics_hh = get_all_languages_salary(
        get_all_language_vacancies_hh,
        predict_rub_salary_hh,
        'RUR', 'from', 'to'
    )
    salary_statistics_sj = get_all_languages_salary(
        get_all_language_vacancies_sj,
        predict_rub_salary,
        'rub', 'payment_from', 'payment_to',
        superjob_api_key=superjob_api_key
    )
    print(get_table(title_hh, salary_statistics_hh))
    print()
    print(get_table(title_sj, salary_statistics_sj))


if __name__ == '__main__':
    load_dotenv()
    main()
