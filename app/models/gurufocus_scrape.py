from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Set up Firefox options (e.g., headless mode if you don't need a UI)
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode

# Set the path to your Geckodriver
gecko_driver_path = "C:\\Python Projects\\geckodriver.exe"  # Escape backslashes
service = Service(gecko_driver_path)

# Initialize the WebDriver
driver = webdriver.Firefox(service=service, options=firefox_options)

# URL of the page to download
url = "https://www.gurufocus.com/stock/LDOS/summary"
driver.get(url)

# Wait for the page to load (adjust the delay if necessary)
time.sleep(5)  # Adjust based on your needs

# Get the page source
page_content = driver.page_source

# Save the content to a file
with open("../../page_content.html", "w", encoding="utf-8") as file:
    file.write(page_content)

# Close the browser
driver.quit()
