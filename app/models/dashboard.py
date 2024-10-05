from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from app.event_handlers import close_browser,clean_cookies,open_focus_guru,open_alpha_spread

class Dashboard(QMainWindow):
    WINDOW_TITLE = "StockSearch"
    WINDOW_ICON_PATH = 'images/search_app.png'
    WINDOW_SIZE = (500, 300)

    def __init__(self):
        super().__init__()
        self.setup_window()
        self.setup_layout()

    def setup_window(self):
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowIcon(QIcon(self.WINDOW_ICON_PATH))
        self.resize(*self.WINDOW_SIZE)

    def setup_layout(self):

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()


        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Enter your stock here")
        layout.addWidget(self.text_input)


        self.button = QPushButton("Serach", self)
        self.button.clicked.connect(self.trigger_method)
        layout.addWidget(self.button)

        central_widget.setLayout(layout)

    def trigger_method(self):
        entered_symbol = self.text_input.text()
        close_browser()
        clean_cookies()
        open_focus_guru(entered_symbol)
        open_alpha_spread(entered_symbol)



