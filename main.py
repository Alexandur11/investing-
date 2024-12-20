from app.error_logging import setup_logging
from app.models.main_window import MainWindow
import sys
from PySide6.QtWidgets import QApplication

setup_logging()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
