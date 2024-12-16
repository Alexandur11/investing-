import logging
import os
import webbrowser
from functools import lru_cache
import time

firefox = webbrowser.get('firefox')
cookies_location_file = "cookies_location.txt"
logger = logging.getLogger(__name__)


def close_browser():
    os.system("taskkill /IM firefox.exe")

    time.sleep(0.5)


@lru_cache(maxsize=None)
def get_cookies_location():
    if os.path.exists(cookies_location_file):
        with open(cookies_location_file, "r") as file:
            cookies_location = file.readline().strip()
            return cookies_location
    else:
        logger.info("Cookies location file not found.")


def clean_cookies():
    cookies_location = get_cookies_location()
    if cookies_location and os.path.exists(cookies_location):
        os.remove(cookies_location)
        logger.info("Cookies deleted successfully!")
    else:
        logger.info("Cookies file not found.")


def open_focus_guru(symbol: str):
    endpoint = f"https://www.gurufocus.com/stock/{symbol}/summary"
    firefox.open(endpoint)


def open_alpha_spread(symbol: str):
    endpoint = f"https://www.alphaspread.com/security/nyse/{symbol}/summary"
    firefox.open(endpoint)


def open_finance_charts(symbol: str):
    endpoint = f'https://www.financecharts.com/stocks/{symbol}'
    firefox.open(endpoint)


def open_macro_trends():
    endpoint = f'https://www.macrotrends.net'
    firefox.open(endpoint)


def open_companies_market_cap():
    endpoint = f'https://companiesmarketcap.com/'
    firefox.open(endpoint)
