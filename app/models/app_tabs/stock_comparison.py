import logging

from PySide6.QtCore import QThread, QObject, Signal
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

        self.threads = []

        self.comparison_tab.stock_search_a_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_a_bar, 'stock_a'))

        self.comparison_tab.stock_search_b_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_b_bar, 'stock_b'))

        self.comparison_tab.stock_search_c_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_c_bar, 'stock_c'))

        self.comparison_tab.stock_search_d_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_d_bar, 'stock_d'))

    def trigger_method(self, symbol, stock_frame):

        worker = ComparisonWorker(
            symbol=symbol,
            stock_frame=stock_frame,
            comparison_widget=self.comparison_tab,
            message=self.message,
            label_styler=self.label_styler
        )
        worker_thread = QThread()


        worker.moveToThread(worker_thread)


        worker_thread.started.connect(worker.collect_data)
        worker.finished.connect(worker.display_data)
        worker.finished.connect(worker.deleteLater)
        worker_thread.finished.connect(worker_thread.deleteLater)

        worker_thread.start()

        self.threads.append(worker_thread)


class ComparisonWorker(QObject):
    progress = Signal(int)
    error = Signal(str)
    finished = Signal()
    show_message = Signal(str, str)

    def __init__(self, symbol, stock_frame, comparison_widget, message, label_styler):
        super().__init__()

        self.message = message
        self.comparison_widget = comparison_widget
        self.label_styler = label_styler

        self.symbol = symbol.text()
        self.stock_frame = stock_frame

        self.data = None

    def collect_data(self):
        print('Collect')

        data = scrape_focus_guru_data(self.symbol)
        print(data)
        if data:
            self.data = parse_scraped_data(data)
            self.finished.emit()
        else:
            self.message.show_message(title='Error',
                                      message=f'No data found found{self.symbol}')

    def display_data(self):

        print('Display')

        dynamic_objects = prepare_objects(self.comparison_widget, self.stock_frame)
        values = prepare_values(self.data)

        for o, v in zip(dynamic_objects, values):
            try:
                self.label_styler.apply_style_filtering(o, v[0], v[1])
            except Exception as e:
                logger.exception(e)
