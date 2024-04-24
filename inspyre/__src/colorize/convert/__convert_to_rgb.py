"""
InsPyre.colorize.convert.convert_to_rgb
---------------------------------------

Module for converting color codes to RGB values.
"""

from typing import List, Tuple, Union

from ..__utils import verify_cmyk_value as _verify_cmyk
from ..__utils import verify_hex_number_value as _verify_hex
from ..__utils import verify_hsl_value as _verify_hsl
from ..__utils import verify_hsv_value as _verify_hsv
from .__helpers import hue_to_rgb as _hue_to_rgb


def hex_to_rgb(
    hex_: str,
    /,
    *,
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a hexadecimal color code to RGB.

    :param hex_: The hexadecimal color value to convert.
    :type hex_: str
    :param return_as_floats: Decides if the RGB value is returned as floats, defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If hex_ is not a valid hex value.
    :return: The converted RBG values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if not isinstance(hex_, str):
        raise TypeError("hex_to_rgb param 'hex_' must be type 'str'.")
    if not isinstance(return_as_floats, bool):
        raise TypeError(
            "'return_as_floats' must be type 'bool'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "hex_to_rgb param 'return_as_tuple' must be type 'bool'.")

    _verify_hex(hex_)

    hex_ = hex_.lstrip('#')
    r = int(hex_[:2], 16)
    g = int(hex_[2:4], 16)
    b = int(hex_[4:], 16)

    if return_as_floats:
        r = float(r / 255)
        g = float(g / 255)
        b = float(b / 255)

    if return_as_tuple:
        return (r, g, b)
    return [r, g, b]


def hsl_to_rgb(
    hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts an HSL color code to RGB.

    :param hsl: The HSL color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsl must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param return_as_floats: Decides if the RGB value is returned as floats, defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl are not valid H, S, or L values.
    :return: The converted RGB values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
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

    if not isinstance(return_as_floats, bool):
        raise TypeError(
            "'return_as_floats' must be type 'bool'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    h = float(h) / 60
    s = float(s) / 100
    l = float(l) / 100
    _verify_hsl(h, s, l)

    chroma = s * (1 - abs(2 * l - 1))
    middle_component = chroma * (1 - abs(h % 2 - 1))
    adjustment_factor = l - (chroma / 2)
    r, g, b = _hue_to_rgb(h, chroma, middle_component)

    r, g, b = [round((r + adjustment_factor) * 255),
               round((g + adjustment_factor) * 255),
               round((b + adjustment_factor) * 255)]

    if return_as_floats:
        r = float(r / 255)
        g = float(g / 255)
        b = float(b / 255)

    if return_as_tuple:
        return (r, g, b)
    return [r, g, b]


def hsv_to_rgb(
    hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts an HSV color code to RGB.

    :param hsv: The HSV color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsv must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param return_as_floats: Decides if the RGB value is returned as floats, defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv are not valid H, S, or V values.
    :return: The converted RGB values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if not (len(hsv) == 3 and isinstance(hsv, (list, tuple))):
        raise TypeError(
            "hsv accepts either a List or Tuple with three values.")
    if not isinstance(return_as_floats, bool):
        raise TypeError(
            "'return_as_floats' must be type 'bool'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    for v in hsv:
        if not isinstance(v, int) and not isinstance(v, float):
            raise TypeError(
                "Each hue, saturation, and value values must be 'int' or 'float'.")
    h, s, v = hsv

    h = float(h) / 60
    s = float(s) / 100
    v = float(v) / 100
    _verify_hsv(h, s, v)

    chroma = v * s
    middle_component = chroma * (1 - abs(h % 2 - 1))
    adjustment_factor = v - chroma
    r, g, b = _hue_to_rgb(h, chroma, middle_component)

    r, g, b = [round((r + adjustment_factor) * 255),
               round((g + adjustment_factor) * 255),
               round((b + adjustment_factor) * 255)]

    if return_as_floats:
        r = float(r / 255)
        g = float(g / 255)
        b = float(b / 255)

    if return_as_tuple:
        return (r, g, b)
    return [r, g, b]


def cmyk_to_rgb(
    cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a CMYK color code to RGB.

    :param cmyk: The CMYK color value to convert. Accepts either a List or Tuple with four values.

        - each value in cmyk must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param return_as_floats: Decides if the RGB value is returned as floats, defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in cmyk are not valid H, S, or V values.
    :return: The converted RGB values.
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

    if not isinstance(return_as_floats, bool):
        raise TypeError(
            "'return_as_floats' must be type 'bool'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    c = float(c)
    m = float(m)
    y = float(y)
    k = float(k)
    _verify_cmyk(c, m, y, k)

    c_prime = c / 100
    m_prime = m / 100
    y_prime = y / 100
    k_prime = k / 100

    r = round(255 * (1 - c_prime) * (1 - k_prime))
    g = round(255 * (1 - m_prime) * (1 - k_prime))
    b = round(255 * (1 - y_prime) * (1 - k_prime))

    if return_as_floats:
        r = float(r / 255)
        g = float(g / 255)
        b = float(b / 255)

    if return_as_tuple:
        return (int(r), int(g), int(b))
    return [int(r), int(g), int(b)]
