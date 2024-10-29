
import requests
from dotenv import dotenv_values

env_vars = dotenv_values()
#
# country = 'LSE'
api_key = env_vars.get('FINHUBAPIKEY')
# url = f'https://finnhub.io/api/v1/stock/symbol?exchange={country}&token={api_key}'
# response = requests.get(url=url)
#
#
# print(response.content)


import finnhub

# Initialize the Finnhub client with your API key
finnhub_client = finnhub.Client(api_key=api_key)  # Replace with your actual API key

print(finnhub_client.stock_symbols('LSE'))