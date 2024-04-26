from re import compile as re_compile
from typing import Union


def verify_rgb_number_value(value: Union[int, float]) -> None:
    """INTERNAL FUNCTION. Raises ValueError if the RGB value is not valid.

    :param value: The R, G, or B value to check.
    :type value: int
    :raises TypeError: If value is not of the correct type.
    :raises ValueError: If value is not in the correct range for RGB values (0-255).
    """

    if type(value) is int and not isinstance(value, bool):
        if not 0 <= value <= 255:
            raise ValueError(
                "RGB value must be an int from 0-255 or a float from 0.0-1.0.")

    elif isinstance(value, float):
        if not 0.0 <= value <= 1.0:
            raise ValueError(
                "RGB value must be an int from 0-255 or a float from 0.0-1.0.")

    else:
        raise TypeError("RGB value must be type 'int'.")


def verify_hex_number_value(value: str) -> None:
    """INTERNAL FUNCTION. Raises ValueError if the hex value is not valid.

    :param value: The hex value to check.
    :type value: str
    :raises TypeError: If value is not of the correct type.
    :raises ValueError: If value is not in the correct range for hex values ('000000'-'FFFFFF').
    """

    if not isinstance(value, str):
        raise TypeError("hex value must be type 'str'.")

    value_int = int(value.lstrip('#'), base=16)
    if not 0 <= value_int <= 16777215:
        raise ValueError(
            f"hex value must be a str from '000000'-'FFFFFF'.")


def verify_hsl_value(
    hue: float,
    saturation: float,
    lightness: float
) -> None:
    """INTERNAL FUNCTION. Raises ValueError if the HSL value is not valid.

    :param hue: The hue of the HSL value to check.
    :type hue: str
    :param saturation: The saturation of the HSL value to check.
    :type saturation: str
    :param lightness: The lightness of the HSL value to check.
    :type lightness: str
    :raises TypeError: If the arguments are not of the correct type.
    :raises ValueError: If the arguments are not in the correct range for HSL values.
    """

    if not isinstance(hue, float):
        raise TypeError("hue must be type 'float'.")
    if not isinstance(saturation, float):
        raise TypeError("saturation must be type 'float'.")
    if not isinstance(lightness, float):
        raise TypeError("lightness must be type 'float'.")

    if hue < 0.0 or hue > 360.0:
        raise ValueError("hue must be a float from 0.0-360.0.")
    if saturation < 0.0 or saturation > 100.0:
        raise ValueError("saturation must be a float from 0.0-100.0.")
    if lightness < 0.0 or lightness > 100.0:
        raise ValueError("lightness must be a float from 0.0-100.0.")


def verify_hsv_value(
    hue: float,
    saturation: float,
    value: float
) -> None:
    """INTERNAL FUNCTION. Raises ValueError if the HSV value is not valid.

    :param hue: The hue of the HSV value to check.
    :type hue: str
    :param saturation: The saturation of the HSV value to check.
    :type saturation: str
    :param value: The value of the HSV value to check.
    :type value: str
    :raises TypeError: If the arguments are not of the correct type.
    :raises ValueError: If the arguments are not in the correct range for HSV values.
    """

    if not isinstance(hue, float):
        raise TypeError("hue must be type 'float'.")
    if not isinstance(saturation, float):
        raise TypeError("saturation must be type 'float'.")
    if not isinstance(value, float):
        raise TypeError("value must be type 'float'.")

    if hue < 0.0 or hue > 360.0:
        raise ValueError("hue must be a float from 0.0-360.0.")
    if saturation < 0.0 or saturation > 100.0:
        raise ValueError("saturation must be a float from 0.0-100.0.")
    if value < 0.0 or value > 100.0:
        raise ValueError("value must be a float from 0.0-100.0.")


def verify_cmyk_value(
    cyan: float,
    magenta: float,
    yellow: float,
    black: float
) -> None:
    """INTERNAL FUNCTION. Raises ValueError if the CMYK value is not valid.

    :param cyan: The cyan of the CMYK value to check.
    :type cyan: str
    :param magenta: The magenta of the CMYK value to check.
    :type magenta: str
    :param yellow: The yellow of the CMYK value to check.
    :type yellow: str
    :param black: The black of the CMYK value to check.
    :type black: str
    :raises TypeError: If the arguments are not of the correct type.
    :raises ValueError: If the arguments are not in the correct range for CMYK values.
    """

    if not isinstance(cyan, float):
        raise TypeError("cyan must be type 'float'.")
    if not isinstance(magenta, float):
        raise TypeError("magenta must be type 'float'.")
    if not isinstance(yellow, float):
        raise TypeError("yellow must be type 'float'.")
    if not isinstance(black, float):
        raise TypeError("black must be type 'float'.")

    if cyan < 0.0 or cyan > 100.0:
        raise ValueError("cyan must be a float from 0.0-100.0.")
    if magenta < 0.0 or magenta > 100.0:
        raise ValueError("magenta must be a float from 0.0-100.0.")
    if yellow < 0.0 or yellow > 100.0:
        raise ValueError("yellow must be a float from 0.0-100.0.")
    if black < 0.0 or black > 100.0:
        raise ValueError("black must be a float from 0.0-100.0.")


def verify_ansi_code(ansi_code: str) -> None:
    """INTERNAL FUNCTION. Raises ValueError if the ANSI code is not valid.

    :param ansi_code: The ANSI code to check.
    :type ansi_code: str
    :raises TypeError: If ansi_code is not of the correct type.
    :raises ValueError: If ansi_code is not correctly formatted.
    """

    if not isinstance(ansi_code, str):
        raise TypeError("ANSI code must be type 'str'.")

    standard_color_pattern = re_compile(
        r'\x1b\[(?:3[0-7]|4[0-7]|9[0-7]|10[0-7])m')
    rgb_color_pattern = re_compile(
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
