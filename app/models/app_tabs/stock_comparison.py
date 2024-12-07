import asyncio
import logging

from PySide6.QtWidgets import QWidget

from app.event_handlers.focus_guru_scrape_handlers import scrape_focus_guru_data
from app.utils import parse_scraped_data, MessageDialog, LabelStyler, prepare_values, prepare_objects

logger = logging.getLogger(__name__)



class StockComparison(QWidget):
    def __init__(self, widget):
        super().__init__()
        self.comparison_tab = widget
        self.label_styler = LabelStyler()
        self.message = MessageDialog()

        self.comparison_tab.stock_search_a_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_a_bar, 'stock_a'))

        self.comparison_tab.stock_search_b_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_b_bar, 'stock_b'))

        self.comparison_tab.stock_search_c_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_c_bar, 'stock_c'))

        self.comparison_tab.stock_search_d_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_d_bar, 'stock_d'))

    def trigger_method(self, symbol, stock_frame):
        data = self.collect_data(symbol.text())
        self.display_data(data, stock_frame)


    def collect_data(self, symbol):
        data = scrape_focus_guru_data(symbol)
        if data:
            return parse_scraped_data(data)
        else:
            self.message.show_message(title='Error',
                                      message=f'No data found found{symbol}')

    def display_data(self, data, stock_frame):

        dynamic_objects = prepare_objects(self.comparison_tab,stock_frame)
        values = prepare_values(data)

        for o, v in zip(dynamic_objects, values):
            try:
                self.label_styler.apply_style_filtering(o, v[0], v[1])
            except Exception as e:
                logger.exception(e)



