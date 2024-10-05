import os
import webbrowser

firefox = webbrowser.get('firefox')
cookies_location = "C:\\Users\\user\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ur7elpgq.default-release\\cookies.sqlite"



def close_browser():
    os.system("taskkill /F /IM firefox.exe")
    print('Browser closed')

def clean_cookies():
    if os.path.exists(cookies_location):
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

search = 'CTVA'

close_browser()
clean_cookies()
open_focus_guru(search)
open_alpha_spread(search)
