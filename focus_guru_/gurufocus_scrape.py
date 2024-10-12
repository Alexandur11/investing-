import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from collections import ChainMap


response = requests.get('https://www.gurufocus.com/stock/AAPL/summary')
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data from the tables
tables = pd.read_html(response.text, header=0)

# If you want to process JSON data from a <script> tag (adjust the selector as necessary)
script_data = soup.find('script', type='application/json')
if script_data:
    json_data = json.loads(script_data.string)
    # Assuming the JSON data structure is known, you can process it as needed
    # Example: Adjust according to the actual keys in the JSON data
    sub_table_values = [[{record["Name"]: record["Current"]} for record in json_data]]
else:
    sub_table_values = [[{record["Name"]: record["Current"]} for record in json.loads(e)] for e in [i.to_json(orient="records") for i in tables]]

sub_formatted = [dict(ChainMap(*a)) for a in sub_table_values]
print(json.dumps(sub_formatted, indent=4))
