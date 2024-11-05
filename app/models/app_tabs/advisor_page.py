from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

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

class FinancialData:
    def __init__(self, financial_strength_data, growth_rank_data, liquidity_ratio_data,
                 profitability_rank_data, gf_value_rank_data):
        self.financial_strength = financial_strength_data
        self.growth_rank = growth_rank_data
        self.liquidity_ratio = liquidity_ratio_data
        self.profitability_rank = profitability_rank_data
        self.gf_value_rank = gf_value_rank_data


class LabelStyler:
    GREEN = "color: rgb(34, 139, 34);"
    RED = "color: rgb(255, 0, 0);"
    BLACK = "color: rgb(0, 0, 0);"

    @staticmethod
    def apply_color(label, condition):
        label.setStyleSheet(LabelStyler.GREEN if condition else LabelStyler.RED)


class AdvisorPageInterface(QWidget):
    def __init__(self, financial_data: FinancialData):
        super().__init__()
        self.financial_data = financial_data
        self.layout = QVBoxLayout()

    def build_ui(self):
        self.add_section("Debt Management", [
            ("Cash to Debt", self.financial_data.financial_strength['cash_to_debt'], lambda x: x >= 0.20),
            ("D/E Ratio", self.financial_data.financial_strength['debt_to_equity'], lambda x: x <= 1),
            ("Debt to EBITDA Ratio", self.financial_data.financial_strength['debt_to_ebitda'], lambda x: x <= 2.5),
            ("Interest Coverage Ratio", self.financial_data.financial_strength['interest_coverage_ratio'],
             lambda x: x >= 5),
            ("Current Ratio", self.financial_data.liquidity_ratio['current_ratio'], lambda x: x >= 1),
        ])

        self.layout.addSpacing(10)

        self.add_section("Efficiency", [
            ("ROA", self.financial_data.profitability_rank['roa'], lambda x: x >= 12),
            ("ROE", self.financial_data.profitability_rank['roe'], lambda x: x >= 5),
            ("ROIC", self.financial_data.profitability_rank['roic'], lambda x: x >= 12),
        ])

        self.layout.addSpacing(10)

        self.add_section("Price Estimates", [
            ("P/E Ratio", self.financial_data.gf_value_rank['P/E Ratio'], lambda x: x <= 23),
            ("PEG Ratio", self.financial_data.gf_value_rank['PEG Ratio'], lambda x: x <= 1),
            ("P/S Ratio", self.financial_data.gf_value_rank['PS Ratio'], lambda x: x <= 2),
            ("P/B Ratio", self.financial_data.gf_value_rank['PB Ratio'], lambda x: x <= 3),
            ("P/FCF Ratio", self.financial_data.gf_value_rank['P FCF'], lambda x: x <= 25),
        ])

        return self.layout

    def add_section(self, section_title, labels):

        section_label = QLabel(f"➢ {section_title}", alignment=Qt.AlignLeft)
        section_label.setStyleSheet(LabelStyler.BLACK)
        self.layout.addWidget(section_label)

        for label_text, value, condition in labels:
            try:
                label = QLabel(f"{label_text}: {value:.2f}", alignment=Qt.AlignLeft)
                LabelStyler.apply_color(label, condition(value))
                self.layout.addWidget(label)
            except (ValueError, TypeError):
                print(f'{label_text} is missing')
