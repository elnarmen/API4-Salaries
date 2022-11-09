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


def get_salary_statistics(get_all_language_vacancies, predict_rub_salary):
    languages = ['Python', 'C', 'Java', 'C++', 'C#', 'JavaScript', 'PHP', 'Go', 'Kotlin']
    salary_statistics = {}
    for language in languages:
        vacancies, amount_of_vacancies = get_all_language_vacancies(language)
        salary_statistics[language] = get_average_language_salaries(predict_rub_salary, vacancies, amount_of_vacancies)
    return salary_statistics