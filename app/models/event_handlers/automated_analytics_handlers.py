import json
import time

import requests
from dotenv import dotenv_values
import pandas as pd

import gspread
from google.oauth2.service_account import Credentials


env_vars = dotenv_values()



def stock_collector(url):
    response = fetch_stocks(url=url,limit=1000)
    df = convert_response_to_dataframe(response)
    save_dataframe_to_sheets(df['df'])

    if df['next_url']:
        print(df['next_url'])
        time.sleep(20)
        stock_collector(df['next_url'])
    print(f' Stock collector process completed')

def fetch_stocks(limit=1000,url=None):
    try:
        api_key = env_vars.get('POLYGONAPIKEY')
        params = {'limit': limit}
        headers = {'Authorization': f'Bearer {api_key}'}
        print('Data fetched')
        return requests.get(url=url, params=params, headers=headers)
    except Exception as e:
        print(f'Error fetching stocks {e}')

def convert_response_to_dataframe(response):
    try:
        print(f'Status code {response.status_code}')
        decoded_data = response.content.decode("utf-8")
        json_data = json.loads(decoded_data)
        df = pd.DataFrame(json_data['results'])
        df.dropna()
        print(f'Data converted {df}')
        return {'df':df.loc[df['market'] == 'stocks', 'ticker'],'next_url':json_data['next_url']}
    except Exception as e:
        print(f'Error converting response to dataframe {e}')

def save_dataframe_to_sheets(df):
    try:
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file('stocks-439709-358f6c1e35af.json', scopes=SCOPES)

        # Authorize the gspread client
        gc = gspread.authorize(creds)

        # Use the spreadsheet ID to open the spreadsheet
        spreadsheet_id = '1Hien8Dr0zsu3aorg2-UhuI0w1rmjIdcb5QAqExnyG3Y'
        worksheet_name = 'Unfiltered_stocks'

        # Open the spreadsheet using its ID
        sh = gc.open_by_key(spreadsheet_id)
        worksheet = sh.worksheet(worksheet_name)

        all_values = worksheet.get_all_values()
        last_column = len(all_values[0])


        data_to_append = df.tolist()
        print(f' Data Size {len(data_to_append)}')

        range_to_update = f"{chr(65 + last_column)}1:{chr(65 + last_column)}{len(data_to_append)}"

        cell_list = worksheet.range(range_to_update)

        for i, cell in enumerate(cell_list):
            cell.value = data_to_append[i]

        worksheet.update_cells(cell_list)

        print(f'Sheet updated')
    except Exception as e:
        print(f'Error saving dataframe to Google Sheets: {e}')


print(stock_collector(url='https://api.polygon.io/v3/reference/tickers'))