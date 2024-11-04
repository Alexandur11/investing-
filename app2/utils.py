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
