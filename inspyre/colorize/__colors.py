"""__colors.py
Contains the TextColors and BGColors classes,
as well as colorizing functions such as format_text() and colorize_by_rgb.
"""

from re import compile as re_compile
from re import match as re_match
from re import split as re_split
from typing import Dict, List, Tuple, Union

from .__classes import PredefinedColor
from .__constants import RESET
from .__utils import verify_cmyk_value as _verify_cmyk
from .__utils import verify_hex_number_value as _verify_hex
from .__utils import verify_hsl_value as _verify_hsl
from .__utils import verify_hsv_value as _verify_hsv
from .__utils import verify_rgb_number_value as _verify_rgb
from .convert import (cmyk_to_rgb, hex_to_rgb, hsl_to_rgb, hsv_to_rgb,
                      rgb_to_cmyk, rgb_to_hex, rgb_to_hsl, rgb_to_hsv)


# color funcs
def format_text(
    txt: str,
    /,
    *formats: PredefinedColor
) -> str:
    """Formats a string with the color or styles given.
    Supports any predefined ANSI values from the TextColors, BGColors, and Styles classes,
    as well as user defined ANSI values via the AnsiFormat class.

    :param txt: The text to be formatted.
    :type txt: str
    :param formats: The formats to apply to the text.
    :type formats: Union[PredefinedColor, List[int], str]
    :raises TypeError: If any of the arguments are not of the correct type.
    :return: The formatted text.
    :rtype: str
    """

    # type checks
    if not isinstance(txt, str):
        raise TypeError("format_text param 'txt' must be type 'str'.")

    formatting = ''
    for format_ in formats:
        if not isinstance(format_, PredefinedColor):
            raise TypeError(
                "Each item in format_text param 'formats' must be type 'PredefinedColor'.")

        formatting += format_

    return formatting + txt + RESET


def colorize_by_rgb(
    txt: str,
    /,
    fg: Union[List[Union[int, float]], Tuple[Union[int, float]], None] = None,
    bg: Union[List[Union[int, float]], Tuple[Union[int, float]], None] = None
) -> str:
    """Colorizes the text with the given foreground and background RGB values.

    :param txt: The text to be colorized.
    :type txt: str
    :param fg: The foreground RGB value, if desired, defaults to None
    :type fg: Union[List[Union[int, float]], Tuple[Union[int, float]], None], optional
    :param bg: The background RGB value, if desired, defaults to None
    :type bg: Union[List[Union[int, float]], Tuple[Union[int, float]], None], optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If the given List(s) or Tuple(s) is the incorrect length.
    :raises ValueError: If the given RGB values are out of the correct range.
    :return: The colorized text.
    :rtype: str
    """

    # type checks
    if not isinstance(txt, str):
        raise TypeError("'txt' must be type 'str'.")

    for color in fg, bg:
        if not isinstance(color, list) and not isinstance(color, tuple) and color is not None:
            raise TypeError(
                "'fg' and 'bg' must be type 'List[int]', 'Tuple[int]', or 'None'.")
        if color is not None and len(color) != 3:
            raise ValueError(
                "All RGB value args must be a 'List[int]' or 'Tuple[int]' of length 3, or 'None'.")

    fg_formatting = ''
    bg_formatting = ''

    if fg:
        red_fg, green_fg, blue_fg = fg
        _verify_rgb(red_fg)
        _verify_rgb(green_fg)
        _verify_rgb(blue_fg)

        if isinstance(red_fg, float):
            red_fg = int(red_fg * 255)
        if isinstance(green_fg, float):
            green_fg = int(green_fg * 255)
        if isinstance(blue_fg, float):
            blue_fg = int(blue_fg * 255)

        fg_formatting = f'\x1b[38;2;{red_fg};{green_fg};{blue_fg}m'

    if bg:
        red_bg, green_bg, blue_bg = bg
        _verify_rgb(red_bg)
        _verify_rgb(green_bg)
        _verify_rgb(blue_bg)

        if isinstance(red_bg, float):
            red_bg = int(red_bg * 255)
        if isinstance(green_bg, float):
            green_bg = int(green_bg * 255)
        if isinstance(blue_bg, float):
            blue_bg = int(blue_bg * 255)

        bg_formatting = f'\x1b[48;2;{red_bg};{green_bg};{blue_bg}m'

    return fg_formatting + bg_formatting + txt + RESET


