import logging

from PySide6.QtWidgets import QMessageBox

class FinancialData:
    def __init__(self, financial_strength_data, growth_rank_data, liquidity_ratio_data,
                 profitability_rank_data, gf_value_rank_data):
        self.financial_strength = financial_strength_data
        self.growth_rank = growth_rank_data
        self.liquidity_ratio = liquidity_ratio_data
        self.profitability_rank = profitability_rank_data
        self.gf_value_rank = gf_value_rank_data

class MessageDialog:
    @staticmethod
    def show_message(title: str, message: str):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    @staticmethod
    def question_message(title: str, message: str, event):
        reply = QMessageBox.question(None,title, message,QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()  # Close the app or proceed with action
            return True
        else:
            event.ignore()  # Cancel the close event


def decide_the_stock_column(column_A,column_B,column_C,symbol,value):

    if value > 10:
        column_A.append(symbol)
        return
    if value > 8:
        column_B.append(symbol)
        return
    if value >= 7:
        column_C.append(symbol)

def parse_scraped_data(data):
    financial_strengths_data = data['financial_strengths']
    growth_rank_data = data['growth_rank']
    liquidity_ratio_data = data['liquidity_ratio']
    profitability_rank_data = data['profitability_rank']
    gf_value_rank_data = data['gf_value_rank']

    return FinancialData(financial_strength_data=financial_strengths_data,
                         growth_rank_data=growth_rank_data,
                         liquidity_ratio_data=liquidity_ratio_data,
                         profitability_rank_data=profitability_rank_data,
                         gf_value_rank_data=gf_value_rank_data)


