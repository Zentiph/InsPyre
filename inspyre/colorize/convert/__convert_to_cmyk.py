"""
InsPyre.colorize.convert.convert_to_cmyk
----------------------------------------

Module for converting color codes to CMYK values.
"""

from typing import List, Tuple, Union

from ..__utils import verify_hex_number_value as _verify_hex
from ..__utils import verify_hsl_value as _verify_hsl
from ..__utils import verify_hsv_value as _verify_hsv
from ..__utils import verify_rgb_number_value as _verify_rgb
from .__convert_to_rgb import hex_to_rgb, hsl_to_rgb, hsv_to_rgb
from .__helpers import normalize_rgb as _normalize_rgb


def rgb_to_cmyk(
    rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an RGB color code to CMYK.

    :param rgb: The RGB color value to convert. Accepts either a List or Tuple with three values.

        - accepts:
        - int RGB values 0-255
        - float RGB values 0.0-1.0

    :type rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb are not valid R, G, or B values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
    """

    # if rgb contains a single list or tuple
    if not (len(rgb) == 3 and isinstance(rgb, (list, tuple))):
        raise TypeError(
            "rgb accepts either a List or Tuple with three values.")
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    r, g, b = _normalize_rgb(rgb)
    for color in (r, g, b):
        _verify_rgb(color)

    r_prime = r / 255
    g_prime = g / 255
    b_prime = b / 255
    k = 1 - max(r_prime, g_prime, b_prime)
    c = (1 - r_prime - k) / (1 - k) * 100
    m = (1 - g_prime - k) / (1 - k) * 100
    y = (1 - b_prime - k) / (1 - k) * 100
    k *= 100

    if return_as_tuple:
        return (float(round(c, decimal_places)),
                float(round(m, decimal_places)),
                float(round(y, decimal_places)),
                float(round(k, decimal_places)))
    return [float(round(c, decimal_places)),
            float(round(m, decimal_places)),
            float(round(y, decimal_places)),
            float(round(k, decimal_places))]


def hex_to_cmyk(
    hex_: str,
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts a hex color code to CMYK.

    :param hex_: The hex color value to convert.
    :type rgb: str
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb are not valid R, G, or B values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if not isinstance(hex_, str):
        raise TypeError("'hex_' must be type 'str'.")
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    _verify_hex(hex_)
    r, g, b = hex_to_rgb(hex_)

    return rgb_to_cmyk([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hsl_to_cmyk(
    hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSL color code to CMYK.

    :param hsl: The HSL color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsl must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl are not valid H, S, or L values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if len(hsl) == 3 and isinstance(hsl, (list, tuple)):
        for v in hsl:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and lightness value must be 'int' or 'float'.")
        h, s, l = hsl

    else:
        raise TypeError(
            "hsl accepts either a List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    _verify_hsl(h, s, l)

    r, g, b = hsl_to_rgb([h, s, l])
    return rgb_to_cmyk([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hsv_to_cmyk(
    hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSV color code to CMYK.

    :param hsv: The HSV color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsv must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv are not valid H, S, or L values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if len(hsv) == 3 and isinstance(hsv, (list, tuple)):
        for v in hsv:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and value value must be 'int' or 'float'.")
        h, s, l = hsv

    else:
        raise TypeError(
            "hsv accepts either a List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    _verify_hsv(h, s, l)

    r, g, b = hsv_to_rgb([h, s, l])
    return rgb_to_cmyk([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)
