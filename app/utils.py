import logging

from PySide6.QtWidgets import QMessageBox

class MessageDialog:
    @staticmethod
    def show_message(title: str, message: str):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    @staticmethod
    def question_message(title: str, message: str, event):
        reply = QMessageBox.question(None,title, message,QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()  # Close the app or proceed with action
            return True
        else:
            event.ignore()  # Cancel the close event


def decide_the_stock_column(column_A,column_B,column_C,symbol,value):

    if value > 10:
        column_A.append(symbol)
        return
    if value > 8:
        column_B.append(symbol)
        return
    if value >= 7:
        column_C.append(symbol)



