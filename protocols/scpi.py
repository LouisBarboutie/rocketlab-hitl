import logging


def select(deviceId: int) -> str:
    if deviceId < 1 or deviceId > 31:
        logging.error(
            f"Invalid device address {deviceId}, expected an address in the range [1..31]"
        )
        return ""

    command = f"INST:NSEL {deviceId}"
    return command


def set_output_voltage(voltage: float) -> str:
    return f"VOLT:LEV {voltage}"


def set_voltage_protection_level(voltage: float) -> str:
    return f"VOLT:PROT:LEV {voltage}"
