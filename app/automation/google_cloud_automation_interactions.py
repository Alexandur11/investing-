import time

from dotenv import dotenv_values
import gspread
from google.oauth2.service_account import Credentials

env_vars = dotenv_values()


def authorize_creds_for_google_sheet():
    try:
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file('stocks-439709-358f6c1e35af.json', scopes=SCOPES)
        return gspread.authorize(creds)
    except Exception as e:
        print(f'Error establishing connection: {e}')


def get_column_letter(column_index):
    """Convert a 1-based column index to an Excel-style column letter (A, B, C, ..., Z, AA, AB, ...)."""
    letter = ""
    while column_index > 0:
        column_index -= 1
        letter = chr(column_index % 26 + 65) + letter
        column_index //= 26
    return letter


def create_new_sheet(sheet_name, num_columns=100):
    gc = authorize_creds_for_google_sheet()

    spreadsheet_id = '1Hien8Dr0zsu3aorg2-UhuI0w1rmjIdcb5QAqExnyG3Y'
    sh = gc.open_by_key(spreadsheet_id)

    sh.add_worksheet(title=sheet_name, rows=200, cols=num_columns)
    print(f"New sheet '{sheet_name}' created with {num_columns} columns.")


def collect_unfiltered_symbols_from_google_sheet_cloud(column: int):
    try:
        gc = authorize_creds_for_google_sheet()
        spreadsheet_id = '1Hien8Dr0zsu3aorg2-UhuI0w1rmjIdcb5QAqExnyG3Y'
        worksheet_name = 'US_Unfiltered_Stocks_Work'

        sh = gc.open_by_key(spreadsheet_id)
        worksheet = sh.worksheet(worksheet_name)
        column_data = worksheet.col_values(column)

        print(f'Stocks from Column {column} collected')
        return column_data
    except Exception as e:
        print(f'Error collecting unfiltered symbols list from column {column}')
        print(f'Due to following error: {e}')


def update_filtered_google_sheet_list_with_new_symbols(data_to_append, sheet_to_update):
    try:
        gc = authorize_creds_for_google_sheet()
        spreadsheet_id = '1Hien8Dr0zsu3aorg2-UhuI0w1rmjIdcb5QAqExnyG3Y'
        worksheet_name = sheet_to_update

        sh = gc.open_by_key(spreadsheet_id)
        worksheet = sh.worksheet(worksheet_name)

        all_values = worksheet.get_all_values()
        last_column = len(all_values[0])

        column_letter = get_column_letter(last_column + 1)
        start_row = 1
        end_row = start_row + len(data_to_append) - 1
        range_to_update = f"{column_letter}{start_row}:{column_letter}{end_row}"

        cell_list = worksheet.range(range_to_update)

        for i, cell in enumerate(cell_list):
            cell.value = data_to_append[i]

        worksheet.update_cells(cell_list)

        print(f'Sheet updated')
    except Exception as e:
        print(f'Error saving dataframe to Google Sheets: {e}')


def update_filtered_stocks_list(data_to_append, sheet_to_update, col_to_update):
    if data_to_append:
        try:
            row = get_column_letter(col_to_update)
            gc = authorize_creds_for_google_sheet()
            spreadsheet_id = '1Hien8Dr0zsu3aorg2-UhuI0w1rmjIdcb5QAqExnyG3Y'
            worksheet_name = sheet_to_update
            sh = gc.open_by_key(spreadsheet_id)
            worksheet = sh.worksheet(worksheet_name)

            existing_values = worksheet.col_values(col_to_update)
            size = len(existing_values)

            start_row = size + 1  # First empty row
            end_row = size + len(data_to_append)  # Last row to update

            range_to_update = f"{row}{start_row}:{row}{end_row}"

            worksheet.update([[x] for x in data_to_append], range_to_update)
        except Exception as e:
            print(e)
            print('Error updating filtered stocks sheet')


def rearrange_sheet():
    symbols = []
    for x in range(1, 26):
        time.sleep(10)
        print('New batch received')
        symbols += collect_unfiltered_symbols_from_google_sheet_cloud(x)
        print('batch appended')

    new_order = []
    inside_order = []
    for x in symbols:
        if len(inside_order) != 99:
            inside_order.append(x)
        else:
            inside_order.append(x)
            new_order.append(inside_order.copy())
            inside_order.clear()
            print('Inside order appended to new order and cleared')

    for data in new_order:
        time.sleep(20)
        update_filtered_google_sheet_list_with_new_symbols(data, 'US_Unfiltered_Stocks_Work')

    print('Process completed')
