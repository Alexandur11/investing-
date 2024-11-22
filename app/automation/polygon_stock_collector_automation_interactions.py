# import json
# import time
#
# import requests
# from dotenv import dotenv_values
# import pandas as pd
#
# env_vars = dotenv_values()
#
#
# def stock_collector_orchestrator(url):
#     response = fetch_stocks(url=url, limit=1000)
#     df = convert_response_to_dataframe(response)
#     # update_unfiltered_stock_symbols_list(df['df'])
#
#     if df['next_url']:
#         time.sleep(20)
#
#         stock_collector_orchestrator(df['next_url'])
#     # print(f' Stock collector process completed')
#
#
# def fetch_stocks(limit=1000, url=None):
#     try:
#         api_key = env_vars.get('POLYGONAPIKEY')
#         params = {'limit': limit}
#         headers = {'Authorization': f'Bearer {api_key}'}
#
#         # print('Data fetched')
#         return requests.get(url=url, params=params, headers=headers)
#
#     except Exception as e:
#         print(f'Error fetching stocks {e}')
#
#
# def convert_response_to_dataframe(response):
#     try:
#         print(f'Status code {response.status_code}')
#
#         decoded_data = response.content.decode("utf-8")
#         json_data = json.loads(decoded_data)
#         df = pd.DataFrame(json_data['results'])
#
#         df.dropna()
#         # print(f'Data converted {df}')
#
#         return {'df': df.loc[df['market'] == 'stocks', 'ticker'], 'next_url': json_data['next_url']}
#     except Exception as e:
#         print(f'Error converting response to dataframe {e}')
