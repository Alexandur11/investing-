"""
Module for automating stock search processes and handling related background tasks.

This module leverages PySide6 to integrate a graphical user interface for stock search automation. It defines classes to manage stock search tasks, communicate progress, handle errors, and update data in Google Sheets. The main components include worker threads for long-running tasks, interactive UI elements for initiating stock searches, and methods to update progress and manage state.

Dependencies:
- PySide6
- logging
- random
- time

Logging:
Logs informational messages for successful operations and exceptions for failed attempts.

"""

import logging
from datetime import datetime

from PySide6.QtCore import QThread, Signal, QObject
import random
import time

from app.automation.focus_guru_automation_interactions import analyse_focus_guru_scraped_data
from app.automation.google_cloud_automation_interactions import (
    collect_unfiltered_symbols_from_google_sheet_cloud, update_filtered_stocks_list
)
from app.models.app_tabs.config_check import save_spreadsheet_activity_history, load_latest_spreadsheet_activity
from app.utils import MessageDialog, decide_the_stock_column

logger = logging.getLogger(__name__)

class StockSearchWorker(QObject):
    progress = Signal(int)
    error = Signal(str)
    finished = Signal()
    show_message = Signal(str, str)

    def __init__(self, column: int):
        super().__init__()
        self.column = column

    def update_stock_list(self, stock_data_list):
        """
        Updates the filtered stocks list in Google Sheets with the categorized stock data.

        Args:
            stock_data_list (list): A list of stock data categorized into tiers.

        Logs:
            - Exception details if the update fails.
        """
        try:
            for index, data in enumerate(stock_data_list):
                time.sleep(3)
                update_filtered_stocks_list(data_to_append=data, sheet_to_update='Filtered_stocks',
                                            col_to_update=index + 1)
        except Exception as e:
            logger.exception(e)

    def run(self):
        """
        Runs the stock search process. Fetches unfiltered stock symbols, analyzes data, and categorizes results.

        Logs:
            - Progress updates.
            - Informational messages for successful operations.
            - Exception details for failed operations.
        """
        A, B, C = [], [], []  # Stocks tier list related to the spreadsheet
        stocks_found = 0

        try:
            unfiltered_symbols = collect_unfiltered_symbols_from_google_sheet_cloud(self.column)

            for index, symbol in enumerate(unfiltered_symbols):
                try:
                    time.sleep(random.uniform(63, 183))
                    result = analyse_focus_guru_scraped_data(symbol)

                    if result > 7:
                        decide_the_stock_column(A, B, C, symbol, result)
                        stocks_found += 1

                    self.progress.emit(index)
                    logger.info(f'{index}/{len(unfiltered_symbols)} analysed')

                except Exception as e:
                    logger.exception(e)

            self.update_stock_list([A, B, C])

            self.show_message.emit('Search Completed', 'Nothing Found' if stocks_found == 0 else 'Something found!')

            save_spreadsheet_activity_history(data={"Symbols Found": stocks_found,
                                                    "Time Finished": f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                                                    "Latest Column Searched": self.column})

            self.finished.emit()

        except Exception as e:
            logger.exception(e)
            self.error.emit(str(e))


class AutoStockSearch:
    def __init__(self, widget):
        self.auto_stock_control = widget
        self.button = self.auto_stock_control.stock_search_automation_button
        self.button.clicked.connect(self.trigger_method)

        self.options_bar = self.auto_stock_control.stock_search_auto_combo_box
        self.options_bar.addItems([str(x) for x in range(1, 60)])
        self.options_bar.setCurrentIndex(load_latest_spreadsheet_activity())

        self.progress_bar = self.auto_stock_control.stock_auto_search_progress_bar
        self.progress_bar.setVisible(False)

        self.message = MessageDialog()

        self.worker = None
        self.worker_thread = None
        self.task_running = False

    def trigger_method(self):
        """
        Initiates the stock search automation process.

        Logs:
            - Progress updates.
            - Error handling and cleanup when the task finishes or fails.
        """
        column = int(self.options_bar.currentText())
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.button.setEnabled(False)
        self.options_bar.setEnabled(False)

        self.task_running = True

        self.worker = StockSearchWorker(column)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)

        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.error.connect(self.handle_error)
        self.worker.finished.connect(self.task_finished)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)

        self.worker.show_message.connect(self.show_message_dialog)

        self.worker_thread.started.connect(self.worker.run)
        self.worker_thread.start()

    def show_message_dialog(self, title, message):
        """
        Displays a message dialog with the given title and message.

        Args:
            title (str): The title of the message dialog.
            message (str): The message content to display.

        Logs:
            - Informational messages when displaying the message dialog.
        """
        self.message.show_message(title=title, message=message)

    def task_finished(self):
        """
        Handles the cleanup after the stock search task finishes.

        Logs:
            - Informational messages indicating task completion.
        """
        self.task_running = False
        self.progress_bar.setVisible(False)
        self.button.setEnabled(True)
        self.options_bar.setEnabled(True)

    def handle_error(self, error_message):
        """
        Logs and handles errors that occur during the stock search task.

        Args:
            error_message (str): The error message received from the worker.

        Logs:
            - Exception details if an error occurs.
        """
        logger.exception(f"An error occurred: {error_message}")
        self.task_running = False
