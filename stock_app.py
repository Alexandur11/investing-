


# app = QApplication(sys.argv)
# app.setWindowIcon(QIcon("images/search_app.png"))
#
# main = Dashboard()
# main.show()
# app.exec()



from  stockapp import *
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

from app2.models2.auto_stock_search import AutoStockSearch
from app2.models2.manual_stock_search import ManualStockSearch
from app2.models2.config_check import ConfigCheck

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-image: url(images/app_back.png);")
        self.configs = ConfigCheck(self.ui)
        self.configs.load_checkbox_config()
        self.manual_stock_search_tab = ManualStockSearch(self.ui,self.configs)
        self.auto_stock_search_tab = AutoStockSearch(self.ui)

    def closeEvent(self, event):
        self.configs.save_checkbox_config()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
