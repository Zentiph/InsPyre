"""
InsPyre.colorize.convert.convert_to_hex
---------------------------------------

Module for converting color codes to hex values.
"""

from typing import List, Tuple, Union

from ..__utils import verify_cmyk_value as _verify_cmyk
from ..__utils import verify_hsl_value as _verify_hsl
from ..__utils import verify_rgb_number_value as _verify_rgb
from .__convert_to_rgb import cmyk_to_rgb, hsl_to_rgb, hsv_to_rgb
from .__helpers import normalize_rgb as _normalize_rgb


def rgb_to_hex(
    rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    include_hashtag: bool = False
) -> str:
    """Converts an RGB color code to hexadecimal.

    :param rgb: The RGB value to convert. Accepts either a List or Tuple with three values.

        - accepts:
        - int RGB values 0-255
        - float RGB values 0.0-1.0

    :type rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    :param include_hashtag: Decides if the hashtag is included in the hex string, defaults to True.
    :type include_hashtag: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb are not valid R, G, or B values.
    :return: The converted hexadecimal value.
    :rtype: str
    """

    if not (len(rgb) == 3 and isinstance(rgb, (list, tuple)) and len(rgb) == 3):
        raise TypeError(
            "rgb accepts either a List or Tuple with three values.")
    if not isinstance(include_hashtag, bool):
        raise TypeError(
            "rgb_to_hex param 'include_hashtag' must be type 'bool'.")

    r, g, b = _normalize_rgb(rgb)
    for color in (r, g, b):
        _verify_rgb(color)

    if include_hashtag:
        return f'{r:02x}{g:02x}{b:02x}'
    return f'{r:02x}{g:02x}{b:02x}'
    # taken from educative.io:
    # https://www.educative.io/answers/how-to-convert-hex-to-rgb-and-rgb-to-hex-in-python


def hsl_to_hex(
    hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    include_hashtag: bool = False
) -> str:
    """Converts an HSL color code to RGB.

    :param hsl: The HSL color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsl must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param include_hashtag: Decides if the hashtag is included in the hex string, defaults to True.
    :type include_hashtag: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl are not valid H, S, or L values.
    :return: The converted hex value.
    :rtype: str
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

    if not isinstance(include_hashtag, bool):
        raise TypeError(
            "'include_hashtag' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    _verify_hsl(h, s, l)

    r, g, b = hsl_to_rgb(hsl)
    return rgb_to_hex([r, g, b], include_hashtag=include_hashtag)


def hsv_to_hex(
    hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    include_hashtag: bool = False
) -> str:
    """Converts an HSL color code to RGB.

    :param hsv: The HSV color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsv must be a percentage (e.g. 0.0-100.0, not 0.0-1.0

    :type hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param include_hashtag: Decides if the hashtag is included in the hex string, defaults to True.
    :type include_hashtag: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv are not valid H, S, or V values.
    :return: The converted hex value.
    :rtype: str
    """

    if len(hsv) == 3 and isinstance(hsv, (list, tuple)):
        for v in hsv:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and value value must be 'int' or 'float'.")
        h, s, v = hsv

    else:
        raise TypeError(
            "hsv accepts either a List or Tuple with three values.")

    if not isinstance(include_hashtag, bool):
        raise TypeError(
            "'include_hashtag' must be type 'bool'.")

    h = float(h)
    s = float(s)
    v = float(v)
    _verify_hsl(h, s, v)

    r, g, b = hsv_to_rgb([h, s, v])
    return rgb_to_hex([r, g, b], include_hashtag=include_hashtag)


def cmyk_to_hex(
    cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    include_hashtag: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a CMYK color code to hex.

    :param cmyk: The CMYK color value to convert. Accepts either a List or Tuple with four values.

        - each value in cmyk must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param include_hashtag: Decides if the hashtag is included in the hex string, defaults to True.
    :type include_hashtag: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in cmyk are not valid H, S, or V values.
    :return: The converted hex values.
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

    if not isinstance(include_hashtag, bool):
        raise TypeError(
            "'include_hashtag' must be type 'bool'.")

    c = float(c)
    m = float(m)
    y = float(y)
    k = float(k)
    _verify_cmyk(c, m, y, k)

    r, g, b = cmyk_to_rgb([c, m, y, k])
    return rgb_to_hex([r, g, b], include_hashtag=include_hashtag)
