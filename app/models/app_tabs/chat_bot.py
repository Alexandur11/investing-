import logging
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QButtonGroup, QWidget

from app.utils import GeminiWorker, OpenAIWorker, MessageDialog

logger = logging.getLogger(__name__)


class ChatBot(QWidget):
    """A widget that integrates with multiple chatbot models to process user prompts
        and display results asynchronously.
    """

    def __init__(self, widget):
        super().__init__()
        self.chat_bot_tab = widget

        self.worker = None
        self.worker_thread = None

        self.settings_group = QButtonGroup()
        self.settings_group.addButton(self.chat_bot_tab.gemini_flash_button)
        self.settings_group.addButton(self.chat_bot_tab.gemini_pro_button)
        self.settings_group.addButton(self.chat_bot_tab.gpt_4o_mini_button)

        self.message = MessageDialog()

        self.models = {'gemini-1.5-flash': GeminiWorker,
                       'gemini-1.5-pro': GeminiWorker,
                       'gpt-4o-mini': OpenAIWorker}

        self.chat_bot_tab.chat_bot_search_button.clicked.connect(
            lambda: self.trigger_method(self.chat_bot_tab.chat_bot_text_edit.toPlainText())
        )

    def trigger_method(self, prompt):

        """
               Triggers the chatbot functionality with the provided prompt.

               Parameters:
               -----------
               prompt : str
                   The user-provided input text to be processed by the selected chatbot model.

               Behavior:
               ---------
               1. Retrieves the selected chatbot model from the button group.
               2. Validates the prompt and model selection.
               3. Initializes the corresponding worker and runs it in a separate thread.
               4. Connects worker signals for processing and cleanup.
               5. Displays a message if no model is selected.

               """

        model = self.settings_group.checkedButton()

        if model:
            model_version = model.text()
            if prompt:
                self.chat_bot_tab.text_browser.append('-' * 120)
                self.chat_bot_tab.text_browser.append(f'Searching for {prompt}')
                self.chat_bot_tab.text_browser.append('-' * 120)

                self.worker = self.models[model_version](prompt=prompt, model=model_version)

                self.worker_thread = QThread()
                self.worker.moveToThread(self.worker_thread)

                # Connect signals
                self.worker_thread.started.connect(self.worker.run)  # Start the worker's run method
                self.worker.finished.connect(self.handle_response)  # When the worker finishes
                self.worker.finished.connect(self.worker_thread.quit)  # Stop the thread when done
                self.worker.finished.connect(self.worker.deleteLater)  # Clean up worker
                self.worker_thread.finished.connect(self.worker_thread.deleteLater)  # Clean up thread

                # Start the thread
                self.worker_thread.start()

                self.chat_bot_tab.chat_bot_text_edit.clear()

        else:
            self.message.show_message(title='Model Choice', message='Choose a model before prompting the Chat Bot')

    def handle_response(self, response):

        """Handles the response from the worker and appends it to the text browser."""

        self.chat_bot_tab.text_browser.append(response)
