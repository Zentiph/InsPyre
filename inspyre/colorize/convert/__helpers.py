"""
InsPyre.colorize.convert.helpers
--------------------------------

Internal module containing helper functions for color conversions.
"""

from typing import List, Tuple, Union


def normalize_rgb(
    rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /
) -> Tuple[int]:
    """INTERNAL FUNCTION. Normalizes the RGB value if it is a float.

    :param rgb: The RGB value to normalize.
    :type rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    :return: The normalized RGB value.
    :rtype: Tuple[int]
    """

    for v in rgb:
        if not isinstance(v, (int, float)):
            raise TypeError(
                "Each RGB value must be 'int' or 'float'.")

    def normalize_value(v):
        return int(v * 255) if isinstance(v, float) else v

    return tuple(normalize_value(v) for v in rgb)


def hue_to_rgb(h: float, c: float, x: float):
    """Arranges RGB values base on the hue, chroma, and middle component.

    :param h: Hue.
    :type h: float
    :param c: _description_
    :type c: float
    :param x: _description_
    :type x: float
    :return: The properly arranged chroma and middle components.
    :rtype: tuple
    """

    if 0.0 <= h < 1.0:
        return c, x, 0
    if 1.0 <= h < 2.0:
        return x, c, 0
    if 2.0 <= h < 3.0:
        return 0, c, x
    if 3.0 <= h < 4.0:
        return 0, x, c
    if 4.0 <= h < 5.0:
        return x, 0, c
    return c, 0, x
