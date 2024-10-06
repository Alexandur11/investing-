from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel
from app.event_handlers import close_browser, clean_cookies, open_focus_guru, open_alpha_spread


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

        # Adding metrics with better formatting
        debt_management_label = QLabel("➢ Debt Management", alignment=Qt.AlignLeft)
        debt_management_label.setStyleSheet("color: rgb(34, 139, 34);")
        layout.addWidget(debt_management_label)

        layout.addWidget(QLabel("Cash To Debt Ratio – Optimal 0.20 or higher"))
        layout.addWidget(QLabel("D/E ratio – Optimal under 1, ideal under 0.5"))
        layout.addWidget(QLabel("Debt to EBITDA ratio – Optimal under 2.5"))
        layout.addWidget(QLabel("Interest Coverage ratio – Optimal over 5, ideal over 10"))
        layout.addWidget(QLabel("Current Ratio – Optimal over 1"))
        layout.addSpacing(10)

        efficiency_label = QLabel("➢ Efficiency", alignment=Qt.AlignLeft)
        efficiency_label.setStyleSheet("color: rgb(34, 139, 34);")
        layout.addWidget(efficiency_label)

        layout.addWidget(QLabel("ROE – Optimal over 12%"))
        layout.addWidget(QLabel("ROA – Optimal over 5-7%"))
        layout.addWidget(QLabel("ROIC – Optimal over 12%"))
        layout.addSpacing(10)

        price_estimates_label = QLabel("➢ Price Estimates", alignment=Qt.AlignLeft)
        price_estimates_label.setStyleSheet("color: rgb(34, 139, 34);")
        layout.addWidget(price_estimates_label)

        layout.addWidget(QLabel("• No revenue growth → P/E under 10/11"))
        layout.addWidget(QLabel("• 5% to 7% revenue growth → P/E under 15/17"))
        layout.addWidget(QLabel("• 10% to 12% revenue growth → P/E under 20/25"))
        layout.addSpacing(10)

        layout.addWidget(QLabel("PEG ratio – Optimal under 1 for growth stocks"))
        layout.addWidget(QLabel("P/S ratio – Optimal under 2.0 for growth"))
        layout.addWidget(QLabel("P/B ratio – Optimal under 3.0 for value"))
        layout.addWidget(QLabel("P/FCF ratio – Look for values under 25"))

        layout.addSpacing(10)

        avoid_companies_label = QLabel("➢ Avoid Companies Under the Following Circumstances", alignment=Qt.AlignLeft)
        avoid_companies_label.setStyleSheet("color: rgb(34, 139, 34);")
        layout.addWidget(avoid_companies_label)

        layout.addWidget(QLabel("• No P/E or no P/FCF"))
        layout.addWidget(QLabel("• P/E over 40 or P/FCF over 40"))
        layout.addWidget(QLabel("• No net capital"))
        layout.addWidget(QLabel("• ROIC under 7%"))
        layout.addSpacing(10)

        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Enter your stock here")
        layout.addWidget(self.text_input)

        self.button = QPushButton("Search", self)
        self.button.clicked.connect(self.trigger_method)
        layout.addWidget(self.button)

        self.feedback_label = QLabel("", self)
        layout.addWidget(self.feedback_label)

        central_widget.setLayout(layout)

    def trigger_method(self):
        entered_symbol = self.text_input.text().strip()

        if not entered_symbol:
            self.feedback_label.setText("Please enter a valid stock symbol.")
            return

        close_browser()
        clean_cookies()
        open_focus_guru(entered_symbol)
        open_alpha_spread(entered_symbol)

        self.text_input.clear()
        self.feedback_label.setText(f"Searching for {entered_symbol}...")
