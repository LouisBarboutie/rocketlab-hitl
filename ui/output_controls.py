import functools

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGroupBox, QVBoxLayout

from network.proxy import PsuProxy
from ui.output_select import OutputSelection
from ui.overcurrent_protect import OverCurrentProtection
from ui.overvoltage_protect import OverVoltageProtection


class OutputControls(QGroupBox):
    def __init__(self, psu_proxy: PsuProxy):
        super().__init__(title="PSU controls")
        self.psu_proxy = psu_proxy

        self.output_selection = OutputSelection()
        self.overcurrent_protection = OverCurrentProtection()
        self.overvoltage_protection = OverVoltageProtection()

        layout = QVBoxLayout()
        layout.addWidget(self.overvoltage_protection)
        layout.addWidget(self.overcurrent_protection)
        layout.addWidget(self.output_selection)
        self.setLayout(layout)

        # fmt: off

        # Connect the contained widgets to the proxy
        self.output_selection.button_output_voltage.clicked.connect(self.on_output_voltage_set)
        self.output_selection.button_output_current.clicked.connect(self.on_output_current_set)
        self.output_selection.button_on.clicked.connect(functools.partial(self.psu_proxy.set_output_status, True))
        self.output_selection.button_off.clicked.connect(functools.partial(self.psu_proxy.set_output_status, False))

        self.overvoltage_protection.button_overvoltage_protection.clicked.connect(self.on_overvoltage_set)
        self.overcurrent_protection.button_overcurrent_protection.clicked.connect(self.on_overcurrent_set)

        # fmt: on

    @Slot()
    def on_output_voltage_set(self):
        if not self.output_selection.output_voltage.text():
            return

        voltage = float(self.output_selection.output_voltage.text())
        self.psu_proxy.set_output_voltage(voltage)

    @Slot()
    def on_output_current_set(self):
        if not self.output_selection.output_current.text():
            return

        current = float(self.output_selection.output_current.text())
        self.psu_proxy.set_output_current(current)

    @Slot()
    def on_overvoltage_set(self):
        voltage = self.overvoltage_protection.overvoltage_input.text()
        if not voltage:
            return

        voltage = float(voltage)
        self.psu_proxy.set_voltage_protection_level(voltage)

    @Slot()
    def on_overcurrent_set(self):
        selection = self.overcurrent_protection.overcurrent_select.currentText()
        self.psu_proxy.set_current_protection(False if selection == "Off" else True)

        delay = self.overcurrent_protection.overcurrent_delay.text()
        if not delay:
            return

        delay = float(delay)
        self.psu_proxy.set_protection_delay(delay)
