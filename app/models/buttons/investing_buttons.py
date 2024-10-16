import asyncio

from app.models.advisor_page import AdvisorPage
from app.models.event_handlers.focus_guru_scrape_handlers import scrape_focus_guru_data
from PySide6.QtWidgets import QPushButton
from app.models.event_handlers.event_handlers import *
from app.models.user_interfaces.advisor_page_user_interface import FinancialData


class InvestingButton(QPushButton):
    def __init__(self, parent, text_input, feedback_label, investing_ui):
        super().__init__("Search", parent)
        self.advisor_page = None
        self.text_input = text_input
        self.feedback_label = feedback_label
        self.investing_ui = investing_ui
        self.clicked.connect(self.trigger_method)

    def trigger_method(self):
        entered_symbol = self.text_input.text().strip()

        if not entered_symbol:
            self.feedback_label.setText("Please enter a valid stock symbol.")
            return

        async def async_wrapper():
            await asyncio.gather(
                self.advisor_method(entered_symbol),
                self.browser_methods(entered_symbol)
            )

        asyncio.run(async_wrapper())

        self.text_input.clear()
        self.feedback_label.setText(f"Searching for {entered_symbol}...")

    async def advisor_method(self, symbol):
        data = scrape_focus_guru_data(symbol)
        if data:
            financial_strengths_data = data['financial_strengths']
            growth_rank_data = data['growth_rank']
            liquidity_ratio_data = data['liquidity_ratio']
            profitability_rank_data = data['profitability_rank']
            gf_value_rank_data = data['gf_value_rank']

            financial_data = FinancialData(financial_strength_data=financial_strengths_data,
                                           growth_rank_data=growth_rank_data,
                                           liquidity_ratio_data=liquidity_ratio_data,
                                           profitability_rank_data=profitability_rank_data,
                                           gf_value_rank_data=gf_value_rank_data)

            self.advisor_page = AdvisorPage(financial_data)
            self.advisor_page.setup_layout()

    async def browser_methods(self, entered_symbol):
        focus_guru_status = self.investing_ui.focus_guru.isChecked()
        alpha_spread_status = self.investing_ui.alpha_spread.isChecked()
        finance_charts_status = self.investing_ui.finance_charts.isChecked()
        macro_trends_status = self.investing_ui.macro_trends.isChecked()
        companies_market_cap_status = self.investing_ui.companies_market_cap.isChecked()

        if any([focus_guru_status,alpha_spread_status,finance_charts_status,
                macro_trends_status,companies_market_cap_status]):
            close_browser()
            clean_cookies()


            if focus_guru_status:
                open_focus_guru(entered_symbol)
            if alpha_spread_status:
                open_alpha_spread(entered_symbol)
            if finance_charts_status:
                open_finance_charts(entered_symbol)
            if macro_trends_status:
                open_macro_trends()
            if companies_market_cap_status:
                open_companies_market_cap()

    async def analytics_method(self, entered_symbol):
        if self.investing_ui.analytics_panel.isChecked():
            await self.advisor_method(entered_symbol)
