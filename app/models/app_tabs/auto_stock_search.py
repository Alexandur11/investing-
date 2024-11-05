from datetime import datetime

from PySide6.QtCore import QThread, Signal, QObject
import random
import time

from app.automation.focus_guru_automation_interactions import automated_focus_guru_scrape_orchestrator
from app.automation.google_cloud_automation_interactions import (
    collect_unfiltered_symbols_from_google_sheet_cloud,
    update_filtered_google_sheet_list_with_new_symbols
)
from app.models.app_tabs.config_check import save_spreadsheet_activity_history, load_latest_spreadsheet_activity
from app.utils import MessageDialog


class StockSearchWorker(QObject):
    progress = Signal(int)
    error = Signal(str)
    finished = Signal()

    def __init__(self, column):
        super().__init__()
        self.column = column
        self.message = MessageDialog()

    def run(self):
        filtered_data = []
        try:
            unfiltered_symbols = collect_unfiltered_symbols_from_google_sheet_cloud(self.column)
            for index, symbol in enumerate(unfiltered_symbols[1:2]):
                time.sleep(random.uniform(63, 183))
                if automated_focus_guru_scrape_orchestrator(symbol):
                    filtered_data.append(symbol)
                    print(f'New stock discovered as potential investment {symbol}')

                self.progress.emit(index)
                print(f'{index}/{len(unfiltered_symbols)} analysed')

            if filtered_data:
                sheet_to_update = 'Filtered_stocks'
                update_filtered_google_sheet_list_with_new_symbols(filtered_data, sheet_to_update)
                self.message.show_message(title='Search Completed', message='Something was found!')
            else:
                self.message.show_message(title='Search Completed', message='Nothing Found :(')

            self.finished.emit()

            save_spreadsheet_activity_history(data={"Symbols Found":len(filtered_data),
                                                    "Time Finished":f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}",
                                                    "Latest Column Searched": self.column})

        except Exception as e:
            self.error.emit(str(e))


class AutoStockSearch:
    def __init__(self, widget):
        self.auto_stock_control = widget
        self.auto_stock_control.stock_search_automation_button.clicked.connect(self.trigger_method)
        self.options_bar = self.auto_stock_control.stock_search_auto_combo_box
        self.options_bar.addItems([str(x) for x in range(1, 60)])
        self.options_bar.setCurrentIndex(load_latest_spreadsheet_activity())
        self.progress_bar = self.auto_stock_control.stock_auto_search_progress_bar
        self.worker = None
        self.worker_thread = None
        self.task_running = False  # Flag to check if task is running

    def trigger_method(self):
        column = int(self.options_bar.currentText())

        # Set task as running
        self.task_running = True

        # Create and start the worker thread
        self.worker = StockSearchWorker(column)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)

        # Connect signals
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.error.connect(self.handle_error)
        self.worker.finished.connect(self.task_finished)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)

        # Start the worker thread
        self.worker_thread.started.connect(self.worker.run)
        self.worker_thread.start()

    def task_finished(self):
        self.task_running = False  # Set task as not running when finished

    def handle_error(self, error_message):
        print(f"An error occurred: {error_message}")
        self.task_running = False  # Set task as not running if an error occurs
