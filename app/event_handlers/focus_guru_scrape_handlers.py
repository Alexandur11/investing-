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
"""

import logging
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from app.event_handlers.focus_guru_xpaths import (
    cash_to_debt,
    debt_to_equity,
    debt_to_ebitda,
    interest_coverage,
    three_year_revenue_growth_rate,
    current_ration,
    roe,
    roa,
    roic,
    pe_ratio,
    peg_ratio,
    ps_ratio,
    pb_ratio,
    p_to_fcf,
)

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

    options = Options()
    driver = webdriver.Chrome(options=options)
    url = f"https://www.gurufocus.com/stock/{symbol}/summary"
    driver.get(url)

    logger.info(f"Requesting data for {symbol}")

    try:
        results = {
            "financial_strengths": financial_strengths(driver),
            "growth_rank": growth_rank(driver),
            "liquidity_ratio": liquidity_ratio(driver),
            "profitability_rank": profitability_rank(driver),
            "gf_value_rank": gf_value_rank(driver),
        }
        logger.info(f"Successfully scraped available data for {symbol}")
        return results
    except (ValueError, TypeError):
        logger.exception(
            f"Scraping data failed, potentially due to invalid symbol: {symbol}"
        )

    driver.quit()


def financial_strengths(driver):
    """
    Parses financial strength metrics from the financial strength table.

    Args:
           Selenium driver: Selenium webdriver instance.

    Returns:
        dict: A dictionary containing the metrics:
            - cash_to_debt
            - debt_to_equity
            - debt_to_ebitda
            - interest_coverage_ratio

    Logs:
        - Exception details if any metric is missing or cannot be parsed.
    """
    try:
        data = {
            "cash_to_debt": driver.find_element(By.XPATH, cash_to_debt).text,
            "debt_to_equity": driver.find_element(By.XPATH, debt_to_equity).text,
            "debt_to_ebitda": driver.find_element(By.XPATH, debt_to_ebitda).text,
            "interest_coverage_ratio": driver.find_element(
                By.XPATH, interest_coverage
            ).text,
        }
        return data
    except NoSuchElementException:
        logger.error("Failed to parse financial strength metrics")


def liquidity_ratio(driver):
    """
    Parses liquidity ratio metrics from the liquidity ratio table.

    Args:
        Selenium driver: Selenium webdriver instance.

    Returns:
        dict: A dictionary containing the metric:
            - current_ratio

    Logs:
        - Exception details if the metric is missing or cannot be parsed.
    """

    try:
        data = {"current_ratio": driver.find_element(By.XPATH, current_ration).text}
        return data
    except NoSuchElementException:
        logger.error("Failed to parse liquidity ratio metrics")


def profitability_rank(driver):
    """
    Parses profitability rank metrics from the profitability rank table.

    Args:
        Selenium driver: Selenium webdriver instance.

    Returns:
        dict: A dictionary containing metrics:
            - roe
            - roa
            - roic

    Logs:
        - Exception details if any metric is missing or cannot be parsed.
    """
    try:
        data = {
            "roe": driver.find_element(By.XPATH, roe).text,
            "roa": driver.find_element(By.XPATH, roa).text,
            "roic": driver.find_element(By.XPATH, roic).text,
        }
        return data
    except NoSuchElementException:
        logger.error("Failed to parse profitability rank metrics")


def growth_rank(driver):
    """
    Parses growth rank metrics from the growth rank table.

    Args:
        driver (WebDriver): Selenium webdriver instance.

    Returns:
        dict: A dictionary containing the metric:
            - 3-Year Revenue Growth Rate

    Logs:
        - Exception details if the metric is missing or cannot be parsed.
    """

    try:
        data = {
            "3-Year Revenue Growth Rate": driver.find_element(
                By.XPATH, three_year_revenue_growth_rate
            ).text
        }
        return data
    except NoSuchElementException:
        logger.error("Failed to parse growth rank metrics")


def gf_value_rank(driver):
    """
    Parses GuruFocus value rank metrics from the GF value rank table.

    Args:
        Selenium driver: Selenium webdriver instance.

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

    try:
        data = {
            "P/E Ratio": driver.find_element(By.XPATH, pe_ratio).text,
            "PEG Ratio": driver.find_element(By.XPATH, peg_ratio).text,
            "PS Ratio": driver.find_element(By.XPATH, ps_ratio).text,
            "PB Ratio": driver.find_element(By.XPATH, pb_ratio).text,
            "P FCF": driver.find_element(By.XPATH, p_to_fcf).text,
        }

        return data
    except NoSuchElementException:
        logger.error("Failed to parse GuruFocus value rank metrics")
