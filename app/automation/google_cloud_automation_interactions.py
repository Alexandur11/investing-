import logging
import time

from dotenv import dotenv_values
import gspread
from google.oauth2.service_account import Credentials

env_vars = dotenv_values()
spreadsheet_id = env_vars.get('SPREADSHEETID')
creds_file = 'creds.json'

logger = logging.getLogger(__name__)

"""
Module: google_sheet_cloud_operations

This module provides utilities for interacting with Google Sheets, including authentication, 
data retrieval, updates, and sheet management. It facilitates operations like appending data, 
rearranging sheets, and creating new sheets, with logging and error handling.

Dependencies:
- logging
- time
- dotenv.dotenv_values
- gspread
- google.oauth2.service_account.Credentials

Functions:
- authorize_creds_for_google_sheet(): Authorize credentials for accessing Google Sheets.
- get_column_letter(column_index): Convert a column index to an Excel-style letter.
- create_new_sheet(sheet_name, num_columns): Create a new sheet with a specified number of columns.
- collect_unfiltered_symbols_from_google_sheet_cloud(column): Collect stock symbols from a specified column.
- update_filtered_google_sheet_list_with_new_symbols(data_to_append, sheet_to_update): Append data to a sheet.
- update_filtered_stocks_list(data_to_append, sheet_to_update, col_to_update): Update a specific column in a sheet.
- rearrange_sheet(): Reorganize sheet data into a specified structure.
"""


def authorize_creds_for_google_sheet():
    """
       Authorize credentials for accessing Google Sheets using a service account.

       Returns:
           gspread.Client: An authorized gspread client for interacting with Google Sheets.

       Raises:
           Exception: Logs any errors encountered during authorization.
       """

    try:
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file(creds_file, scopes=SCOPES)
        return gspread.authorize(creds)
    except Exception as e:
        logger.exception(f'Error establishing connection: {e}')


def get_column_letter(column_index):
    """
        Convert a 1-based column index to an Excel-style column letter.

        Args:
            column_index (int): The 1-based index of the column.

        Returns:
            str: The corresponding Excel-style column letter.
    """

    """Convert a 1-based column index to an Excel-style column letter (A, B, C, ..., Z, AA, AB, ...)."""
    letter = ""
    while column_index > 0:
        column_index -= 1
        letter = chr(column_index % 26 + 65) + letter
        column_index //= 26
    return letter


def create_new_sheet(sheet_name, num_columns=100):
    """
        Create a new sheet in the Google Spreadsheet.

        Args:
            sheet_name (str): The name of the new sheet to create.
            num_columns (int, optional): The number of columns for the new sheet. Defaults to 100.

        Raises:
            Exception: Logs errors encountered during sheet creation.
        """

    gc = authorize_creds_for_google_sheet()

    sh = gc.open_by_key(spreadsheet_id)

    sh.add_worksheet(title=sheet_name, rows=200, cols=num_columns)


def collect_unfiltered_symbols_from_google_sheet_cloud(column: int):
    """
        Collect stock symbols from a specified column in a Google Sheet.

        Args:
            column (int): The column number to retrieve data from.

        Returns:
            list[str]: A list of stock symbols from the specified column.

        Raises:
            Exception: Logs errors encountered during data retrieval.
        """

    try:
        gc = authorize_creds_for_google_sheet()

        worksheet_name = 'US_Unfiltered_Stocks_Work'

        sh = gc.open_by_key(spreadsheet_id)
        worksheet = sh.worksheet(worksheet_name)
        column_data = worksheet.col_values(column)

        logger.info(f'Stocks from Column {column} collected')
        return column_data
    except Exception as e:
        logger.exception(f'Error collecting unfiltered symbols list from column {column}')
        logger.exception(f'Due to following error: {e}')


def update_filtered_google_sheet_list_with_new_symbols(data_to_append, sheet_to_update):
    """
       Append a list of new symbols to a specified sheet in the next available column.

       Args:
           data_to_append (list[str]): A list of symbols to append.
           sheet_to_update (str): The name of the sheet to update.

       Raises:
           Exception: Logs errors encountered during the update process.

       """

    try:
        gc = authorize_creds_for_google_sheet()
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
        logger.info(f'Sheet updated')
    except Exception as e:
        logger.exception(f'Error saving dataframe to Google Sheets: {e}')


def update_filtered_stocks_list(data_to_append, sheet_to_update, col_to_update):
    """
      Update a specific column in a sheet with new data.

      Args:
          data_to_append (list[str]): A list of symbols to append to the column.
          sheet_to_update (str): The name of the sheet to update.
          col_to_update (int): The column number to update.

      Raises:
          Exception: Logs errors encountered during the update process.

      """

    if data_to_append:
        try:
            row = get_column_letter(col_to_update)
            gc = authorize_creds_for_google_sheet()
            worksheet_name = sheet_to_update
            sh = gc.open_by_key(spreadsheet_id)
            worksheet = sh.worksheet(worksheet_name)

            existing_values = worksheet.col_values(col_to_update)
            size = len(existing_values)

            start_row = size + 1
            end_row = size + len(data_to_append)

            range_to_update = f"{row}{start_row}:{row}{end_row}"

            worksheet.update([[x] for x in data_to_append], range_to_update)
            logger.info(' Filtered Sheet updated')
        except Exception as e:
            logger.exception(f'Error updating filtered stocks sheet: {e}')


def rearrange_sheet():
    """
        Reorganize stock symbols into groups and append them to the specified sheet.

        Workflow:
            1. Collects stock symbols from multiple columns.
            2. Groups symbols into batches of 99.
            3. Appends each group as a new column to the sheet.

        Raises:
            Exception: Logs errors encountered during data collection or appending.
        """

    symbols = []
    for x in range(1, 26):
        time.sleep(10)

        symbols += collect_unfiltered_symbols_from_google_sheet_cloud(x)

    new_order = []
    inside_order = []
    for x in symbols:
        if len(inside_order) != 99:
            inside_order.append(x)
        else:
            inside_order.append(x)
            new_order.append(inside_order.copy())
            inside_order.clear()

    for data in new_order:
        time.sleep(20)
        update_filtered_google_sheet_list_with_new_symbols(data, 'US_Unfiltered_Stocks_Work')
