import yfinance as yf

from app.models.stock_analysis_automation.google_cloud_automation_interactions import \
    collect_unfiltered_symbols_from_google_sheet_cloud, update_filtered_google_sheet_list_with_new_symbols


data = []

def filter_for_etf(column):
    unfiltered = collect_unfiltered_symbols_from_google_sheet_cloud(column)
    for x in unfiltered:
        try:
            symbol = yf.Ticker(x).info

            data.append([{x:symbol['quoteType']}])
            print(f'{x} symbol appended')
        except:
            print(f'{x} symbol does not exist')
            pass

    print(data)

for x in range(1,60):
    filter_for_etf(x)

print(data)




