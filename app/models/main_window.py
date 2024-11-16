from app.utils import MessageDialog
from stockapp import *
from PySide6.QtWidgets import QMainWindow

from app.models.app_tabs.auto_stock_search import AutoStockSearch
from app.models.app_tabs.manual_stock_search import ManualStockSearch
from app.models.app_tabs.config_check import ConfigCheck


class MainWindow(QMainWindow):
    WINDOW_TITLE = "StockApp"
    WINDOW_ICON_PATH = 'images/search_app.png'
    WINDOW_SIZE = (800, 600)

    def __init__(self):
        super().__init__()

        self.ui = Ui_stock_app()
        self.ui.setupUi(self)
        self.setup_window()
        self.configs = ConfigCheck(self.ui)
        self.configs.load_checkbox_config()
        self.manual_stock_search_tab = ManualStockSearch(self.ui, self.configs)
        self.auto_stock_search_tab = AutoStockSearch(self.ui)

    def closeEvent(self, event):
        if self.auto_stock_search_tab.task_running:
            if MessageDialog().question_message(title='Warning',
                                             message='A task is still running. Are you sure you want to exit?',
                                             event=event):
                super().closeEvent(event)
        else:
            event.accept()
            super().closeEvent(event)

        self.configs.save_checkbox_config()


    def setup_window(self):
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowIcon(QIcon(self.WINDOW_ICON_PATH))
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-image: url(images/app_back.png);")
