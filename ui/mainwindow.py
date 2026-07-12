from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLayout

from ui.output_controls import OutputControls
from ui.serial_controls import SerialControls
from network.proxy import PsuProxy


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        entrypoint = PsuProxy()
        serial_controls = SerialControls(entrypoint)
        output_controls = OutputControls(entrypoint)

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(serial_controls)
        layout.addWidget(output_controls)
        layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
