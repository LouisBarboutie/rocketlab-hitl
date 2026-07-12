from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
)


class OutputControls(QGroupBox):
    def __init__(self):
        super().__init__(title="PSU controls")

        output_control = QGroupBox("Output control")
        self.button_on = QPushButton("On")
        self.button_off = QPushButton("Off")
        layout = QHBoxLayout()
        layout.addWidget(self.button_on)
        layout.addWidget(self.button_off)
        layout.setStretch(0, 1)
        layout.setStretch(1, 1)
        output_control.setLayout(layout)

        overvoltage_control = QGroupBox("Over-voltage protection")
        self.button_overvoltage_protection = QPushButton("Set")
        self.max_voltage = QLineEdit()
        layout = QHBoxLayout()
        layout.addWidget(self.max_voltage)
        layout.addWidget(self.button_overvoltage_protection)
        layout.setStretch(0, 1)
        layout.setStretch(1, 1)
        overvoltage_control.setLayout(layout)

        overcurrent_control = QGroupBox("Over-current protection")
        self.button_overcurrent_protection = QPushButton("Set")
        self.max_current = QLineEdit()
        layout = QHBoxLayout()
        layout.addWidget(self.max_current)
        layout.addWidget(self.button_overcurrent_protection)
        layout.setStretch(0, 1)
        layout.setStretch(1, 1)
        overcurrent_control.setLayout(layout)

        self.button_output_voltage = QPushButton("Set")

        layout = QVBoxLayout()
        layout.addWidget(overvoltage_control)
        layout.addWidget(overcurrent_control)
        layout.addWidget(output_control)
        self.setLayout(layout)
