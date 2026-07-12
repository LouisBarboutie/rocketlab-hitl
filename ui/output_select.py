from PySide6.QtWidgets import (
    QGroupBox,
    QPushButton,
    QLineEdit,
    QFormLayout,
    QHBoxLayout,
    QVBoxLayout,
)


class OutputSelection(QGroupBox):
    def __init__(self):
        super().__init__(title="Output selection")

        self.button_on = QPushButton("On")
        self.button_off = QPushButton("Off")
        self.button_output_voltage = QPushButton("Set")
        self.button_output_current = QPushButton("Set")
        self.output_voltage = QLineEdit()
        self.output_current = QLineEdit()

        form = QFormLayout()

        # Voltage target
        layout = QHBoxLayout()
        layout.addWidget(self.output_voltage)
        layout.addWidget(self.button_output_voltage)
        form.addRow("Target voltage (Volts): ", layout)

        # Current target
        layout = QHBoxLayout()
        layout.addWidget(self.output_current)
        layout.addWidget(self.button_output_current)
        form.addRow("Target current (Amps): ", layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_on)
        button_layout.addWidget(self.button_off)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(button_layout)
        self.setLayout(layout)
