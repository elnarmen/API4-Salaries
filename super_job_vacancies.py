import os
import requests
from dotenv import load_dotenv


load_dotenv()
url = 'https://api.superjob.ru/2.0/vacancies'
superjob_api_key = os.getenv('SUPERJOB_API_KEY')
headers = {'X-Api-App-Id': superjob_api_key}
response = requests.get(url, headers=headers)
response.raise_for_status()
print('\n'.join([i['profession'] for i in response.json()['objects']]))