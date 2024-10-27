import asyncio
import time
import random

from app.models.event_handlers.focus_guru_scrape_handlers import scrape_focus_guru_data
from app.models.stock_analysis_automation.google_cloud_automation_interactions import \
    collect_unfiltered_symbols_from_google_sheet_cloud, update_filtered_google_sheet_list_with_new_symbols
from app.models.stock_analysis_automation.stock_analysis_utils.data_validators import data_validation_orchestrator


def automated_focus_guru_scrape_orchestrator():
    filtered_data = []

    unfiltered_symbols = collect_unfiltered_symbols_from_google_sheet_cloud(9)

    try:
        for index,symbol in enumerate(unfiltered_symbols[9:13]):
            time.sleep(random.uniform(5, 15))
            try:
                scraped_data = scrape_focus_guru_data(symbol)
                if scraped_data:
                    financial_strengths = scraped_data['financial_strengths']
                    growth_rank = scraped_data['growth_rank']
                    liquidity_ratio=scraped_data['liquidity_ratio']
                    profitability_rank=scraped_data['profitability_rank']
                    gf_value_rank=scraped_data['gf_value_rank']

                    successful_validation =  asyncio.run(data_validation_orchestrator(financial_strengths,
                                                                          growth_rank,
                                                                          liquidity_ratio,
                                                                          profitability_rank,
                                                                          gf_value_rank))

                    if successful_validation:
                        filtered_data.append(symbol)
                        print(f'New stock discovered as potential investment {symbol}')

                    print(f'{index}/{len(unfiltered_symbols)} analysed')
            except Exception as e:
                print(f'Error {e}')
    except Exception as e:
        print(f'Error occurred while analysing: {e}')


    # send_filtered_data_to_cloud_sheet
    update_filtered_google_sheet_list_with_new_symbols(filtered_data)

automated_focus_guru_scrape_orchestrator()