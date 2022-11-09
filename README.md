# Статистика по средним зарплатам программистов
Программа запрашивает информацию о вакансиях с сайтов [hh.ru](https://hh.ru) и [SuperJob](https://www.superjob.ru),
загружает данные по зарплатам для самых популярных языков программирования и отображает полученные данные в виде консольной таблицы
## Загрузка проекта
На вашем компьютере уже должен быть установлен Python3.
Для загрузки проекта откройте терминал и перейдите в папку, в которую хотите загрузить файлы.

Затем введите команду:
```
git clone https://github.com/elnarmen/API3
```
## Настройка виртуального окружения
Перейдите в папку с проектом:
```
cd gjodjglvflgkrklkhsk
```
Далее введите команду:
```
python -m venv venv
```
Активируйте виртуальное окружение командой:
```
cd venv\Scripts
activate.bat
```
Затем вернитесь в папку с проектом:
```
cd ../..
```
## Установка зависимостей
Используйте pip для установки зависимостей:

   ```
   pip install -r requirements.txt
   ```
## Получение ключа
SuperJob не отдаст данные без авторизации. Вам понадобится ключ. Зарегистрируйтесь [здесь](https://api.superjob.ru/).
При регистрации приложения от вас потребуют указать сайт. Введите любой, они не проверяют.
Ключ выглядит примерно так: 
`v1.h002e16b85c34bcf7b2a478ac1a5c68fac32cb8ff57fcd579677d01e2eba075d4ae0c999a.20774ea98a8b18a1253b6e9bc289288078607a93`
Далее создайте в папке с проектом файл **`.env`** и сохраните в переменную SUPERJOB_API_KEY полученный ключ:
```
SUPERJOB_API_KEY = <ваш ключ>
```
## Запуск приложения
Для того, чтобы получить таблицу со средними зарплатами программистов введите команду:
```
python salaries.py
```
Пример работы программы:

(example)[]