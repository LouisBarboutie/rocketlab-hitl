from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from ui.output_controls import OutputControls
from ui.serial_controls import SerialControls
from ui.status_display import StatusDisplay


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        serial_controls = SerialControls()
        output_controls = OutputControls()
        status_display = StatusDisplay()

        layout = QVBoxLayout()
        layout.addWidget(serial_controls)
        layout.addWidget(output_controls)
        layout.addWidget(status_display)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
