from dotenv import dotenv_values
import gspread
from google.oauth2.service_account import Credentials


env_vars = dotenv_values()



def update_unfiltered_stock_symbols_list(df):
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


def collect_unfiltered_symbols_from_google_sheet_cloud(column:int):
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

    column_data = worksheet.col_values(column)

    return column_data

def update_filtered_google_sheet_list_with_new_symbols(data_to_append):
    try:
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file('stocks-439709-358f6c1e35af.json', scopes=SCOPES)

        # Authorize the gspread client
        gc = gspread.authorize(creds)

        # Use the spreadsheet ID to open the spreadsheet
        spreadsheet_id = '1Hien8Dr0zsu3aorg2-UhuI0w1rmjIdcb5QAqExnyG3Y'
        worksheet_name = 'Filtered_stocks'

        # Open the spreadsheet using its ID
        sh = gc.open_by_key(spreadsheet_id)
        worksheet = sh.worksheet(worksheet_name)

        all_values = worksheet.get_all_values()
        last_column = len(all_values[0])


        print(f' Data Size {len(data_to_append)}')

        range_to_update = f"{chr(65 + last_column)}1:{chr(65 + last_column)}{len(data_to_append)}"

        cell_list = worksheet.range(range_to_update)

        for i, cell in enumerate(cell_list):
            cell.value = data_to_append[i]

        worksheet.update_cells(cell_list)

        print(f'Sheet updated')
    except Exception as e:
        print(f'Error saving dataframe to Google Sheets: {e}')