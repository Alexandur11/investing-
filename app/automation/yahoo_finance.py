import yfinance as yf



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




