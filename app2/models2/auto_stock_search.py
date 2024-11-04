from app.models.stock_analysis_automation.focus_guru_automation_interactions import \
    automated_focus_guru_scrape_orchestrator


class AutoStockSearch:

    def __init__(self, widget):
        self.auto_stock_control = widget
        self.auto_stock_control.stock_search_automation_button.clicked.connect(self.trigger_method)
        self.options_bar = self.auto_stock_control.stock_search_auto_combo_box
        self.options_bar.addItems([str(x) for x in range(1,60)])

    def trigger_method(self):
        # Get selected value and convert to integer if needed
        try:
            selected_value = int(self.options_bar.currentText())
            automated_focus_guru_scrape_orchestrator(selected_value)
        except ValueError:
            print("Invalid selection. Please select a valid number.")

