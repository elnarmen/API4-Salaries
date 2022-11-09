from terminaltables import AsciiTable, DoubleTable, SingleTable
from salary_stastics import get_salary_statistics_hh, get_salary_statistics_sj


def get_table(title, salary_statistics):
    table_data_hh = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]
    table_data_hh.extend(
        [[k, v['vacancies_found'], v['vacancies_processed'], v['average_salary']] for k, v in salary_statistics().items()])
    table_instance = AsciiTable(table_data_hh, title)
    return table_instance.table


def main():
    title_hh = 'HaedHunter Moscow'
    title_sj = 'SuperJob Moscow'
    print(get_table(title_sj, get_salary_statistics_sj))
    print()
    print(get_table(title_hh, get_salary_statistics_hh))


if __name__ == '__main__':
    main()