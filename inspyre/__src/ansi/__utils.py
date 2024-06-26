from re import compile


def verify_rgb_number_value(value: int) -> None:
    """INTERNAL FUNCTION. Raises ValueError if the RGB value is not valid.

    :param value: The R, G, or B value to check.
    :type value: int
    :raises TypeError: If value is not of the correct type.
    :raises ValueError: If value is not in the correct range for RGB values (0-255).
    """

    if type(value) is not int or isinstance(value, bool):
        raise TypeError("RGB value must be type 'int'.")

    if not 0 <= value <= 255:
        raise ValueError("RGB value must be an int from 0-255.")


def verify_hex_number_value(value: str) -> None:
    """INTERNAL FUNCTION. Raises ValueError if the hex value is not valid.

    :param value: The hex value to check.
    :type value: str
    :raises TypeError: If value is not of the correct type.
    :raises ValueError: If value is not in the correct range for hex values ('000000'-'FFFFFF').
    """

    if not isinstance(value, str):
        raise TypeError("hex value must be type 'str'.")

    value_int = int(value, base=16)
    if not 0 <= value_int <= 16777215:
        raise ValueError(
            f"hex value must be a str from '000000'-'FFFFFF'.")


def verify_ansi_code(ansi_code: str) -> None:
    """INTERNAL FUNCTION. Raises ValueError if the ANSI code is not valid.

    :param ansi_code: The ANSI code to check.
    :type ansi_code: str
    :raises TypeError: If ansi_code is not of the correct type.
    :raises ValueError: If ansi_code is not correctly formatted.
    """

    if not isinstance(ansi_code, str):
        raise TypeError("ANSI code must be type 'str'.")

    standard_color_pattern = compile(
        r'\x1b\[(?:3[0-7]|4[0-7]|9[0-7]|10[0-7])m')
    rgb_color_pattern = compile(
        r'\x1b\[(38|48);2;(\d{1,3});(\d{1,3});(\d{1,3})m')

    match = rgb_color_pattern.match(ansi_code)
    if match:
        r, g, b = map(int, match.groups()[1:])

        for value in r, g, b:
            if not 0 <= value <= 255:
                raise ValueError(
                    f"RGB value out of range in ANSI code: {ansi_code}.")

    if not standard_color_pattern.match(ansi_code) and not rgb_color_pattern.match(ansi_code):
        raise ValueError(
            f"Incorrect ANSI code formatting. Got: {ansi_code!r}. Expected format: standard color code or 24-bit RGB color code.")
