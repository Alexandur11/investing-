from bs4 import BeautifulSoup
import chardet
import os

file_path = 'C:\\Python Projects\\investing-\\focus_guru.html'
try:
    # Try reading the file with different encodings
    encodings_to_try = ['utf-8', 'utf-16', 'latin-1']
    content = None

    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            print(f"Successfully read the file with encoding: {encoding}")
            break  # Exit loop if successful
        except UnicodeDecodeError:
            print(f"Failed to decode with encoding: {encoding}")

    if content is None:
        raise ValueError("Unable to read the file with the provided encodings.")

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Now you can extract data using BeautifulSoup
    financial_strength = soup.find('h2').text.strip()
    rows = soup.select('table.summary-table tbody tr')

    # Prepare a list to hold extracted data
    financial_data = []

    # Loop through each row and extract relevant information
    for row in rows:
        indicator_name = row.find('td', class_='t-caption p-v-sm semi-bold').text.strip()
        current_value = row.find('td', class_='t-caption').find('span', class_='p-l-sm').text.strip()

        # Extract values for Vs Industry and Vs History (if present)
        vs_industry = row.find_all('td')[3].find('div').find('div')['style'].split('width: ')[1].rstrip('%;')
        vs_history = row.find_all('td')[5].find('div').find('div')['style'].split('width: ')[1].rstrip('%;')

        financial_data.append({
            'Indicator Name': indicator_name,
            'Current Value': current_value,
            'Vs Industry': vs_industry,
            'Vs History': vs_history
        })

    # Print the extracted financial data
    print(financial_strength)
    for data in financial_data:
        print(data)

except FileNotFoundError:
    print(f"File '{file_path}' not found. Please check the path and filename.")
except Exception as e:
    print(f"An error occurred: {e}")