"""
InsPyre.colorize.convert.convert_to_hsv
---------------------------------------

Module for converting color codes to HSV values.
"""

from typing import List, Tuple, Union

from ..__utils import verify_cmyk_value as _verify_cmyk
from ..__utils import verify_hex_number_value as _verify_hex
from ..__utils import verify_hsl_value as _verify_hsl
from ..__utils import verify_rgb_number_value as _verify_rgb
from .__convert_to_rgb import cmyk_to_rgb, hex_to_rgb, hsl_to_rgb
from .__helpers import normalize_rgb as _normalize_rgb


def rgb_to_hsv(
    rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an RGB color code to HSV.

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
    :return: The converted HSV values.
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

    r = r / 255
    g = g / 255
    b = b / 255
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    delta = max_value - min_value
    value = max_value
    saturation = delta / max_value

    if delta == 0:
        hue = 0.0
    elif max_value == r:
        hue = (g - b) / delta % 6
    elif max_value == g:
        hue = ((b - r) / delta) + 2
    elif max_value == b:
        hue = ((r - g) / delta) + 4

    hue *= 60
    if hue < 0:
        hue += 360.0

    hue = round(hue, decimal_places)
    saturation = round(saturation * 100, decimal_places)
    value = round(value * 100, decimal_places)

    if return_as_tuple:
        return (float(hue), float(saturation), float(value))
    return [float(hue), float(saturation), float(value)]


def hex_to_hsv(
    hex_: str,
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts a hex color code to HSV.

    :param hex_: The hex color value to convert.
    :type rgb: str
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb are not valid R, G, or B values.
    :return: The converted HSV values.
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

    return rgb_to_hsv([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hsl_to_hsv(
    hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSL color code to HSV.

    :param hsl: The HSL color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsl must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl are not valid H, S, or L values.
    :return: The converted HSV values.
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
    return rgb_to_hsv([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def cmyk_to_hsv(
    cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a CMYK color code to HSV.

    :param cmyk: The CMYK color value to convert. Accepts either a List or Tuple with four values.

        - each value in cmyk must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in cmyk are not valid H, S, or V values.
    :return: The converted HSV values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if len(cmyk) == 4 and isinstance(cmyk, (list, tuple)):
        for v in cmyk:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each cyan, magenta, yellow, and black value must be 'int' or 'float'.")
        c, m, y, k = cmyk

    else:
        raise TypeError(
            "cmyk accepts a List or Tuple with four values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    c = float(c)
    m = float(m)
    y = float(y)
    k = float(k)
    _verify_cmyk(c, m, y, k)

    r, g, b = cmyk_to_rgb([c, m, y, k])
    return rgb_to_hsv([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)