def colorize_by_hex(
    txt: str,
    /,
    fg: Union[str, None] = None,
    bg: Union[str, None] = None
) -> str:
    """Colorizes the text with the given foreground and background hex values.

    :param txt: The text to be colorized.
    :type txt: str
    :param fg: The foreground hex value, if desired, defaults to None
    :type fg: Union[str, None], optional
    :param bg: The background hex value, if desired, defaults to None
    :type bg: Union[str, None], optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If the given string(s) are the incorrect length.
    :raises ValueError: If the given hex values are out of the correct range.
    :return: The colorized text.
    :rtype: str
    """

    # type checks
    if not isinstance(txt, str):
        raise TypeError("'txt' must be type 'str'.")

    for color in fg, bg:
        if not isinstance(color, str) and color is not None:
            raise TypeError(
                "'fg' and 'bg' must be type 'str' or 'None'.")
        if color is not None and len(color) not in [6, 7]:
            raise ValueError(
                "All hex value arguments must be a 'str' of length 6 or 7, or 'None'.")

    if fg:
        _verify_hex(fg)
        red_fg, green_fg, blue_fg = hex_to_rgb(fg)
        fg_formatting = f'\x1b[38;2;{red_fg};{green_fg};{blue_fg}m'
    else:
        fg_formatting = ''

    if bg:
        _verify_hex(bg)
        red_bg, green_bg, blue_bg = hex_to_rgb(bg)
        bg_formatting = f'\x1b[48;2;{red_bg};{green_bg};{blue_bg}m'
    else:
        bg_formatting = ''

    return fg_formatting + bg_formatting + txt + RESET


def colorize_by_hsl(
    txt: str,
    /,
    fg: Union[List[Union[int, float]], Tuple[Union[int, float]], None] = None,
    bg: Union[List[Union[int, float]], Tuple[Union[int, float]], None] = None,
) -> str:
    """Colorizes the text with the given foreground and background HSL values.

    :param txt: The text to be colorized.
    :type txt: str
    :param fg: The foreground HSL value, if desired, defaults to None
    :type fg: Union[int, float], optional
    :param bg: The background HSL value, if desired, defaults to None
    :type bg: Union[int, float], optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If the given string(s) are the incorrect length.
    :raises ValueError: If the given HSL values are out of the correct range.
    :return: The colorized text.
    :rtype: str
    """

    # type checks
    if not isinstance(txt, str):
        raise TypeError("'txt' must be type 'str'.")

    for color in fg, bg:
        if not isinstance(color, list) and not isinstance(color, tuple) and color is not None:
            raise TypeError(
                "'fg' and 'bg' must be 'List[int | float]', 'Tuple[int | float]', or 'None'.")
        if color is not None and len(color) != 3:
            raise ValueError(
                "HSL vals must be 'List[int | float]' or 'Tuple[int | float]' of len 3, or 'None'.")

    if fg:
        _verify_hsl(fg[0], fg[1], fg[2])
        red_fg, green_fg, blue_fg = hsl_to_rgb(fg)
        fg_formatting = f'\x1b[38;2;{red_fg};{green_fg};{blue_fg}m'
    else:
        fg_formatting = ''

    if bg:
        _verify_hsl(bg[0], bg[1], bg[2])
        red_bg, green_bg, blue_bg = hsl_to_rgb(bg)
        bg_formatting = f'\x1b[48;2;{red_bg};{green_bg};{blue_bg}m'
    else:
        bg_formatting = ''

    return fg_formatting + bg_formatting + txt + RESET


def colorize_by_hsv(
    txt: str,
    /,
    fg: Union[List[Union[int, float]], Tuple[Union[int, float]], None] = None,
    bg: Union[List[Union[int, float]], Tuple[Union[int, float]], None] = None,
) -> str:
    """Colorizes the text with the given foreground and background HSV values.

    :param txt: The text to be colorized.
    :type txt: str
    :param fg: The foreground HSV value, if desired, defaults to None
    :type fg: Union[int, float], optional
    :param bg: The background HSV value, if desired, defaults to None
    :type bg: Union[int, float], optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If the given string(s) are the incorrect length.
    :raises ValueError: If the given HSV values are out of the correct range.
    :return: The colorized text.
    :rtype: str
    """

    # type checks
    if not isinstance(txt, str):
        raise TypeError("'txt' must be type 'str'.")

    for color in fg, bg:
        if not isinstance(color, list) and not isinstance(color, tuple) and color is not None:
            raise TypeError(
                "'fg' and 'bg' must be 'List[int | float]', 'Tuple[int | float]', or 'None'.")
        if color is not None and len(color) != 3:
            raise ValueError(
                "HSV vals must be 'List[int | float]' or 'Tuple[int | float]' of len 3, or 'None'.")

    if fg:
        _verify_hsv(fg[0], fg[1], fg[2])
        red_fg, green_fg, blue_fg = hsv_to_rgb(fg)
        fg_formatting = f'\x1b[38;2;{red_fg};{green_fg};{blue_fg}m'
    else:
        fg_formatting = ''

    if bg:
        _verify_hsv(bg[0], bg[1], bg[2])
        red_bg, green_bg, blue_bg = hsv_to_rgb(bg)
        bg_formatting = f'\x1b[48;2;{red_bg};{green_bg};{blue_bg}m'
    else:
        bg_formatting = ''

    return fg_formatting + bg_formatting + txt + RESET


