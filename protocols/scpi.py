EOM = "\r\n"  # End-Of-Message


def select(address: int) -> str:
    command = f"INST:NSEL {address}"
    return command


def set_output_voltage(voltage: float) -> str:
    return f"VOLT:LEV {voltage}"


def set_output_current(current: float) -> str:
    return f"CURR:LEV {current}"


def set_voltage_protection_level(voltage: float) -> str:
    return f"VOLT:PROT:LEV {voltage}"


def set_current_protection(status: bool) -> str:
    param = "CC" if status is True else "OFF"
    return f"OUTP:PROT:FOLD {param}"


def set_protection_delay(delay: float) -> str:
    return f"OUTP:PROT:DEL {delay}"


def set_output_status(status: bool) -> str:
    param = 1 if status is True else 0
    return f"OUTP {param}"
