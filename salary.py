from dotenv import load_dotenv
from terminaltables import AsciiTable
from hh_ru_vacancies import get_salary_statistics_hh
from super_job_vacancies import get_salary_statistics_sj


def get_table(title, get_salary_statistics):
    salary_table = [['Язык программирования',
                     'Вакансий найдено',
                     'Вакансий обработано',
                     'Средняя зарплата']]
    salary_table.extend(
        [[language_name,
          salary_statistics['vacancies_found'],
          salary_statistics['vacancies_processed'],
          salary_statistics['average_salary']]
         for language_name, salary_statistics in get_salary_statistics().items()])
    table_instance = AsciiTable(salary_table, title)
    return table_instance.table


def main():
    load_dotenv()
    title_hh = 'HaedHunter Moscow'
    title_sj = 'SuperJob Moscow'
    print(get_table(title_hh, get_salary_statistics_hh))
    print()
    print(get_table(title_sj, get_salary_statistics_sj))


if __name__ == '__main__':
    load_dotenv()
    main()
