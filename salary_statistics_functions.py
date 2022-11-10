def get_average_language_salaries(predict_salary, vacancies, amount_of_vacancies, currency, salary_from, salary_to):
    total_salary = 0
    vacancies_processed = 0
    for vacancy in vacancies:
        salary = predict_salary(vacancy, currency, salary_from, salary_to)
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


def get_all_languages_salary(get_all_language_vacancies, predict_rub_salary, currency, salary_from, salary_to):
    languages = ['python', 'c', 'c#', 'c++', 'java', 'JavaScript', 'ruby', 'go', '1c']
    all_languages_salary = {}
    for language in languages:
        vacancies, amount_of_vacancies = get_all_language_vacancies(language)
        all_languages_salary[language] = get_average_language_salaries(
            predict_rub_salary,
            vacancies,
            amount_of_vacancies,
            currency,
            salary_from,
            salary_to)
    return all_languages_salary


def predict_rub_salary(vacancy, currency, salary_from, salary_to):
        if vacancy['currency'] != currency:
            return None
        if vacancy[salary_from] and vacancy[salary_to]:
            return (vacancy[salary_from] + vacancy[salary_to]) / 2
        if vacancy[salary_to]:
            return vacancy[salary_to] * .8
        if vacancy[salary_from]:
            return vacancy[salary_from] * 1.2
        return None