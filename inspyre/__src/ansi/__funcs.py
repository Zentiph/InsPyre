from re import compile as re_compile, match as re_match, split as re_split
from typing import Dict, List, Tuple, Union

from .__classes import PredefinedColor
from .__utils import verify_rgb_number_value, verify_hex_number_value


def rgb_to_hex(*rgb_value: Union[int, List[int], Tuple[int]], include_hashtag: bool = True) -> str:
    """Converts an RGB color code to hexadecimal.

    :param rgb_value: The RGB value to convert. Accepts either three int values or a single List[int] or Tuple[int] with three values.
    :type rgb_value: Union[int, List[int], Tuple[int]]
    :param include_hashtag: Boolean indicating whether to include the hashtag in the returned hex string or not, defaults to True.
    :type include_hashtag: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: The converted hexadecimal value.
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
            "rgb_to_hex accepts either three int values or a single list[int] or tuple[int] with three values.")

    if not isinstance(include_hashtag, bool):
        raise TypeError(
            "rgb_to_hex param 'include_hashtag' must be type 'bool'.")

    for color in (r, g, b):
        verify_rgb_number_value(color)

    if include_hashtag:
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)  # taken from educative.io
    else:
        return '{:02x}{:02x}{:02x}'.format(r, g, b)


def hex_to_rgb(hex_: str, /, *, return_tuple: bool = False) -> Union[List[int], Tuple[int]]:
    """Converts a hexadecimal color code to RGB.

    :param hex_: The hexadecimal color value to convert.
    :type hex_: str
    :param return_tuple: Determines whether to return the colors as a tuple or a list, defaults to False. If False, returns the colors as a list.
    :type return_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If hex_ is not a valid hex value.
    :return: The converted RBG values.
    :rtype: Union[List[int], Tuple[int]]
    """

    if not isinstance(hex_, str):
        raise TypeError("hex_to_rgb param 'hex_' must be type 'str'.")
    if not isinstance(return_tuple, bool):
        raise TypeError(
            "hex_to_rgb param 'return_tuple' must be type 'bool'.")

    hex_ = hex_.lstrip('#')
    verify_hex_number_value(hex_)

    if return_tuple:
        # taken from John1024 on stackoverflow
        return tuple(int(hex_[i:i+2], 16) for i in (0, 2, 4))
    return list(int(hex_[i:i+2], 16) for i in (0, 2, 4))


def get_colors(txt: str, /, *, return_hex: bool = False, include_reset: bool = False,
               include_color_type: bool = False) -> List[Dict[str, Union[List[int], str]]]:
    """Gets all the colors in the given string and returns them in a list of dictionaries.

    :param txt: The text to parse.
    :type txt: str
    :param return_hex: Determines whether to return the colors as hex, defaults to False. If False, returns the colors as RGB lists.
    :type return_hex: bool, optional
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
            "get_colors param 'txt' only accepts type 'str'. If using a predefined color from textformatting_vsct, use the color's 'get_rgb' or 'get_hex' method instead.")
    if not isinstance(return_hex, bool):
        raise TypeError(
            "get_colors param 'return_hex' only accepts type 'bool'.")
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
                color = rgb_to_hex(int(r), int(g), int(b)) \
                    if return_hex else [int(r), int(g), int(b)]

                if include_color_type:
                    color_type = "FG" if "38" in color_type_code else "BG"
                    colors.append({'color': color, 'type': color_type})
                else:
                    colors.append({'color': color})

            elif re_match(reset_regex, part) and include_reset:
                colors.append({'color': "RESET"})

    return colors


def remove_formatting(txt: str, /) -> str:
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


def gradient(txt: str, /, left_color: Union[List[int], Tuple[int], str, PredefinedColor],
             right_color: Union[List[int], Tuple[int], str, PredefinedColor], *, color_type: str = 'FG') -> str:
    """Applies a gradient effect to the text. Automatically appends the RESET constant.

    :param txt: The text to apply the gradient on.
    :type txt: str
    :param left_color: The leftmost color.
    :type left_color: Union[List[int], Tuple[int], str, PredefinedColor]
    :param right_color: The rightmost color.
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
            verify_rgb_number_value(x)

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
            verify_rgb_number_value(x)

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
