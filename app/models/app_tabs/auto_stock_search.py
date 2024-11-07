from datetime import datetime

from PySide6.QtCore import QThread, Signal, QObject
import random
import time

from app.automation.focus_guru_automation_interactions import analyse_focus_guru_scraped_data
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
    show_message = Signal(str, str)

    def __init__(self, column):
        super().__init__()
        self.column = column

    def run(self):
        filtered_data = []
        try:
            unfiltered_symbols = collect_unfiltered_symbols_from_google_sheet_cloud(self.column)
            for index, symbol in enumerate(unfiltered_symbols):
                time.sleep(random.uniform(63, 183))
                if analyse_focus_guru_scraped_data(symbol):
                    filtered_data.append(symbol)
                    print(f'New stock discovered as potential investment {symbol}')

                self.progress.emit(index)
                print(f'{index}/{len(unfiltered_symbols)} analysed')

            if filtered_data:
                sheet_to_update = 'Filtered_stocks'
                update_filtered_google_sheet_list_with_new_symbols(filtered_data, sheet_to_update)
                self.show_message.emit('Search Completed', 'Something was found!')
            else:
                self.show_message.emit('Search Completed', 'Nothing Found :(')

            save_spreadsheet_activity_history(data={"Symbols Found": len(filtered_data),
                                                    "Time Finished": f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                                                    "Latest Column Searched": self.column})

            self.finished.emit()

        except Exception as e:
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

        self.worker = None
        self.worker_thread = None
        self.task_running = False

    def trigger_method(self):
        column = int(self.options_bar.currentText())
        self.progress_bar.setVisible(True)
        self.button.setEnabled(False)
        self.options_bar.setEnabled(False)

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

        # Connect the message signal
        self.worker.show_message.connect(self.show_message_dialog)

        # Start the worker thread
        self.worker_thread.started.connect(self.worker.run)
        self.worker_thread.start()

    def show_message_dialog(self, title, message):
        self.message = MessageDialog()
        self.message.show_message(title=title, message=message)

    def task_finished(self):
        self.task_running = False
        self.progress_bar.setVisible(True)
        self.button.setEnabled(True)
        self.options_bar.setEnabled(True)

    def handle_error(self, error_message):
        print(f"An error occurred: {error_message}")
        self.task_running = False

