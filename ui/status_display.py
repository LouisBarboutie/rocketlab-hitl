from PySide6.QtWidgets import QGroupBox


class StatusDisplay(QGroupBox):

    def __init__(self):
        super().__init__(title="PSU status")
