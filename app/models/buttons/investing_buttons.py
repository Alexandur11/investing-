import asyncio

from app.models.advisor_page import AdvisorPage
from app.models.event_handlers.focus_guru_scrape_handlers import scrape_focus_guru_data
from PySide6.QtWidgets import QPushButton
from app.models.event_handlers.event_handlers import *

class InvestingButton(QPushButton):
    def __init__(self, parent, text_input, feedback_label, investing_ui):
        super().__init__("Search", parent)
        self.text_input = text_input
        self.feedback_label = feedback_label
        self.investing_ui = investing_ui
        self.clicked.connect(self.trigger_method)

    def trigger_method(self):
        entered_symbol = self.text_input.text().strip()

        if not entered_symbol:
            self.feedback_label.setText("Please enter a valid stock symbol.")
            return

        self.advisor_method(entered_symbol)

        close_browser()
        clean_cookies()

        if self.investing_ui.focus_guru.isChecked():
            open_focus_guru(entered_symbol)
        if self.investing_ui.alpha_spread.isChecked():
            open_alpha_spread(entered_symbol)
        if self.investing_ui.finance_charts.isChecked():
            open_finance_charts(entered_symbol)
        if self.investing_ui.macro_trends.isChecked():
            open_macro_trends()
        if self.investing_ui.companies_market_cap.isChecked():
            open_companies_market_cap()

        self.text_input.clear()
        self.feedback_label.setText(f"Searching for {entered_symbol}...")

    def advisor_method(self,symbol):
        data = scrape_focus_guru_data(symbol)

        financial_strengths_data = data['financial_strengths']
        growth_rank_data = data['growth_rank']
        liquidity_ratio_data = data['liquidity_ratio']
        profitability_rank_data = data['profitability_rank']
        gf_value_rank_data=data['gf_value_rank']

        self.advisor_page = AdvisorPage(
            financial_strengths_data, growth_rank_data, liquidity_ratio_data,
            profitability_rank_data, gf_value_rank_data
        )
        self.advisor_page.setup_layout()

