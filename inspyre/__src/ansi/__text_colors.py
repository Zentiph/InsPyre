from typing import List, Tuple, Union

from .__classes import PredefinedColor
from .__funcs import hex_to_rgb
from .__utils import verify_hex_number_value, verify_rgb_number_value


def rgb_text(*args: Union[int, List[int], Tuple[int]]) -> str:
    """Generates a ANSI escape code for colored text using an RGB value.

    :param args: The RGB value to convert. Accepts either three int values or a single List[int] or Tuple[int] with three values.
    :type args: Union[int, List[int], Tuple[int]]
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: ANSI escape code correlating to the color input.
    :rtype: str
    """

    # if args contains a single list with three ints
    if len(args) == 1 and (isinstance(args[0], list) or isinstance(args[0], tuple)) and len(args[0]) == 3 and all(isinstance(args[0][v], int) for v in range(len(args[0]))):
        r, g, b = args[0]
    # if args contains three ints
    elif len(args) == 3 and all(isinstance(arg, int) for arg in args):
        r, g, b = args
    else:
        raise TypeError(
            "rgb_text accepts either three int values or a single list[int] with three values.")

    for color in (r, g, b):
        verify_rgb_number_value(color)

    return f'\x1b[38;2;{r};{g};{b}m'


def hex_text(hex_: str, /) -> str:
    """Generates an ANSI escape code for colored text using a hex value.

    :param hex_: The hexadecimal color value.
    :type hex_: str
    :raises TypeError: If hex_ is not of the correct type.
    :raises ValueError: If hex_ is not a valid hex value.
    :return: ANSI escape code correlating to the color input.
    :rtype: str
    """

    # value check
    if not isinstance(hex_, str):
        raise TypeError("hex_text only accepts arguments of type 'str'.")

    hex_ = hex_.lstrip('#')
    verify_hex_number_value(hex_)

    r, g, b = hex_to_rgb(hex_)
    return rgb_text(r, g, b)
