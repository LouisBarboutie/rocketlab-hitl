EOM = "\r"  # End-Of-Message


def select(address: int) -> str:
    command = f"ADR {address}"
    return command


def set_output_voltage(voltage: float) -> str:
    return f"PV {voltage}"


def set_output_current(current: float) -> str:
    return f"PC {current}"


def set_voltage_protection_level(voltage: float) -> str:
    return f"OVP {voltage}"


def set_current_protection(status: bool) -> str:
    param = "CC" if status is True else "OFF"
    return f"FLD {param}"


def set_protection_delay(delay: float) -> str:
    return f"FBD {delay * 0.1}"


def set_output_status(status: bool) -> str:
    param = 1 if status is True else 0
    return f"OUTP {param}"
