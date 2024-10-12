import pandas as pd
import requests


def scrape_focus_guru_data(symbol:str):
    url = f'https://www.gurufocus.com/stock/{symbol}/summary'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }


    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        tables = pd.read_html(response.text, header=0)

        financial_strength_data = tables[0]
        growth_rank_data = tables[1]
        momentum_rank_data = tables[2]
        liquidity_ratio_data = tables[3]
        dividend_and_buy_back_data = tables[4]
        profitability_rank_data = tables[5]
        gf_value_rank_data = tables[6]

        financial_strengths(financial_strength_data)
        growth_rank(growth_rank_data)
        liquidity_ratio(liquidity_ratio_data)
        profitability_rank(profitability_rank_data)
        gf_value_rank(gf_value_rank_data)


    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



def financial_strengths(financial_strength_data):

    data = {'cash_to_debt':None,'debt_to_equity':None,'debt_to_ebitda':None,'interest_coverage_ratio':None}
    values = ['Cash-To-Debt','Debt-to-Equity','Debt-to-EBITDA','Interest Coverage']

    for d, v in zip(data.keys(), values):
        row = financial_strength_data[financial_strength_data['Name'] == v]
        if not row.empty:
            data[d] = row.iloc[0]['Current']

    return data
def liquidity_ratio(liquidity_ratio_data):
    data = {'current_ratio':None}
    values = ['Current Ratio']

    for d,v in zip(data.keys(),values):
        row = liquidity_ratio_data[liquidity_ratio_data['Name']==v]
        if not row.empty:
            data[d] = row.iloc[0]['Current']

    return data

def dividend_and_buy_back(dividend_and_buy_back_data):
    pass

def profitability_rank(profitability_rank_data):
    data = {'roe':None,'roa':None,'roic':None}
    values = ['ROE %','ROA %','ROIC %']

    for d,v in zip(data.keys(),values):
        row = profitability_rank_data[profitability_rank_data['Name'] == v]
        if not row.empty:
            data[d] = row.iloc[0]['Current']

    return data



def growth_rank(growth_rank_data):
    data = {'3-Year Revenue Growth Rate': None}
    values = ['3-Year Revenue Growth Rate']

    for d,v in zip(data.keys(),values):
        row = growth_rank_data[growth_rank_data['Name'] == v]
        if not row.empty:
            data[d] = row.iloc[0]['Current']

    return data

def gf_value_rank(gf_value_rank_data):
    data = {'P/E Ratio':None,'PEG Ratio': None,'PS Ratio':None,'PB Ratio':None,'P FCF': None}
    values = ['PE Ratio', 'PEG Ratio', 'PS Ratio', 'PB Ratio', 'Price-to-Free-Cash-Flow']

    for d,v in zip(data.keys(),values):
        row =  gf_value_rank_data[gf_value_rank_data['Name'] == v]
        if not row.empty:
            data[d] = row.iloc[0]['Current']

    return data

