import logging

from PySide6.QtWidgets import QMessageBox

class MessageDialog:
    @staticmethod
    def show_message(title: str, message: str):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)  # You can use different icons
        msg_box.setStandardButtons(QMessageBox.Ok)  # Add OK button
        msg_box.exec()  # Display the message box

    @staticmethod
    def question_message(title: str, message: str, event):
        reply = QMessageBox.question(None,title, message,QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()  # Close the app or proceed with action
        else:
            event.ignore()  # Cancel the close event


def decide_the_stock_column(column_A,column_B,column_C,symbol,value):
    if value == 12:
        column_A.append(symbol)
    if value in range(9,12):
        column_B.append(symbol)
    if value == 8:
        column_C.append(symbol)