def colorize_by_cmyk(
    txt: str,
    /,
    fg: Union[List[Union[int, float]], Tuple[Union[int, float]], None] = None,
    bg: Union[List[Union[int, float]], Tuple[Union[int, float]], None] = None,
) -> str:
    """Colorizes the text with the given foreground and background CMYK values.

    :param txt: The text to be colorized.
    :type txt: str
    :param fg: The foreground CMYK value, if desired, defaults to None
    :type fg: Union[int, float], optional
    :param bg: The background CMYK value, if desired, defaults to None
    :type bg: Union[int, float], optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If the given string(s) are the incorrect length.
    :raises ValueError: If the given CMYK values are out of the correct range.
    :return: The colorized text.
    :rtype: str
    """

    # type checks
    if not isinstance(txt, str):
        raise TypeError("'txt' must be type 'str'.")

    for color in fg, bg:
        if not isinstance(color, list) and not isinstance(color, tuple) and color is not None:
            raise TypeError(
                "'fg' and 'bg' must be 'List[int | float]', 'Tuple[int | float]', or 'None'.")
        if color is not None and len(color) != 4:
            raise ValueError(
                "CMYK val must be 'List[int | float]' or 'Tuple[int | float]' of len 4, or 'None'.")

    if fg:
        _verify_cmyk(fg[0], fg[1], fg[2], fg[3])
        red_fg, green_fg, blue_fg = cmyk_to_rgb(fg)
        fg_formatting = f'\x1b[38;2;{red_fg};{green_fg};{blue_fg}m'
    else:
        fg_formatting = ''

    if bg:
        _verify_cmyk(bg[0], bg[1], bg[2], bg[3])
        red_bg, green_bg, blue_bg = cmyk_to_rgb(bg)
        bg_formatting = f'\x1b[48;2;{red_bg};{green_bg};{blue_bg}m'
    else:
        bg_formatting = ''

    return fg_formatting + bg_formatting + txt + RESET


# color info / adjustment funcs

def get_colors(
    txt: str,
    /,
    *,
    return_as: str = 'rgb',
    include_reset: bool = False,
    include_color_type: bool = False
) -> List[Dict[str, Union[List[int], List[float], str]]]:
    """Gets all the colors in the given string and returns them in a list of dictionaries.

    :param txt: The text to parse.
    :type txt: str
    :param return_as: Determines the color type to return, defaults to 'rgb'.

        - supported return color types:
        - 'rgb' (default)
        - 'rgb float' / 'rgbf'
        - 'hex'
        - 'hsl'
        - 'hsv'
        - 'cmyk'

    :type return_as: str, optional
    :param include_reset: Determines whether to include the RESET constant if it is found in the string, defaults to False.
    :type include_reset: bool, optional
    :param include_color_type: Determines whether to include the color type of each color ('FG' or 'BG'), defaults to False.
    :type include_color_type: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :return: A list of dictionaries each representing the data of each color found.
    :rtype: List[Dict[str, Union[List[int], str]]]

        - 'color': The color as a list[int] for RGB or a str for hex.
        - 'type': Optional; 'FG' or 'BG' if 'include_color_type' is True.
    """

    # value checks
    if not isinstance(txt, str):
        raise TypeError(
            "get_colors param 'txt' only accepts type 'str'. If using a predefined color, use the color's 'get_rgb' or 'get_hex' method instead.")
    if not isinstance(return_as, str):
        raise TypeError(
            "get_colors param 'return_as' only accepts type 'bool'.")
    if not isinstance(include_reset, bool):
        raise TypeError(
            "get_colors param 'include_reset' only accepts type 'bool'.")
    if not isinstance(include_color_type, bool):
        raise TypeError(
            "get_colors param 'include_color_type' only accepts type 'bool'.")

    ansi_color_regex = r'\x1b\[((3[8]|4[8]);2);(\d+);(\d+);(\d+)m'
    reset_regex = r'\x1b\[0m'
    colors = []

    parts = re_split(f"({ansi_color_regex}|{reset_regex})", txt)

    for part in parts:
        if part:
            color_match = re_match(ansi_color_regex, part)
            if color_match:
                color_type_code, _, r, g, b = color_match.groups()

                match return_as.lower():
                    case 'rgb':
                        color = [int(r), int(g), int(b)]
                    case 'rgb float' | 'rgbf':
                        color = [float(r) / 255, float(g) /
                                 255, float(b) / 255]
                    case 'hex':
                        color = rgb_to_hex([int(r), int(g), int(b)])
                    case 'hsl':
                        color = rgb_to_hsl([int(r), int(g), int(b)])
                    case 'hsv':
                        color = rgb_to_hsv([int(r), int(g), int(b)])
                    case 'cmyk':
                        raise NotImplementedError
                    case _:
                        raise ValueError(
                            f"'{return_as}' is not a supported return color type.")

                if include_color_type:
                    color_type = "FG" if "38" in color_type_code else "BG"
                    colors.append({'color': color, 'type': color_type})
                else:
                    colors.append({'color': color})

            elif re_match(reset_regex, part) and include_reset:
                colors.append({'color': "RESET"})

    return colors


