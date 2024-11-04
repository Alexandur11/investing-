class ConfigCheck:
    CONFIG_FILE = 'checkbox_config.txt'

    def __init__(self,widget):
        self.analytics_panel = widget.analytics_check_box
        self.alpha_spread = widget.alpha_spread_check_box
        self.focus_guru = widget.focus_guru_check_box
        self.macro_trends = widget.macro_trends_check_box
        self.finance_charts = widget.finance_charts_check_box
        self.companies_market_cap = widget.companies_market_cap_check_box

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
            f.write(f"{ self.focus_guru.isChecked()}\n")
            f.write(f"{self.macro_trends.isChecked()}\n")
            f.write(f"{self.finance_charts.isChecked()}\n")
            f.write(f"{ self.companies_market_cap.isChecked()}\n")
