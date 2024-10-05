import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from app.models.dashboard import Dashboard

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("images/search_app.png"))


main = Dashboard()
main.show()
app.exec()