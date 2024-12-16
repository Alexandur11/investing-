"""
This module is responsible for displaying the analyzed basic fundamental stock data inside the Stock Comparison Tab.


Dependencies:
- Pyside6
- logging
- threading

Logging:
Logs informational messages for successful operations and exceptions for failed attempts.
"""

import logging
from PySide6.QtCore import Signal, QThreadPool, QRunnable
from PySide6.QtWidgets import QWidget
from app.event_handlers.focus_guru_scrape_handlers import scrape_focus_guru_data
from app.utils import parse_scraped_data, MessageDialog, LabelStyler, prepare_values, prepare_objects

logger = logging.getLogger(__name__)


class StockComparison(QWidget):
    def __init__(self, widget):
        super().__init__()
        self.comparison_tab = widget
        self.message = MessageDialog()
        self.label_styler = LabelStyler()

        self.setup_ui()

    def setup_ui(self):

        """This method connects all buttons inside the Comparison Tab."""

        self.comparison_tab.stock_search_a_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_a_bar, 'stock_a'))

        self.comparison_tab.stock_search_b_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_b_bar, 'stock_b'))

        self.comparison_tab.stock_search_c_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_c_bar, 'stock_c'))

        self.comparison_tab.stock_search_d_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_d_bar, 'stock_d'))

    def trigger_method(self, symbol, stock_frame):

        """
          Initiates the process of displaying information about the selected stock at the desired frame.

          Parameters:
          -----------
          symbol : str
              The stock symbol to be processed.

          stock_frame : str
              A reference to which of the 4 optional frames was selected as a displaying location.

          Logging:
          --------
          - Logs an INFO message when the comparison process is triggered.
          - Logs an ERROR message with stack trace if an exception occurs.

          UI Interaction:
          ---------------
          - Displays a user-friendly error message in a MessageDialog if an error occurs.
          """

        try:
            logger.info(f"Triggering comparison for symbol: {symbol}")

            runnable = ComparisonWorkerRunnable(
                symbol=symbol,
                stock_frame=stock_frame,
                comparison_widget=self.comparison_tab,
                message=self.message,
                label_styler=self.label_styler
            )

            QThreadPool.globalInstance().start(runnable)

        except Exception as e:
            logger.exception("Exception in trigger_method:", exc_info=e)
            self.message.show_message(title='Error', message='An error occurred while processing the request.')


class ComparisonWorker(QWidget):
    """ Handles the collection and display of data for a given stock symbol using a GUI widget. """

    progress = Signal(int)
    error = Signal(str)
    finished = Signal()
    show_message = Signal(str, str)

    def __init__(self, symbol, stock_frame, comparison_widget, message, label_styler):
        super().__init__()
        self.symbol = symbol.text()
        self.stock_frame = stock_frame
        self.comparison_widget = comparison_widget
        self.message = message
        self.label_styler = label_styler
        self.data = None

    def collect_data(self):
        try:
            logger.info(f"Collecting data for symbol: {self.symbol}")
            data = scrape_focus_guru_data(self.symbol)

            if data:
                self.data = parse_scraped_data(data)
                self.finished.emit()
            else:
                self.message.show_message(title='Error',
                                          message=f'No data found for {self.symbol}')
                logger.warning(f"No data found for {self.symbol}")

        except Exception as e:
            logger.exception(f"Error while collecting data for symbol: {self.symbol}", exc_info=e)
            self.error.emit(f"Error collecting data: {str(e)}")

    def display_data(self):
        try:
            logger.info(f"Displaying data for symbol: {self.symbol}")
            dynamic_objects = prepare_objects(self.comparison_widget, self.stock_frame)
            values = prepare_values(self.data)

            for o, v in zip(dynamic_objects, values):
                try:
                    self.label_styler.apply_style_filtering(o, v[0], v[1])
                except Exception as e:
                    logger.exception(f"Error applying style for object: {o}", exc_info=e)

            self.finished.emit()

        except Exception as e:
            logger.exception(f"Error while displaying data for symbol: {self.symbol}", exc_info=e)
            self.error.emit(f"Error displaying data: {str(e)}")


class ComparisonWorkerRunnable(QRunnable):
    """
        A runnable wrapper for ComparisonWorker, enabling asynchronous execution.

        Attributes:
        -----------
        worker : ComparisonWorker
            An instance of the ComparisonWorker to perform operations.
    """

    def __init__(self, symbol, stock_frame, comparison_widget, message, label_styler):
        super().__init__()
        self.worker = ComparisonWorker(symbol, stock_frame, comparison_widget, message, label_styler)

    def run(self):
        self.worker.collect_data()
        if self.worker.data is not None:
            self.worker.display_data()
