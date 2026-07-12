import logging

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QGroupBox,
    QComboBox,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QFormLayout,
)
from PySide6.QtGui import QIntValidator
from network.proxy import PsuProxy

MIN_PSU_ADDRESS = 1
MAX_PSU_ADDRESS = 31


class SerialControls(QGroupBox):

    def __init__(self, entrypoint: PsuProxy):
        super().__init__(title="Serial controls")

        self.entrypoint = entrypoint

        # Create the widgets
        self.button_scan = QPushButton("Scan")
        self.port_select = QComboBox(placeholderText="--- select port ---")
        self.baudrate_select = QComboBox(placeholderText="--- select baud rate ---")
        self.address_select = QLineEdit()
        self.button_address_select = QPushButton("Select")
        self.protocol_select = QComboBox(placeholderText="--- select protocol ---")

        port_select_layout = QHBoxLayout()
        port_select_layout.addWidget(self.port_select)
        port_select_layout.addWidget(self.button_scan)

        address_select_layout = QHBoxLayout()
        address_select_layout.addWidget(self.address_select)
        address_select_layout.addWidget(self.button_address_select)

        # Add the widgets to the UI
        layout = QFormLayout(self)
        layout.addRow("Selected port: ", port_select_layout)
        layout.addRow("Baud rate: ", self.baudrate_select)
        layout.addRow("PSU address: ", address_select_layout)
        layout.addRow("Protocol: ", self.protocol_select)
        self.setLayout(layout)

        # Configure the available settings
        self.address_select.setValidator(
            QIntValidator(MIN_PSU_ADDRESS, MAX_PSU_ADDRESS)
        )

        for rate in PsuProxy.baudrates:
            self.baudrate_select.addItem(str(rate))

        for protocol in PsuProxy.protocols.keys():
            self.protocol_select.addItem(protocol)

        # Wire up the signals and slots
        self.button_scan.clicked.connect(self.scan)
        self.port_select.currentTextChanged.connect(self.entrypoint.set_port)
        self.button_address_select.clicked.connect(self.select)
        self.protocol_select.currentTextChanged.connect(self.entrypoint.set_protocol)
        self.baudrate_select.currentTextChanged.connect(
            lambda rate: self.entrypoint.set_baudrate(int(rate))
        )

    @Slot()
    def scan(self):
        self.port_select.clear()
        ports = PsuProxy.list_ports()
        logging.info(f"Found {len(ports)} available ports")
        for port in ports:
            self.port_select.addItem(port)

    @Slot()
    def select(self):
        if not self.address_select.hasAcceptableInput():
            logging.debug(f"Invalid selection {repr(self.address_select.text())}")
            return

        address = int(self.address_select.text())
        self.entrypoint.select(address)