def remove_formatting(
    txt: str,
    /
) -> str:
    """Removes all color and style formatting from the string input.

    :param txt: The text to remove formatting from.
    :type txt: str
    :raises TypeError: If txt is not of the correct type.
    :return: The unformatted text.
    :rtype: str
    """

    if not isinstance(txt, str):
        raise TypeError("remove_formatting only accepts type 'str'.")

    ansi_code_regex = re_compile(r'\x1b\[([0-9A-Za-z;]*m)')
    return ansi_code_regex.sub('', txt)


def gradient(
    txt: str,
    /,
    left_color: Union[List[int], Tuple[int], str, PredefinedColor],
    right_color: Union[List[int], Tuple[int], str, PredefinedColor],
    *,
    color_type: str = 'FG'
) -> str:
    """Applies a gradient effect to the text. Automatically appends the RESET constant.

    :param txt: The text to apply the gradient on.
    :type txt: str
    :param left_color: The leftmost color. Currently only supports RGB and hex values.
    :type left_color: Union[List[int], Tuple[int], str, PredefinedColor]
    :param right_color: The rightmost color. Currently only supports RGB and hex values.
    :type right_color: Union[List[int], Tuple[int], str, PredefinedColor]
    :param color_type: The type of gradient to be applied, defaults to "FG". "FG" for foreground/text, "BG" for background.

        - Note: Predefined colors from the package do not determine the gradient type.
        - For instance, using two colors from BGColors with color_type='FG' will return a foreground gradient.

    :type color_type: str, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If the colors provided are not valid values for their respective color types.
    :return: The text string with the gradient applied.
    :rtype: str
    """

    # value checks
    if not isinstance(txt, str):
        raise TypeError("gradient param 'txt' only accepts type 'str'.")

    if len(txt) < 2:
        raise ValueError(
            "gradient param 'txt' cannot be less than 2 characters long.")

    if not isinstance(color_type, str):
        raise TypeError("gradient param 'color_type' only accepts type 'str'.")

    if color_type.lower().startswith('f'):
        escape_code_template = '\x1b[38;2;{};{};{}m'
    elif color_type.lower().startswith('b'):
        escape_code_template = '\x1b[48;2;{};{};{}m'
    else:
        raise ValueError(
            "gradient param 'color_type' only accepts strings starting with 't' or 'b'.")

    if isinstance(left_color, list) or isinstance(left_color, tuple):
        for x in left_color:
            _verify_rgb(x)

        if len(left_color) != 3:
            raise ValueError(
                "gradient param 'left_color' must have a length of 3.")

    # if color is string (hex), convert it to rgb
    elif isinstance(left_color, str):
        # don't need to verify hex val since hex_to_rgb already does
        left_color = hex_to_rgb(left_color)

    # if color is a PredefinedColor (predefined color)
    elif isinstance(left_color, PredefinedColor):
        left_color = left_color.get_rgb()

    else:
        raise TypeError(
            "gradient param 'left_color' only accepts type 'list[int]', 'tuple[int]', or 'str'.")

    if isinstance(right_color, list) or isinstance(right_color, tuple):
        for x in right_color:
            _verify_rgb(x)

        if len(right_color) != 3:
            raise ValueError(
                "gradient param 'right_color' must have a length of 3.")

    elif isinstance(right_color, str):
        right_color = hex_to_rgb(right_color)

    elif isinstance(right_color, PredefinedColor):
        right_color = right_color.get_rgb()

    else:
        raise TypeError(
            "gradient param 'right_color' only accepts type 'list[int]', 'tuple[int]', or 'str'.")

    # calculates the step for each color component based on the text length
    steps = [(end - start) / (len(txt) - 1)
             for start, end in zip(left_color, right_color)]

    gradient_text = ''

    for i, char in enumerate(txt):
        # calculates intermediate RGB values for each char
        r = int(left_color[0] + steps[0] * i)
        g = int(left_color[1] + steps[1] * i)
        b = int(left_color[2] + steps[2] * i)

        gradient_text += escape_code_template.format(r, g, b) + char

    # add RESET
    gradient_text += '\x1b[0m'

    return gradient_text
