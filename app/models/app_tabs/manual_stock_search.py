import asyncio

from PySide6.QtWidgets import QWidget

from app.event_handlers.event_handlers import close_browser, open_focus_guru, open_alpha_spread, open_finance_charts, \
    open_macro_trends, open_companies_market_cap, clean_cookies
from app.event_handlers.focus_guru_scrape_handlers import scrape_focus_guru_data
from app.models.app_tabs.advisor_page import AdvisorPage, FinancialData

from app.utils import MessageDialog, parse_scraped_data


class ManualStockSearch(QWidget):

    def __init__(self, widget, configs):
        super().__init__()
        self.configs = configs
        self.manual_stock_control = widget
        self.manual_stock_control.stock_search_manual_button.clicked.connect(self.trigger_method)
        self.text_input = self.manual_stock_control.stock_search_manual_bar
        self.advisor_page = None

    def trigger_method(self):
        entered_symbol = self.text_input.text().strip()

        if not entered_symbol:
            MessageDialog.show_message(message='Please enter a symbol', title='Warning')
        else:
            async def async_wrapper():
                pass
                await asyncio.gather(
                    self.advisor_method(entered_symbol),
                    self.browser_methods(entered_symbol)
                )

            asyncio.run(async_wrapper())

            self.text_input.clear()

    async def advisor_method(self, symbol):
        advisor_method_status = self.configs.analytics_panel.isChecked()
        if advisor_method_status:
            data = scrape_focus_guru_data(symbol)
            if data:
                financial_data = parse_scraped_data(data)
                self.advisor_page = AdvisorPage(financial_data)
                self.advisor_page.setup_layout()

    async def browser_methods(self, entered_symbol):
        focus_guru_status = self.configs.focus_guru.isChecked()
        alpha_spread_status = self.configs.alpha_spread.isChecked()
        finance_charts_status = self.configs.finance_charts.isChecked()
        macro_trends_status = self.configs.macro_trends.isChecked()
        companies_market_cap_status = self.configs.companies_market_cap.isChecked()

        if any([focus_guru_status, alpha_spread_status, finance_charts_status,
                macro_trends_status, companies_market_cap_status]):
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
        if self.configs.analytics_panel.isChecked():
            await self.advisor_method(entered_symbol)
