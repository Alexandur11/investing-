import logging
import os

from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QMessageBox

from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()

import google.generativeai as genai
logger = logging.getLogger(__name__)

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


    logger.info('Scraped Data Parsed')
    return FinancialData(financial_strength_data=financial_strengths_data,
                         growth_rank_data=growth_rank_data,
                         liquidity_ratio_data=liquidity_ratio_data,
                         profitability_rank_data=profitability_rank_data,
                         gf_value_rank_data=gf_value_rank_data)




class LabelStyler:
    GREEN = "color: rgb(50, 205, 50);"
    RED = "color: rgb(255, 0, 0);"
    BLACK = "color: rgb(0, 0, 0);"
    YELLOW = 'COLOR: rgb(255, 255, 0)'

    @staticmethod
    def apply_style_filtering(object, information, condition):
        try:
            value = float(information.split(':')[1].strip())
            object.setText(information)
            object.setStyleSheet(LabelStyler.GREEN if condition(value) else LabelStyler.RED)
            object.setVisible(True)
        except Exception as e:
            logger.exception(e)

def prepare_values(data):
    try:
        return [
            (f'P/E: {data.gf_value_rank["P/E Ratio"]}', lambda x: x <= 23),
            (f'PEG: {data.gf_value_rank["PEG Ratio"]}', lambda x: x <= 1),
            (f'P/S: {data.gf_value_rank["PS Ratio"]}', lambda x: x <= 2),
            (f'P/B: {data.gf_value_rank["PB Ratio"]}', lambda x: x <= 3),
            (f'P/FCF: {data.gf_value_rank["P FCF"]}', lambda x: x <= 25),
            (f'C/D: {data.financial_strength["cash_to_debt"]}', lambda x: x >= 0.20),
            (f'D/E: {data.financial_strength["debt_to_equity"]}', lambda x: x <= 1),
            (f'D/EBITDA: {data.financial_strength["debt_to_ebitda"]}', lambda x: x <= 2.5),
            (f'IC: {data.financial_strength["interest_coverage_ratio"]}', lambda x: x >= 5),
            (f'CR: {data.liquidity_ratio["current_ratio"]}', lambda x: x >= 1),
            (f'ROA: {data.profitability_rank["roa"]}', lambda x: x >= 12),
            (f'ROE: {data.profitability_rank["roe"]}', lambda x: x >= 5),
            (f'ROIC: {data.profitability_rank["roic"]}', lambda x: x >= 12)
        ]
    except Exception as e:
        logger.exception(e)

def prepare_objects(comparison_tab, stock_frame):
    try:
        labels = [f'{stock_frame}_pe', f'{stock_frame}_peg',
                  f'{stock_frame}_ps', f'{stock_frame}_pb',
                  f'{stock_frame}_pfcf', f'{stock_frame}_cash_to_debt',
                  f'{stock_frame}_debt_to_equity', f'{stock_frame}_debt_to_ebitda',
                  f'{stock_frame}_interest_coverage', f'{stock_frame}_current_ratio',
                  f'{stock_frame}_roa', f'{stock_frame}_roe', f'{stock_frame}_roic']

        return [getattr(comparison_tab, x, None) for x in labels]
    except Exception as e:
        logger.exception(e)

class GeminiWorker(QObject):
    finished = Signal(str)

    def __init__(self, prompt,model):
        super().__init__()
        self.prompt = prompt
        self.model=model

    def run(self):
        result = self.gemini_request(self.prompt)
        self.finished.emit(result)

    def gemini_request(self, prompt):
        try:
            genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
            model = genai.GenerativeModel(self.model)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            logging.exception(e)


class OpenAIWorker(QObject):
    finished = Signal(str)

    def __init__(self, prompt,model):
        super().__init__()
        self.prompt = prompt
        self.model = model

    def run(self):
        result = self.open_ai_request(self.prompt)
        self.finished.emit(result)


    def open_ai_request(self, prompt):
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user",
                     "content": prompt}
                ]
            )

            result = response.choices[0].message.content
            cleaned = result.strip('```json\n').strip('\n```')
            return cleaned

        except Exception as e:
            logging.exception(e)