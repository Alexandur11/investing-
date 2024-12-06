from PySide6.QtWidgets import QWidget

from app.event_handlers.focus_guru_scrape_handlers import scrape_focus_guru_data
from app.utils import parse_scraped_data


class LabelStyler:
    GREEN = "color: rgb(34, 139, 34);"
    RED = "color: rgb(255, 0, 0);"
    BLACK = "color: rgb(0, 0, 0);"

    @staticmethod
    def apply_color(label, condition):
        label.setStyleSheet(LabelStyler.GREEN if condition else LabelStyler.RED)



class StockComparison(QWidget):
    def __init__(self, widget):
        super().__init__()
        self.comparison_tab = widget



        self.comparison_tab.stock_search_a_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_a_bar,'stock_a'))



        self.comparison_tab.stock_search_b_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_b_bar,'stock_b'))


        self.comparison_tab.stock_search_c_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_c_bar, 'stock_c'))


        self.comparison_tab.stock_search_d_button.clicked.connect(
            lambda: self.trigger_method(self.comparison_tab.stock_search_d_button,'stock_d'))





    def trigger_method(self,symbol,stock_frame):
        data = self.collect_data(symbol.text())
        self.display_data(data,stock_frame)


    def collect_data(self,symbol):
        data = scrape_focus_guru_data(symbol)
        if data:
            return parse_scraped_data(data)

    def display_data(self,data,stock_frame):


        dynamic_name = f"{stock_frame}_pe"
        dynamic_object = getattr(self.comparison_tab, dynamic_name, None)
        dynamic_object.setVisible(True)


