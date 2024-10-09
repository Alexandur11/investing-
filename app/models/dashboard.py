from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QLineEdit, QLabel

from app.models.config_check import ConfigCheck
from app.models.investing_buttons import InvestingButton
from app.models.user_interface import InvestingInterface


class Dashboard(QMainWindow):
    WINDOW_TITLE = "StockSearch"
    WINDOW_ICON_PATH = 'images/search_app.png'
    WINDOW_SIZE = (500, 300)


    def __init__(self):
        super().__init__()
        self.setup_window()
        self.text_input = QLineEdit(self)
        self.feedback_label = QLabel("", self)
        self.central_widget = QWidget()
        self.investing_ui = InvestingInterface()
        self.setup_layout()

        self.configs = ConfigCheck(self.investing_ui)
        self.configs.load_checkbox_config()


    def setup_window(self):
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowIcon(QIcon(self.WINDOW_ICON_PATH))
        self.resize(*self.WINDOW_SIZE)

    def setup_layout(self):
        layout = self.investing_ui.ui()

        self.text_input.setPlaceholderText("Enter your stock here")
        layout.addWidget(self.text_input)

        layout.addWidget(self.feedback_label)

        button = InvestingButton(self, self.text_input, self.feedback_label, self.investing_ui)
        layout.addWidget(button)

        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(layout)

    def closeEvent(self, event):
        self.configs.save_checkbox_config()
        super().closeEvent(event)