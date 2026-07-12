import logging
from types import ModuleType
from typing import Dict, List

from PySide6.QtCore import QObject, Slot
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

import protocols.scpi
import protocols.gen


class EntryPoint(QObject):

    protocols: Dict[str, ModuleType] = {
        "SCPI": protocols.scpi,
        "GEN": protocols.gen,
    }

    baudrates: List[int] = [1_200, 2_400, 4_800, 9_600, 19_200, 38_400, 57_600]

    def __init__(self):
        super().__init__()
        self.port = QSerialPort()

        # This configuration is the default, but we set it explicitly anyways
        self.port.setParity(QSerialPort.Parity.NoParity)
        self.port.setStopBits(QSerialPort.StopBits.OneStop)
        self.port.setDataBits(QSerialPort.DataBits.Data8)

        self.protocol: ModuleType = protocols.scpi

    @staticmethod
    def list_ports() -> List[str]:
        return [port.portName() for port in QSerialPortInfo.availablePorts()]

    def select(self, deviceId: int):
        cmd = self.protocol.select(deviceId)

    @Slot(str)
    def set_port(self, port: str) -> None:
        self.port.setPortName(port)
        logging.info(f"Set port to {repr(port)}")

    @Slot(str)
    def set_protocol(self, protocol: str):
        if protocol not in EntryPoint.protocols:
            logging.error(f"Unsupported protocol {protocol}")

        self.protocol = EntryPoint.protocols[protocol]
        logging.info(f"Set protocol to {repr(protocol)}")

    @Slot(int)
    def set_baudrate(self, rate: int):
        if rate not in EntryPoint.baudrates:
            logging.error(
                f"Invalid baud rate {rate}, available rates are {", ".join(map(str, EntryPoint.baudrates))}"
            )

        self.port.setBaudRate(rate)
        logging.info(f"Set baud rate to {rate}")
