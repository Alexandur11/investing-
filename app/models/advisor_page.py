from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget

from app.models.user_interfaces.advisor_page_user_interface import AdvisorPageInterface


class AdvisorPage(QMainWindow):
    WINDOW_TITLE = "Advisor Page"
    WINDOW_ICON_PATH = 'images/search_app.png'
    WINDOW_SIZE = (500, 300)

    def __init__(self, financial_data):
        super().__init__()
        self.financial_data = financial_data
        self.central_widget = QWidget()
        self.advisor_ui = AdvisorPageInterface(self.financial_data)
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowIcon(QIcon(self.WINDOW_ICON_PATH))
        self.resize(*self.WINDOW_SIZE)

    def setup_layout(self):
        layout = self.advisor_ui.build_ui()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)
        self.show()
