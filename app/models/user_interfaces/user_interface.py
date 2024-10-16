from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QCheckBox


class InvestingInterface(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.analytics_panel = QCheckBox("Analytics Panel")
        self.alpha_spread = QCheckBox("Alpha Spread")
        self.focus_guru = QCheckBox("Focus Guru")
        self.macro_trends = QCheckBox("Macro Trends")
        self.finance_charts = QCheckBox("Finance Charts")
        self.companies_market_cap = QCheckBox("Companies Market Cap")



    def ui(self):
        # Adding metrics with better formatting
        debt_management_label = QLabel("➢ Debt Management", alignment=Qt.AlignLeft)
        debt_management_label.setStyleSheet("color: rgb(34, 139, 34);")
        self.layout.addWidget(debt_management_label)

        self.layout.addWidget(QLabel("Cash To Debt Ratio – Optimal 0.20 or higher"))
        self.layout.addWidget(QLabel("D/E ratio – Optimal under 1, ideal under 0.5"))
        self.layout.addWidget(QLabel("Debt to EBITDA ratio – Optimal under 2.5"))
        self.layout.addWidget(QLabel("Interest Coverage ratio – Optimal over 5, ideal over 10"))
        self.layout.addWidget(QLabel("Current Ratio – Optimal over 1"))
        self.layout.addSpacing(10)

        efficiency_label = QLabel("➢ Efficiency", alignment=Qt.AlignLeft)
        efficiency_label.setStyleSheet("color: rgb(34, 139, 34);")
        self.layout.addWidget(efficiency_label)

        self.layout.addWidget(QLabel("ROE – Optimal over 12%"))
        self.layout.addWidget(QLabel("ROA – Optimal over 5-7%"))
        self.layout.addWidget(QLabel("ROIC – Optimal over 12%"))
        self.layout.addSpacing(10)

        price_estimates_label = QLabel("➢ Price Estimates", alignment=Qt.AlignLeft)
        price_estimates_label.setStyleSheet("color: rgb(34, 139, 34);")
        self.layout.addWidget(price_estimates_label)

        self.layout.addWidget(QLabel("• No revenue growth → P/E under 10/11"))
        self.layout.addWidget(QLabel("• 5% to 7% revenue growth → P/E under 15/17"))
        self.layout.addWidget(QLabel("• 10% to 12% revenue growth → P/E under 20/25"))
        self.layout.addSpacing(10)

        self.layout.addWidget(QLabel("PEG ratio – Optimal under 1 for growth stocks"))
        self.layout.addWidget(QLabel("P/S ratio – Optimal under 2.0 for growth"))
        self.layout.addWidget(QLabel("P/B ratio – Optimal under 3.0 for value"))
        self.layout.addWidget(QLabel("P/FCF ratio – Look for values under 25"))

        self.layout.addSpacing(10)

        avoid_companies_label = QLabel("➢ Avoid Companies Under the Following Circumstances", alignment=Qt.AlignLeft)
        avoid_companies_label.setStyleSheet("color: rgb(34, 139, 34);")
        self.layout.addWidget(avoid_companies_label)

        self.layout.addWidget(QLabel("• No P/E or no P/FCF"))
        self.layout.addWidget(QLabel("• P/E over 40 or P/FCF over 40"))
        self.layout.addWidget(QLabel("• No net capital"))
        self.layout.addWidget(QLabel("• ROIC under 7%"))
        self.layout.addSpacing(10)

        self.status_label = QLabel("Select options")

        self.layout.addWidget(self.analytics_panel)
        self.layout.addWidget(self.alpha_spread)
        self.layout.addWidget(self.focus_guru)
        self.layout.addWidget(self.macro_trends)
        self.layout.addWidget(self.finance_charts)
        self.layout.addWidget(self.companies_market_cap)
        self.layout.addWidget(self.status_label)

        return self.layout

