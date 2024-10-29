import yfinance as yf

from app.models.stock_analysis_automation.google_cloud_automation_interactions import \
    collect_unfiltered_symbols_from_google_sheet_cloud, update_filtered_google_sheet_list_with_new_symbols



def filter_for_etf(column):
    unfiltered = collect_unfiltered_symbols_from_google_sheet_cloud(column)
    updated_list = []

    for x in unfiltered:
        try:
            symbol = yf.Ticker(x).info
            if symbol['quoteType'] != 'ETF' or symbol['legalType'] != 'Exchange Traded Fund':
                updated_list.append(x)
                print(f'{x} symbol appended')
        except:
            print(f'{x} symbol does not exist')
            pass

    update_filtered_google_sheet_list_with_new_symbols(updated_list)




filter_for_etf(25)