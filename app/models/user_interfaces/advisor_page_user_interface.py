from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class AdvisorPageInterface(QWidget):
    def __init__(self, financial_strength_data, growth_rank_data, liquidity_ratio_data,
                 profitability_rank_data, gf_value_rank_data):
        self.financial_strength_data = financial_strength_data
        self.growth_rank_data = growth_rank_data
        self.liquidity_ratio_data = liquidity_ratio_data
        self.profitability_rank_data = profitability_rank_data
        self.gf_value_rank_data = gf_value_rank_data

        self.green = "color: rgb(34, 139, 34);"
        self.black = "color: rgb(0, 0, 0);"
        self.red = "color: rgb(255, 0, 0);"
        super().__init__()
        self.layout = QVBoxLayout()

    def set_label_color(self, label, condition):
        label.setStyleSheet(self.green if condition else self.red)

    def ui(self):
        debt_management_label = QLabel("➢ Debt Management", alignment=Qt.AlignLeft)
        debt_management_label.setStyleSheet(self.green)
        self.layout.addWidget(debt_management_label)

        cash_to_debt_label = QLabel(f"Cash to Debt: {self.financial_strength_data['cash_to_debt']:.2f}", alignment=Qt.AlignLeft)
        self.set_label_color(cash_to_debt_label, self.financial_strength_data['cash_to_debt'] >= 0.20)
        self.layout.addWidget(cash_to_debt_label)

        debt_to_equity_label = QLabel(f"D/E Ratio: {self.financial_strength_data['debt_to_equity']:.2f}", alignment=Qt.AlignLeft)
        self.set_label_color(debt_to_equity_label, self.financial_strength_data['debt_to_equity'] <= 1)
        self.layout.addWidget(debt_to_equity_label)

        debt_to_ebitda_label = QLabel(f"Debt to EBITDA Ratio: {self.financial_strength_data['debt_to_ebitda']:.2f}", alignment=Qt.AlignLeft)
        self.set_label_color(debt_to_ebitda_label, self.financial_strength_data['debt_to_ebitda'] <= 2.5)
        self.layout.addWidget(debt_to_ebitda_label)

        interest_coverage_label = QLabel(f"Interest Coverage Ratio: {self.financial_strength_data['interest_coverage_ratio']:.2f}", alignment=Qt.AlignLeft)
        self.set_label_color(interest_coverage_label, self.financial_strength_data['interest_coverage_ratio'] >= 5)
        self.layout.addWidget(interest_coverage_label)

        current_ratio_label = QLabel(f"Current Ratio: {self.liquidity_ratio_data['current_ratio']:.2f}", alignment=Qt.AlignLeft)
        self.set_label_color(current_ratio_label, self.liquidity_ratio_data['current_ratio'] >= 1)
        self.layout.addWidget(current_ratio_label)

        self.layout.addSpacing(10)

        efficiency_label = QLabel("➢ Efficiency", alignment=Qt.AlignLeft)
        efficiency_label.setStyleSheet(self.green)
        self.layout.addWidget(efficiency_label)

        roa_label = QLabel(f"ROA: {self.profitability_rank_data['roa']:.2f}%", alignment=Qt.AlignLeft)
        self.set_label_color(roa_label, self.profitability_rank_data['roa'] >= 12)
        self.layout.addWidget(roa_label)

        roe_label = QLabel(f"ROE: {self.profitability_rank_data['roe']:.2f}%", alignment=Qt.AlignLeft)
        self.set_label_color(roe_label, self.profitability_rank_data['roe'] >= 5)
        self.layout.addWidget(roe_label)

        roic_label = QLabel(f"ROIC: {self.profitability_rank_data['roic']:.2f}%", alignment=Qt.AlignLeft)
        self.set_label_color(roic_label, self.profitability_rank_data['roic'] >= 12)
        self.layout.addWidget(roic_label)

        self.layout.addSpacing(10)

        price_estimates_label = QLabel("➢ Price Estimates", alignment=Qt.AlignLeft)
        price_estimates_label.setStyleSheet(self.green)
        self.layout.addWidget(price_estimates_label)

        pe_label = QLabel(f"P/E Ratio: {self.gf_value_rank_data['P/E Ratio']:.2f}", alignment=Qt.AlignLeft)
        self.set_label_color(pe_label, self.gf_value_rank_data['P/E Ratio'] <= 15)
        self.layout.addWidget(pe_label)

        peg_label = QLabel(f"PEG Ratio: {self.gf_value_rank_data['PEG Ratio']:.2f}", alignment=Qt.AlignLeft)
        self.set_label_color(peg_label, self.gf_value_rank_data['PEG Ratio'] <= 1)
        self.layout.addWidget(peg_label)

        ps_label = QLabel(f"P/S Ratio: {self.gf_value_rank_data['PS Ratio']:.2f}", alignment=Qt.AlignLeft)
        self.set_label_color(ps_label, self.gf_value_rank_data['PS Ratio'] <= 2)
        self.layout.addWidget(ps_label)

        pb_label = QLabel(f"P/B Ratio: {self.gf_value_rank_data['PB Ratio']:.2f}", alignment=Qt.AlignLeft)
        self.set_label_color(pb_label, self.gf_value_rank_data['PB Ratio'] <= 3)
        self.layout.addWidget(pb_label)

        p_fcf_label = QLabel(f"P/FCF Ratio: {self.gf_value_rank_data['P FCF']:.2f}", alignment=Qt.AlignLeft)
        self.set_label_color(p_fcf_label, self.gf_value_rank_data['P FCF'] <= 25)
        self.layout.addWidget(p_fcf_label)

        return self.layout
