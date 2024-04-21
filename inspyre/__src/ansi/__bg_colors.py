from typing import List, Tuple, Union

from .__classes import PredefinedColor
from .__funcs import hex_to_rgb
from .__utils import verify_hex_number_value, verify_rgb_number_value


def rgb_bg(*rgb_value: Union[int, List[int], Tuple[int]]) -> str:
    """Generates a ANSI escape code for colored text backgrounds using an RGB value.

    :param rgb_value: The RGB value to convert. Accepts either three int values or a single List[int] or Tuple[int] with three values.
    :type rgb_value: Union[int, List[int], Tuple[int]]
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: ANSI escape code correlating to the color input.
    :rtype: str
    """

    # if rgb_value contains a single list with three ints
    if len(rgb_value) == 1 and (isinstance(rgb_value[0], list) or isinstance(rgb_value[0], tuple)) and len(rgb_value[0]) == 3 and all(isinstance(rgb_value[0][v], int) for v in range(len(rgb_value[0]))):
        r, g, b = rgb_value[0]
    # if rgb_value contains three ints
    elif len(rgb_value) == 3 and all(isinstance(arg, int) for arg in rgb_value):
        r, g, b = rgb_value
    else:
        raise TypeError(
            "rgb_bg accepts either three int values or a single list[int] with three values.")

    for color in (r, g, b):
        verify_rgb_number_value(color)

    return f'\x1b[48;2;{r};{g};{b}m'


def hex_bg(
    hex_: str,
    /
) -> str:
    """Generates an ANSI escape code for colored text backgrounds using a hex value.

    :param hex_: The hexadecimal color value.
    :type hex_: str
    :raises TypeError: If the argument is not of the correct type.
    :raises ValueError: If the argument is not a valid hex value.
    :return: ANSI escape code correlating to the color input.
    :rtype: str
    """

    # value check
    if not isinstance(hex_, str):
        raise TypeError("hex_bg only accepts arguments of type 'str'.")
    if len(hex_) == 7 and not hex_.startswith('#'):
        raise ValueError(
            "hex_bg only accepts hex values of length 7 starting with '#'.")
    elif len(hex_) != 6 and len(hex_) != 7:
        raise ValueError(
            "hex_bg only accepts hex values of length 6, or length 7 starting with '#'.")

    hex_ = hex_.lstrip('#')
    verify_hex_number_value(hex_)

    r, g, b = hex_to_rgb(hex_)
    return rgb_bg(r, g, b)
