from PySide6.QtWidgets import (
    QGroupBox,
    QPushButton,
    QComboBox,
    QLineEdit,
    QFormLayout,
    QVBoxLayout,
)


class OverCurrentProtection(QGroupBox):

    def __init__(self):
        super().__init__(title="Over-current protection")

        self.button_overcurrent_protection = QPushButton("Set")
        self.overcurrent_select = QComboBox()
        self.overcurrent_select.addItem("Off")
        self.overcurrent_select.addItem("On")
        self.overcurrent_delay = QLineEdit()

        form = QFormLayout()
        form.addRow("Over-current active:", self.overcurrent_select)
        form.addRow("Over-current delay:", self.overcurrent_delay)
        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.button_overcurrent_protection)
        self.setLayout(layout)
