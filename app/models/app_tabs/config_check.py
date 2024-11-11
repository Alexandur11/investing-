import json


class ConfigCheck:
    CONFIG_FILE = 'checkbox_config.txt'
    SPREADSHEET_HISTORY = 'spreadsheet_history.txt'

    def __init__(self, widget):
        self.analytics_panel = widget.analytics_check_box
        self.alpha_spread = widget.alpha_spread_check_box
        self.focus_guru = widget.focus_guru_check_box
        self.macro_trends = widget.macro_trends_check_box
        self.finance_charts = widget.finance_charts_check_box
        self.companies_market_cap = widget.companies_market_cap_check_box
        self.latest_column = None

    def load_checkbox_config(self):
        try:
            with open(self.CONFIG_FILE, 'r') as f:
                lines = f.readlines()
                self.analytics_panel.setChecked(lines[0].strip() == 'True')
                self.alpha_spread.setChecked(lines[1].strip() == 'True')
                self.focus_guru.setChecked(lines[2].strip() == 'True')
                self.macro_trends.setChecked(lines[3].strip() == 'True')
                self.finance_charts.setChecked(lines[4].strip() == 'True')
                self.companies_market_cap.setChecked(lines[5].strip() == 'True')
        except FileNotFoundError:
            pass

    def save_checkbox_config(self):
        with open(self.CONFIG_FILE, 'w') as f:
            f.write(f"{self.analytics_panel.isChecked()}\n")
            f.write(f"{self.alpha_spread.isChecked()}\n")
            f.write(f"{self.focus_guru.isChecked()}\n")
            f.write(f"{self.macro_trends.isChecked()}\n")
            f.write(f"{self.finance_charts.isChecked()}\n")
            f.write(f"{self.companies_market_cap.isChecked()}\n")


def save_spreadsheet_activity_history(file='spreadsheet_history.txt', data=None):
    if data is None:
        print("No data provided to save.")
    try:
        json_data = json.dumps(data)

        with open(file, 'a') as f:
            f.write(f"{json_data}\n")
    except Exception as e:
        print(f"An error occurred while saving to the file: {e}")


def load_latest_spreadsheet_activity(file='spreadsheet_history.txt'):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("The file is empty.")
                return 0

            last_line = lines[-1].strip()
            last_activity = json.loads(last_line)
            last = last_activity.get('Latest Column Searched', None)

            return last if last != 59 else 0

    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Could not decode the JSON. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return 0
