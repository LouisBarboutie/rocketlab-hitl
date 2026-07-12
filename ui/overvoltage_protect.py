from PySide6.QtWidgets import (
    QGroupBox,
    QPushButton,
    QLineEdit,
    QFormLayout,
    QVBoxLayout,
)


class OverVoltageProtection(QGroupBox):

    def __init__(self):
        super().__init__(title="Over-voltage protection")

        self.button_overvoltage_protection = QPushButton("Set")
        self.overvoltage_input = QLineEdit()

        form = QFormLayout()
        form.addRow("Level (Volts):", self.overvoltage_input)
        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.button_overvoltage_protection)
        self.setLayout(layout)
