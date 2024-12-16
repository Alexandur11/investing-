import asyncio
import logging
import time
import random

from app.event_handlers.focus_guru_scrape_handlers import scrape_focus_guru_data
from app.automation.google_cloud_automation_interactions import \
    collect_unfiltered_symbols_from_google_sheet_cloud, update_filtered_google_sheet_list_with_new_symbols
from app.automation.stock_analysis_utils.data_validators import data_validation_orchestrator

logger = logging.getLogger(__name__)

"""
Module: focus_guru_analysis_orchestrator

This module provides automation functionalities to scrape and analyze stock data from Focus Guru, 
validate the data against specific financial criteria, and update results to a Google Sheet.

Dependencies:
- asyncio
- logging
- time
- random
- app.event_handlers.focus_guru_scrape_handlers.scrape_focus_guru_data
- app.automation.google_cloud_automation_interactions.collect_unfiltered_symbols_from_google_sheet_cloud
- app.automation.google_cloud_automation_interactions.update_filtered_google_sheet_list_with_new_symbols
- app.automation.stock_analysis_utils.data_validators.data_validation_orchestrator

Functions:
- automated_focus_guru_scrape_orchestrator(columns)
- analyse_focus_guru_scraped_data(symbol)
"""


def automated_focus_guru_scrape_orchestrator(columns):
    """
        Orchestrates the automated process of scraping stock data from Focus Guru, validating it,
        and updating the filtered stock list in Google Sheets.

        Args:
            columns (int): The Column associated to a specific list of stocks from the Google Sheet.

        Workflow:
            1. Retrieves unfiltered stock symbols from a Google Sheet.
            2. For each symbol:
                - Scrapes data from Focus Guru.
                - Validates the scraped financial data against specified criteria.
                - Adds validated symbols to a filtered data list.
            3. Updates a Google Sheet with the filtered stock list if any valid symbols are found.

        Raises:
            Exception: Logs exceptions that occur during data scraping, validation, or Google Sheet updates.
        """

    filtered_data = []
    unfiltered_symbols = collect_unfiltered_symbols_from_google_sheet_cloud(columns)

    try:
        for index, symbol in enumerate(unfiltered_symbols):
            time.sleep(random.uniform(63, 183))
            try:
                scraped_data = scrape_focus_guru_data(symbol)
                if scraped_data:
                    financial_strengths = scraped_data['financial_strengths']
                    growth_rank = scraped_data['growth_rank']
                    liquidity_ratio = scraped_data['liquidity_ratio']
                    profitability_rank = scraped_data['profitability_rank']
                    gf_value_rank = scraped_data['gf_value_rank']

                    successful_validation = asyncio.run(data_validation_orchestrator(financial_strengths,
                                                                                     growth_rank,
                                                                                     liquidity_ratio,
                                                                                     profitability_rank,
                                                                                     gf_value_rank))

                    if successful_validation:
                        filtered_data.append(symbol)
                        logger.info(f'New stock discovered as potential investment {symbol}')

                    logger.info(f'{index}/{len(unfiltered_symbols)} analysed')
            except Exception as e:

                logger.exception(f'Error {e}')

    except Exception as e:
        logger.exception(f'Error occurred while analysing: {e}')

    if len(filtered_data) > 0:
        sheet_to_update = 'Filtered_stocks'
        update_filtered_google_sheet_list_with_new_symbols(filtered_data, sheet_to_update)

    logger.info('Nothing Found, task completed')


def analyse_focus_guru_scraped_data(symbol):
    """
    Analyzes and validates financial data for a single stock symbol scraped from Focus Guru.

    Args:
        symbol (str): The stock symbol to scrape and validate.

    Returns:
        int: The count of successful validations for the financial data points.

    Raises:
        Exception: Logs exceptions encountered during data scraping or validation.


    """

    try:
        scraped_data = scrape_focus_guru_data(symbol)
        if scraped_data:
            financial_strengths = scraped_data['financial_strengths']
            growth_rank = scraped_data['growth_rank']
            liquidity_ratio = scraped_data['liquidity_ratio']
            profitability_rank = scraped_data['profitability_rank']
            gf_value_rank = scraped_data['gf_value_rank']

            successful_validation = asyncio.run(data_validation_orchestrator(financial_strengths,
                                                                             growth_rank,
                                                                             liquidity_ratio,
                                                                             profitability_rank,
                                                                             gf_value_rank))

            return len([x for x in successful_validation if x])

    except Exception as e:
        logger.exception(e)
