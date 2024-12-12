import logging
from PySide6.QtCore import QThread

from app.utils import GeminiWorker

logger = logging.getLogger(__name__)

class ChatBot:
    def __init__(self, widget):
        super().__init__()
        self.chat_bot_tab = widget
        self.worker = None
        self.worker_thread = None


        self.chat_bot_tab.chat_bot_search_button.clicked.connect(
            lambda: self.trigger_method(self.chat_bot_tab.chat_bot_text_edit.toPlainText())
        )

    def trigger_method(self, prompt):

        self.chat_bot_tab.chat_bot_text_edit.clear()
        self.chat_bot_tab.text_browser.append('-' * 120)


        self.worker = GeminiWorker(prompt)
        self.worker_thread = QThread()


        self.worker.moveToThread(self.worker_thread)

        # Connect signals
        self.worker.finished.connect(self.handle_response)  # When the worker finishes
        self.worker_thread.started.connect(self.worker.run)  # Start the worker's run method
        self.worker.finished.connect(self.worker_thread.quit)  # Stop the thread when done
        self.worker.finished.connect(self.worker.deleteLater)  # Clean up worker
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)  # Clean up thread

        # Start the thread
        self.worker_thread.start()

    def handle_response(self, response):
        self.chat_bot_tab.text_browser.append(response)
