import logging
from types import ModuleType
from typing import Dict, List

from PySide6.QtCore import QObject, Slot
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

import protocols.scpi
import protocols.gen


class PsuProxy(QObject):

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

    @Slot(str)
    def set_port(self, port: str) -> None:
        self.port.close()
        self.port.setPortName(port)
        logging.info(f"Set port to {repr(port)}")
        self.port.open(QSerialPort.OpenModeFlag.ReadWrite)

    @Slot(str)
    def set_protocol(self, protocol: str):
        if protocol not in PsuProxy.protocols:
            logging.error(f"Unsupported protocol {protocol}")

        self.protocol = PsuProxy.protocols[protocol]
        logging.info(f"Set protocol to {repr(protocol)}")

    @Slot(int)
    def set_baudrate(self, rate: int):
        if rate not in PsuProxy.baudrates:
            logging.error(
                f"Invalid baud rate {rate}, available rates are {", ".join(map(str, PsuProxy.baudrates))}"
            )

        self.port.setBaudRate(rate)
        logging.info(f"Set baud rate to {rate}")

    def send_command(self, command: str) -> None:
        data = f"{command}{self.protocol.EOM}"
        logging.debug(f"Sending command {repr(data)}")
        self.port.write(data.encode())

    def select(self, address: int):
        command = self.protocol.select(address)
        self.send_command(command)

    def set_output_voltage(self, voltage: float) -> None:
        command = self.protocol.set_output_voltage(voltage)
        self.send_command(command)

    def set_output_current(self, current: float) -> None:
        command = self.protocol.set_output_current(current)
        self.send_command(command)

    def set_voltage_protection_level(self, voltage: float) -> None:
        command = self.protocol.set_voltage_protection_level(voltage)
        self.send_command(command)

    def set_current_protection(self, status: bool) -> None:
        command = self.protocol.set_current_protection(status)
        self.send_command(command)

    def set_protection_delay(self, delay: float) -> None:
        command = self.protocol.set_protection_delay(delay)
        self.send_command(command)

    def set_output_status(self, status: bool) -> None:
        command = self.protocol.set_output_status(status)
        self.send_command(command)
