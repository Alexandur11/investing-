import os
import webbrowser
import time
from functools import lru_cache

firefox = webbrowser.get('firefox')
cookies_location_file = "cookies_location.txt"

def close_browser():
    os.system("taskkill /IM firefox.exe")
    print('Browser closed')
    time.sleep(0.5)

@lru_cache(maxsize=None)
def get_cookies_location():

    if os.path.exists(cookies_location_file):
        with open(cookies_location_file, "r") as file:
            cookies_location = file.readline().strip()
            return cookies_location
    else:
        print("Cookies location file not found.")
        return None

def clean_cookies():
    cookies_location = get_cookies_location()
    if cookies_location and os.path.exists(cookies_location):
        os.remove(cookies_location)
        print("Cookies deleted successfully!")
    else:
        print("Cookies file not found.")

def open_focus_guru(symbol: str):
    endpoint = f"https://www.gurufocus.com/stock/{symbol}/summary"
    firefox.open(endpoint)

def open_alpha_spread(symbol: str):
    endpoint = f"https://www.alphaspread.com/security/nyse/{symbol}/summary"
    firefox.open(endpoint)