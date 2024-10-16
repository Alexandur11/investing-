
class ConfigCheck:
    CONFIG_FILE = 'checkbox_config.txt'

    def __init__(self,investing_ui):
        self.investing_ui = investing_ui

    def load_checkbox_config(self):
        try:
            with open(self.CONFIG_FILE, 'r') as f:
                lines = f.readlines()
                self.investing_ui.analytics_panel.setChecked(lines[0].strip() == 'True')
                self.investing_ui.alpha_spread.setChecked(lines[1].strip() == 'True')
                self.investing_ui.focus_guru.setChecked(lines[2].strip() == 'True')
                self.investing_ui.macro_trends.setChecked(lines[3].strip() == 'True')
                self.investing_ui.finance_charts.setChecked(lines[4].strip() == 'True')
                self.investing_ui.companies_market_cap.setChecked(lines[5].strip() == 'True')
        except FileNotFoundError:
            pass

    def save_checkbox_config(self):
        with open(self.CONFIG_FILE, 'w') as f:
            f.write(f"{self.investing_ui.analytics_panel.isChecked()}\n")
            f.write(f"{self.investing_ui.alpha_spread.isChecked()}\n")
            f.write(f"{self.investing_ui.focus_guru.isChecked()}\n")
            f.write(f"{self.investing_ui.macro_trends.isChecked()}\n")
            f.write(f"{self.investing_ui.finance_charts.isChecked()}\n")
            f.write(f"{self.investing_ui.companies_market_cap.isChecked()}\n")
