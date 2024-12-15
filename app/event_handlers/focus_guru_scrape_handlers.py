"""
Module for scraping and parsing financial data from GuruFocus.

This module uses `requests` to fetch HTML content from GuruFocus and `pandas` to extract
tables containing financial metrics. The module includes functions to parse data
such as financial strengths, liquidity ratios, profitability ranks, growth ranks,
and GuruFocus value ranks.

Dependencies:
- pandas
- requests
- logging
- io.StringIO

Logging:
Logs informative messages for successful operations and exceptions for failed attempts.

Author: [Your Name]
"""

import logging
import pandas as pd
import requests
from io import StringIO

logger = logging.getLogger(__name__)

def scrape_focus_guru_data(symbol: str):
    """
    Scrapes financial data from GuruFocus for a given stock symbol.

    Fetches data from the GuruFocus webpage and processes relevant tables
    for financial metrics. The extracted data is returned as a dictionary
    of parsed metrics.

    Args:
        symbol (str): The stock symbol to fetch data for.

    Returns:
        dict: A dictionary containing parsed data or None if scraping fails.

    Logs:
        - Informational messages when data is requested or successfully scraped.
        - Exception details if scraping fails or the symbol is invalid.
        - Informational message if the webpage cannot be retrieved.

    Example:
        results = scrape_focus_guru_data("AAPL")
    """
    url = f'https://www.gurufocus.com/stock/{symbol}/summary'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    logger.info(f'Requesting data for {symbol}')
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            tables = pd.read_html(StringIO(response.text))
            financial_strength_data = tables[0]
            growth_rank_data = tables[1]
            liquidity_ratio_data = tables[3]
            profitability_rank_data = tables[5]
            gf_value_rank_data = tables[6]

            results = {
                'financial_strengths': financial_strengths(financial_strength_data),
                'growth_rank': growth_rank(growth_rank_data),
                'liquidity_ratio': liquidity_ratio(liquidity_ratio_data),
                'profitability_rank': profitability_rank(profitability_rank_data),
                'gf_value_rank': gf_value_rank(gf_value_rank_data)
            }
            logger.info(f'Successfully scraped available data for {symbol}')
            return results
        except (ValueError, TypeError):
            logger.exception(f"Scraping data failed, potentially due to invalid symbol: {symbol}")
    else:
        logger.info(f"Failed to retrieve the webpage. Status code: {response.status_code}")

def financial_strengths(financial_strength_data):
    """
    Parses financial strength metrics from the financial strength table.

    Args:
        financial_strength_data (DataFrame): DataFrame containing financial strength data.

    Returns:
        dict: A dictionary containing the metrics:
            - cash_to_debt
            - debt_to_equity
            - debt_to_ebitda
            - interest_coverage_ratio

    Logs:
        - Exception details if any metric is missing or cannot be parsed.
    """
    data = {'cash_to_debt': None, 'debt_to_equity': None, 'debt_to_ebitda': None, 'interest_coverage_ratio': None}
    values = ['Cash-To-Debt', 'Debt-to-Equity', 'Debt-to-EBITDA', 'Interest Coverage']

    for d, v in zip(data.keys(), values):
        try:
            row = financial_strength_data[financial_strength_data['Name'] == v]
            if not row.empty:
                data[d] = float(row.iloc[0]['Current'])
        except Exception as e:
            logger.exception(f'Financial Strengths failed, missing {v}: {e}')

    return data

def liquidity_ratio(liquidity_ratio_data):
    """
    Parses liquidity ratio metrics from the liquidity ratio table.

    Args:
        liquidity_ratio_data (DataFrame): DataFrame containing liquidity ratio data.

    Returns:
        dict: A dictionary containing the metric:
            - current_ratio

    Logs:
        - Exception details if the metric is missing or cannot be parsed.
    """
    data = {'current_ratio': None}
    values = ['Current Ratio']

    for d, v in zip(data.keys(), values):
        try:
            row = liquidity_ratio_data[liquidity_ratio_data['Name'] == v]
            if not row.empty:
                data[d] = float(row.iloc[0]['Current'])
        except Exception as e:
            logger.exception(f'Liquidity ratio is missing {v}: {e}')

    return data

def profitability_rank(profitability_rank_data):
    """
    Parses profitability rank metrics from the profitability rank table.

    Args:
        profitability_rank_data (DataFrame): DataFrame containing profitability rank data.

    Returns:
        dict: A dictionary containing metrics:
            - roe
            - roa
            - roic

    Logs:
        - Exception details if any metric is missing or cannot be parsed.
    """
    data = {'roe': None, 'roa': None, 'roic': None}
    values = ['ROE %', 'ROA %', 'ROIC %']

    for d, v in zip(data.keys(), values):
        try:
            row = profitability_rank_data[profitability_rank_data['Name'] == v]
            if not row.empty:
                data[d] = float(row.iloc[0]['Current'])
        except Exception as e:
            logger.exception(f'Profitability rank is missing {v}: {e}')

    return data

def growth_rank(growth_rank_data):
    """
    Parses growth rank metrics from the growth rank table.

    Args:
        growth_rank_data (DataFrame): DataFrame containing growth rank data.

    Returns:
        dict: A dictionary containing the metric:
            - 3-Year Revenue Growth Rate

    Logs:
        - Exception details if the metric is missing or cannot be parsed.
    """
    data = {'3-Year Revenue Growth Rate': None}
    values = ['3-Year Revenue Growth Rate']

    for d, v in zip(data.keys(), values):
        try:
            row = growth_rank_data[growth_rank_data['Name'] == v]
            if not row.empty:
                data[d] = float(row.iloc[0]['Current'])
        except Exception as e:
            logger.exception(f'Growth rank is missing {v}: {e}')

    return data

def gf_value_rank(gf_value_rank_data):
    """
    Parses GuruFocus value rank metrics from the GF value rank table.

    Args:
        gf_value_rank_data (DataFrame): DataFrame containing GF value rank data.

    Returns:
        dict: A dictionary containing metrics:
            - P/E Ratio
            - PEG Ratio
            - PS Ratio
            - PB Ratio
            - Price-to-Free-Cash-Flow (P FCF)

    Logs:
        - Exception details if any metric is missing or cannot be parsed.
    """
    data = {'P/E Ratio': None, 'PEG Ratio': None, 'PS Ratio': None, 'PB Ratio': None, 'P FCF': None}
    values = ['PE Ratio', 'PEG Ratio', 'PS Ratio', 'PB Ratio', 'Price-to-Free-Cash-Flow']

    for d, v in zip(data.keys(), values):
        try:
            row = gf_value_rank_data[gf_value_rank_data['Name'] == v]
            if not row.empty:
                data[d] = float(row.iloc[0]['Current'])
        except Exception as e:
            logger.exception(f'GF value rank is missing {v}: {e}')
    return data
