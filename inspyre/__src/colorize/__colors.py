"""__colors.py
Contains the TextColors and BGColors classes,
as well as colorizing functions such as format_text() and colorize_by_rgb.
"""

from typing import List, Tuple, Union

from .__classes import PredefinedColor
from .__constants import RESET
from .__utils import verify_cmyk_value as _verify_cmyk
from .__utils import verify_hex_number_value as _verify_hex
from .__utils import verify_hsl_value as _verify_hsl
from .__utils import verify_hsv_value as _verify_hsv
from .__utils import verify_rgb_number_value as _verify_rgb
from .convert import cmyk_to_rgb, hex_to_rgb, hsl_to_rgb, hsv_to_rgb


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
    else:
        fg_formatting = ''

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
    else:
        bg_formatting = ''

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


# color classes
class ColorLib:
    """Base class for color library classes.
    """

    def is_color(
        self,
        color: str,
        /
    ) -> bool:
        """Verifies if the given color name is a color in the class.

        :param color: The color to be verified.
        :type color: str
        :return: The status of the verification.
        :rtype: bool
        """

        for k in self.__class__.__dict__:
            if color.upper() == k:
                return True
        return False

    def print_color_sample(
        self,
        color: str,
        /,
        *,
        msg: str = "This text is {color}."
    ) -> None:
        """Prints a sample of the given color to the terminal.

        :param color: The color to be printed.
        :type color: str
        :raises ValueError: If the given color is not a color of the class.
        :raises TypeError: If any of the arguments are not of the correct type.
        :param msg: The message to be printed. Place {color} in the message to print the color name.
        :type msg: str, optional
        """

        if not isinstance(msg, str):
            raise TypeError("'msg' must be type 'str'.")

        if isinstance(color, str):
            color_name = color.replace(' ', '_').replace('-', '_').upper()

            if self.is_color(color_name):
                print(
                    f'{getattr(self.__class__, color_name)}{msg.format(color=color)}{RESET}')
            else:
                raise ValueError(
                    f'{color} is not a valid color of {self.__class__.__name__}.')

        else:
            raise TypeError("'color' must be type 'str'.")

    def compare_colors(
        self,
        *colors: str,
        msg: str = "This text is {color}."
    ) -> None:
        """Prints a sample of both colors side to side to compare them.

        :param colors: The colors to be compared.
        :type colors: str
        :param msg: The message to be printed. Place {color} in the message to print the color name.
        :type msg: str, optional
        """

        for color in colors:
            self.print_color_sample(color, msg=msg)


class TextColors(ColorLib):
    """Text color library class.
    """

    # reds
    MAROON = PredefinedColor('\x1b[38;2;128;0;0m')
    DARK_RED = PredefinedColor('\x1b[38;2;139;0;0m')
    BROWN = PredefinedColor('\x1b[38;2;165;42;42m')
    FIREBRICK = PredefinedColor('\x1b[38;2;178;34;34m')
    CRIMSON = PredefinedColor('\x1b[38;2;220;20;60m')
    RED = PredefinedColor('\x1b[38;2;255;0;0m')
    TOMATO = PredefinedColor('\x1b[38;2;255;99;71m')
    CORAL = PredefinedColor('\x1b[38;2;255;127;80m')
    INDIAN_RED = PredefinedColor('\x1b[38;2;205;92;92m')
    LIGHT_CORAL = PredefinedColor('\x1b[38;2;240;128;128m')
    DARK_SALMON = PredefinedColor('\x1b[38;2;233;150;122m')
    SALMON = PredefinedColor('\x1b[38;2;250;128;114m')
    LIGHT_SALMON = PredefinedColor('\x1b[38;2;255;160;122m')

    # oranges
    ORANGE_RED = PredefinedColor('\x1b[38;2;255;69;0m')
    DARK_ORANGE = PredefinedColor('\x1b[38;2;255;140;0m')
    ORANGE = PredefinedColor('\x1b[38;2;255;165;0m')

    # yellows
    GOLD = PredefinedColor('\x1b[38;2;255;215;0m')
    DARK_GOLDEN_ROD = PredefinedColor('\x1b[38;2;184;134;11m')
    GOLDEN_ROD = PredefinedColor('\x1b[38;2;218;165;32m')
    PALE_GOLDEN_ROD = PredefinedColor('\x1b[38;2;238;232;170m')
    DARK_KHAKI = PredefinedColor('\x1b[38;2;189;183;107m')
    KHAKI = PredefinedColor('\x1b[38;2;240;230;140m')
    OLIVE = PredefinedColor('\x1b[38;2;128;128;0m')
    YELLOW = PredefinedColor('\x1b[38;2;255;255;0m')

    # greens
    YELLOW_GREEN = PredefinedColor('\x1b[38;2;154;205;50m')
    DARK_OLIVE_GREEN = PredefinedColor('\x1b[38;2;85;107;47m')
    OLIVE_DRAB = PredefinedColor('\x1b[38;2;107;142;35m')
    LAWN_GREEN = PredefinedColor('\x1b[38;2;124;252;0m')
    CHARTREUSE = PredefinedColor('\x1b[38;2;127;255;0m')
    GREEN_YELLOW = PredefinedColor('\x1b[38;2;173;255;47m')
    DARK_GREEN = PredefinedColor('\x1b[38;2;0;100;0m')
    GREEN = PredefinedColor('\x1b[38;2;0;128;0m')
    FOREST_GREEN = PredefinedColor('\x1b[38;2;34;139;34m')
    LIME = PredefinedColor('\x1b[38;2;0;255;0m')
    LIME_GREEN = PredefinedColor('\x1b[38;2;50;205;50m')
    LIGHT_GREEN = PredefinedColor('\x1b[38;2;144;238;144m')
    PALE_GREEN = PredefinedColor('\x1b[38;2;152;251;152m')
    DARK_SEA_GREEN = PredefinedColor('\x1b[38;2;143;188;143m')
    MEDIUM_SPRING_GREEN = PredefinedColor('\x1b[38;2;0;250;154m')
    SPRING_GREEN = PredefinedColor('\x1b[38;2;0;255;127m')
    SEA_GREEN = PredefinedColor('\x1b[38;2;46;139;87m')
    MEDIUM_SEA_GREEN = PredefinedColor('\x1b[38;2;60;179;113m')
    MINT_CREAM = PredefinedColor('\x1b[38;2;245;255;250m')
    HONEYDEW = PredefinedColor('\x1b[38;2;240;255;240m')

    # blues
    MEDIUM_AQUA_MARINE = PredefinedColor('\x1b[38;2;102;205;170m')
    LIGHT_SEA_GREEN = PredefinedColor('\x1b[38;2;32;178;170m')
    DARK_SLATE_GRAY = PredefinedColor('\x1b[38;2;47;79;79m')
    TEAL = PredefinedColor('\x1b[38;2;0;128;128m')
    DARK_CYAN = PredefinedColor('\x1b[38;2;0;139;139m')
    AQUA = PredefinedColor('\x1b[38;2;0;255;255m')
    CYAN = PredefinedColor('\x1b[38;2;0;255;255m')
    LIGHT_CYAN = PredefinedColor('\x1b[38;2;224;255;255m')
    DARK_TURQUOISE = PredefinedColor('\x1b[38;2;0;206;209m')
    TURQUOISE = PredefinedColor('\x1b[38;2;64;224;208m')
    MEDIUM_TURQUOISE = PredefinedColor('\x1b[38;2;72;209;204m')
    PALE_TURQUOISE = PredefinedColor('\x1b[38;2;175;238;238m')
    AQUA_MARINE = PredefinedColor('\x1b[38;2;127;255;212m')
    POWDER_BLUE = PredefinedColor('\x1b[38;2;176;224;230m')
    CADET_BLUE = PredefinedColor('\x1b[38;2;95;158;160m')
    STEEL_BLUE = PredefinedColor('\x1b[38;2;70;130;180m')
    CORN_FLOWER_BLUE = PredefinedColor('\x1b[38;2;100;149;237m')
    DEEP_SKY_BLUE = PredefinedColor('\x1b[38;2;0;191;255m')
    DODGER_BLUE = PredefinedColor('\x1b[38;2;30;144;255m')
    LIGHT_BLUE = PredefinedColor('\x1b[38;2;173;216;230m')
    SKY_BLUE = PredefinedColor('\x1b[38;2;135;206;235m')
    LIGHT_SKY_BLUE = PredefinedColor('\x1b[38;2;135;206;250m')
    MIDNIGHT_BLUE = PredefinedColor('\x1b[38;2;25;25;112m')
    NAVY = PredefinedColor('\x1b[38;2;0;0;128m')
    DARK_BLUE = PredefinedColor('\x1b[38;2;0;0;139m')
    MEDIUM_BLUE = PredefinedColor('\x1b[38;2;0;0;205m')
    BLUE = PredefinedColor('\x1b[38;2;0;0;255m')
    ROYAL_BLUE = PredefinedColor('\x1b[38;2;65;105;225m')
    LIGHT_STEEL_BLUE = PredefinedColor('\x1b[38;2;176;196;222m')
    ALICE_BLUE = PredefinedColor('\x1b[38;2;240;248;255m')
    AZURE = PredefinedColor('\x1b[38;2;240;255;255m')

    # purples
    BLUE_VIOLET = PredefinedColor('\x1b[38;2;138;43;226m')
    INDIGO = PredefinedColor('\x1b[38;2;75;0;130m')
    DARK_SLATE_BLUE = PredefinedColor('\x1b[38;2;72;61;139m')
    SLATE_BLUE = PredefinedColor('\x1b[38;2;106;90;205m')
    MEDIUM_SLATE_BLUE = PredefinedColor('\x1b[38;2;123;104;238m')
    MEDIUM_PURPLE = PredefinedColor('\x1b[38;2;147;112;219m')
    DARK_MAGENTA = PredefinedColor('\x1b[38;2;139;0;139m')
    DARK_VIOLET = PredefinedColor('\x1b[38;2;148;0;211m')
    DARK_ORCHID = PredefinedColor('\x1b[38;2;153;50;204m')
    MEDIUM_ORCHID = PredefinedColor('\x1b[38;2;186;85;211m')
    PURPLE = PredefinedColor('\x1b[38;2;128;0;128m')
    LAVENDER = PredefinedColor('\x1b[38;2;0;0;0m')

    # pinks
    THISTLE = PredefinedColor('\x1b[38;2;216;191;216m')
    PLUM = PredefinedColor('\x1b[38;2;221;160;221m')
    VIOLET = PredefinedColor('\x1b[38;2;238;130;238m')
    MAGENTA = PredefinedColor('\x1b[38;2;255;0;255m')
    FUCHSIA = PredefinedColor('\x1b[38;2;255;0;255m')
    ORCHID = PredefinedColor('\x1b[38;2;218;112;214m')
    MEDIUM_VIOLET_RED = PredefinedColor('\x1b[38;2;199;21;133m')
    PALE_VIOLET_RED = PredefinedColor('\x1b[38;2;219;112;147m')
    DEEP_PINK = PredefinedColor('\x1b[38;2;255;20;147m')
    HOT_PINK = PredefinedColor('\x1b[38;2;255;105;180m')
    LIGHT_PINK = PredefinedColor('\x1b[38;2;255;182;193m')
    PINK = PredefinedColor('\x1b[38;2;255;192;203m')

    # whites
    ANTIQUE_WHITE = PredefinedColor('\x1b[38;2;250;235;215m')
    BEIGE = PredefinedColor('\x1b[38;2;245;245;220m')
    BISQUE = PredefinedColor('\x1b[38;2;255;228;196m')
    BLANCHED_ALMOND = PredefinedColor('\x1b[38;2;255;235;205m')
    WHEAT = PredefinedColor('\x1b[38;2;245;222;179m')
    CORN_SILK = PredefinedColor('\x1b[38;2;255;248;220m')
    LEMON_CHIFFON = PredefinedColor('\x1b[38;2;255;250;205m')
    LIGHT_GOLDEN_ROD_YELLOW = PredefinedColor('\x1b[38;2;250;250;210m')
    LIGHT_YELLOW = PredefinedColor('\x1b[38;2;255;255;224m')
    FLORAL_WHITE = PredefinedColor('\x1b[38;2;255;250;240m')
    GHOST_WHITE = PredefinedColor('\x1b[38;2;248;248;255m')
    IVORY = PredefinedColor('\x1b[38;2;255;255;240m')
    SNOW = PredefinedColor('\x1b[38;2;255;250;250m')
    WHITE = PredefinedColor('\x1b[38;2;255;255;255m')
    WHITE_SMOKE = PredefinedColor('\x1b[38;2;245;245;245m')

    # brown
    SADDLE_BROWN = PredefinedColor('\x1b[38;2;139;69;19m')
    SIENNA = PredefinedColor('\x1b[38;2;160;82;45m')
    CHOCOLATE = PredefinedColor('\x1b[38;2;210;105;30m')
    PERU = PredefinedColor('\x1b[38;2;205;133;63m')
    SANDY_BROWN = PredefinedColor('\x1b[38;2;244;164;96m')
    BURLY_WOOD = PredefinedColor('\x1b[38;2;222;184;135m')
    TAN = PredefinedColor('\x1b[38;2;210;180;140m')
    ROSY_BROWN = PredefinedColor('\x1b[38;2;188;143;143m')
    MOCCASIN = PredefinedColor('\x1b[38;2;255;228;181m')
    NAVAJO_WHITE = PredefinedColor('\x1b[38;2;255;222;173m')
    PEACH_PUFF = PredefinedColor('\x1b[38;2;255;218;185m')
    MISTY_ROSE = PredefinedColor('\x1b[38;2;255;228;225m')
    LAVENDER_BLUSH = PredefinedColor('\x1b[38;2;255;240;245m')
    LINEN = PredefinedColor('\x1b[38;2;250;240;230m')
    OLD_LACE = PredefinedColor('\x1b[38;2;253;245;230m')
    PAPAYA_WHIP = PredefinedColor('\x1b[38;2;255;239;213m')
    SEA_SHELL = PredefinedColor('\x1b[38;2;255;245;238m')

    # grays
    SLATE_GRAY = PredefinedColor('\x1b[38;2;112;128;144m')
    LIGHT_SLATE_GRAY = PredefinedColor('\x1b[38;2;119;136;153m')
    GAINSBORO = PredefinedColor('\x1b[38;2;220;220;220m')
    LIGHT_GRAY = PredefinedColor('\x1b[38;2;211;211;211m')
    SILVER = PredefinedColor('\x1b[38;2;192;192;192m')
    DARK_GRAY = PredefinedColor('\x1b[38;2;169;169;169m')
    GRAY = PredefinedColor('\x1b[38;2;128;128;128m')
    DIM_GRAY = PredefinedColor('\x1b[38;2;105;105;105m')
    BLACK = PredefinedColor('\x1b[38;2;0;0;0m')


class BGColors(ColorLib):
    """Background color library class.
    """

    # reds
    MAROON = PredefinedColor('\x1b[48;2;128;0;0m')
    DARK_RED = PredefinedColor('\x1b[48;2;139;0;0m')
    BROWN = PredefinedColor('\x1b[48;2;165;42;42m')
    FIREBRICK = PredefinedColor('\x1b[48;2;178;34;34m')
    CRIMSON = PredefinedColor('\x1b[48;2;220;20;60m')
    RED = PredefinedColor('\x1b[48;2;255;0;0m')
    TOMATO = PredefinedColor('\x1b[48;2;255;99;71m')
    CORAL = PredefinedColor('\x1b[48;2;255;127;80m')
    INDIAN_RED = PredefinedColor('\x1b[48;2;205;92;92m')
    LIGHT_CORAL = PredefinedColor('\x1b[48;2;240;128;128m')
    DARK_SALMON = PredefinedColor('\x1b[48;2;233;150;122m')
    SALMON = PredefinedColor('\x1b[48;2;250;128;114m')
    LIGHT_SALMON = PredefinedColor('\x1b[48;2;255;160;122m')

    # oranges
    ORANGE_RED = PredefinedColor('\x1b[48;2;255;69;0m')
    DARK_ORANGE = PredefinedColor('\x1b[48;2;255;140;0m')
    ORANGE = PredefinedColor('\x1b[48;2;255;165;0m')

    # yellows
    GOLD = PredefinedColor('\x1b[48;2;255;215;0m')
    DARK_GOLDEN_ROD = PredefinedColor('\x1b[48;2;184;134;11m')
    GOLDEN_ROD = PredefinedColor('\x1b[48;2;218;165;32m')
    PALE_GOLDEN_ROD = PredefinedColor('\x1b[48;2;238;232;170m')
    DARK_KHAKI = PredefinedColor('\x1b[48;2;189;183;107m')
    KHAKI = PredefinedColor('\x1b[48;2;240;230;140m')
    OLIVE = PredefinedColor('\x1b[48;2;128;128;0m')
    YELLOW = PredefinedColor('\x1b[48;2;255;255;0m')

    # greens
    YELLOW_GREEN = PredefinedColor('\x1b[48;2;154;205;50m')
    DARK_OLIVE_GREEN = PredefinedColor('\x1b[48;2;85;107;47m')
    OLIVE_DRAB = PredefinedColor('\x1b[48;2;107;142;35m')
    LAWN_GREEN = PredefinedColor('\x1b[48;2;124;252;0m')
    CHARTREUSE = PredefinedColor('\x1b[48;2;127;255;0m')
    GREEN_YELLOW = PredefinedColor('\x1b[48;2;173;255;47m')
    DARK_GREEN = PredefinedColor('\x1b[48;2;0;100;0m')
    GREEN = PredefinedColor('\x1b[48;2;0;128;0m')
    FOREST_GREEN = PredefinedColor('\x1b[48;2;34;139;34m')
    LIME = PredefinedColor('\x1b[48;2;0;255;0m')
    LIME_GREEN = PredefinedColor('\x1b[48;2;50;205;50m')
    LIGHT_GREEN = PredefinedColor('\x1b[48;2;144;238;144m')
    PALE_GREEN = PredefinedColor('\x1b[48;2;152;251;152m')
    DARK_SEA_GREEN = PredefinedColor('\x1b[48;2;143;188;143m')
    MEDIUM_SPRING_GREEN = PredefinedColor('\x1b[48;2;0;250;154m')
    SPRING_GREEN = PredefinedColor('\x1b[48;2;0;255;127m')
    SEA_GREEN = PredefinedColor('\x1b[48;2;46;139;87m')
    MEDIUM_SEA_GREEN = PredefinedColor('\x1b[48;2;60;179;113m')
    MINT_CREAM = PredefinedColor('\x1b[48;2;245;255;250m')
    HONEYDEW = PredefinedColor('\x1b[48;2;240;255;240m')

    # blues
    MEDIUM_AQUA_MARINE = PredefinedColor('\x1b[48;2;102;205;170m')
    LIGHT_SEA_GREEN = PredefinedColor('\x1b[48;2;32;178;170m')
    DARK_SLATE_GRAY = PredefinedColor('\x1b[48;2;47;79;79m')
    TEAL = PredefinedColor('\x1b[48;2;0;128;128m')
    DARK_CYAN = PredefinedColor('\x1b[48;2;0;139;139m')
    AQUA = PredefinedColor('\x1b[48;2;0;255;255m')
    CYAN = PredefinedColor('\x1b[48;2;0;255;255m')
    LIGHT_CYAN = PredefinedColor('\x1b[48;2;224;255;255m')
    DARK_TURQUOISE = PredefinedColor('\x1b[48;2;0;206;209m')
    TURQUOISE = PredefinedColor('\x1b[48;2;64;224;208m')
    MEDIUM_TURQUOISE = PredefinedColor('\x1b[48;2;72;209;204m')
    PALE_TURQUOISE = PredefinedColor('\x1b[48;2;175;238;238m')
    AQUA_MARINE = PredefinedColor('\x1b[48;2;127;255;212m')
    POWDER_BLUE = PredefinedColor('\x1b[48;2;176;224;230m')
    CADET_BLUE = PredefinedColor('\x1b[48;2;95;158;160m')
    STEEL_BLUE = PredefinedColor('\x1b[48;2;70;130;180m')
    CORN_FLOWER_BLUE = PredefinedColor('\x1b[48;2;100;149;237m')
    DEEP_SKY_BLUE = PredefinedColor('\x1b[48;2;0;191;255m')
    DODGER_BLUE = PredefinedColor('\x1b[48;2;30;144;255m')
    LIGHT_BLUE = PredefinedColor('\x1b[48;2;173;216;230m')
    SKY_BLUE = PredefinedColor('\x1b[48;2;135;206;235m')
    LIGHT_SKY_BLUE = PredefinedColor('\x1b[48;2;135;206;250m')
    MIDNIGHT_BLUE = PredefinedColor('\x1b[48;2;25;25;112m')
    NAVY = PredefinedColor('\x1b[48;2;0;0;128m')
    DARK_BLUE = PredefinedColor('\x1b[48;2;0;0;139m')
    MEDIUM_BLUE = PredefinedColor('\x1b[48;2;0;0;205m')
    BLUE = PredefinedColor('\x1b[48;2;0;0;255m')
    ROYAL_BLUE = PredefinedColor('\x1b[48;2;65;105;225m')
    LIGHT_STEEL_BLUE = PredefinedColor('\x1b[48;2;176;196;222m')
    ALICE_BLUE = PredefinedColor('\x1b[48;2;240;248;255m')
    AZURE = PredefinedColor('\x1b[48;2;240;255;255m')

    # purples
    BLUE_VIOLET = PredefinedColor('\x1b[48;2;138;43;226m')
    INDIGO = PredefinedColor('\x1b[48;2;75;0;130m')
    DARK_SLATE_BLUE = PredefinedColor('\x1b[48;2;72;61;139m')
    SLATE_BLUE = PredefinedColor('\x1b[48;2;106;90;205m')
    MEDIUM_SLATE_BLUE = PredefinedColor('\x1b[48;2;123;104;238m')
    MEDIUM_PURPLE = PredefinedColor('\x1b[48;2;147;112;219m')
    DARK_MAGENTA = PredefinedColor('\x1b[48;2;139;0;139m')
    DARK_VIOLET = PredefinedColor('\x1b[48;2;148;0;211m')
    DARK_ORCHID = PredefinedColor('\x1b[48;2;153;50;204m')
    MEDIUM_ORCHID = PredefinedColor('\x1b[48;2;186;85;211m')
    PURPLE = PredefinedColor('\x1b[48;2;128;0;128m')
    LAVENDER = PredefinedColor('\x1b[48;2;0;0;0m')

    # pinks
    THISTLE = PredefinedColor('\x1b[48;2;216;191;216m')
    PLUM = PredefinedColor('\x1b[48;2;221;160;221m')
    VIOLET = PredefinedColor('\x1b[48;2;238;130;238m')
    MAGENTA = PredefinedColor('\x1b[48;2;255;0;255m')
    FUCHSIA = PredefinedColor('\x1b[48;2;255;0;255m')
    ORCHID = PredefinedColor('\x1b[48;2;218;112;214m')
    MEDIUM_VIOLET_RED = PredefinedColor('\x1b[48;2;199;21;133m')
    PALE_VIOLET_RED = PredefinedColor('\x1b[48;2;219;112;147m')
    DEEP_PINK = PredefinedColor('\x1b[48;2;255;20;147m')
    HOT_PINK = PredefinedColor('\x1b[48;2;255;105;180m')
    LIGHT_PINK = PredefinedColor('\x1b[48;2;255;182;193m')
    PINK = PredefinedColor('\x1b[48;2;255;192;203m')

    # whites
    ANTIQUE_WHITE = PredefinedColor('\x1b[48;2;250;235;215m')
    BEIGE = PredefinedColor('\x1b[48;2;245;245;220m')
    BISQUE = PredefinedColor('\x1b[48;2;255;228;196m')
    BLANCHED_ALMOND = PredefinedColor('\x1b[48;2;255;235;205m')
    WHEAT = PredefinedColor('\x1b[48;2;245;222;179m')
    CORN_SILK = PredefinedColor('\x1b[48;2;255;248;220m')
    LEMON_CHIFFON = PredefinedColor('\x1b[48;2;255;250;205m')
    LIGHT_GOLDEN_ROD_YELLOW = PredefinedColor('\x1b[48;2;250;250;210m')
    LIGHT_YELLOW = PredefinedColor('\x1b[48;2;255;255;224m')
    FLORAL_WHITE = PredefinedColor('\x1b[48;2;255;250;240m')
    GHOST_WHITE = PredefinedColor('\x1b[48;2;248;248;255m')
    IVORY = PredefinedColor('\x1b[48;2;255;255;240m')
    SNOW = PredefinedColor('\x1b[48;2;255;250;250m')
    WHITE = PredefinedColor('\x1b[48;2;255;255;255m')
    WHITE_SMOKE = PredefinedColor('\x1b[48;2;245;245;245m')

    # browns
    SADDLE_BROWN = PredefinedColor('\x1b[48;2;139;69;19m')
    SIENNA = PredefinedColor('\x1b[48;2;160;82;45m')
    CHOCOLATE = PredefinedColor('\x1b[48;2;210;105;30m')
    PERU = PredefinedColor('\x1b[48;2;205;133;63m')
    SANDY_BROWN = PredefinedColor('\x1b[48;2;244;164;96m')
    BURLY_WOOD = PredefinedColor('\x1b[48;2;222;184;135m')
    TAN = PredefinedColor('\x1b[48;2;210;180;140m')
    ROSY_BROWN = PredefinedColor('\x1b[48;2;188;143;143m')
    MOCCASIN = PredefinedColor('\x1b[48;2;255;228;181m')
    NAVAJO_WHITE = PredefinedColor('\x1b[48;2;255;222;173m')
    PEACH_PUFF = PredefinedColor('\x1b[48;2;255;218;185m')
    MISTY_ROSE = PredefinedColor('\x1b[48;2;255;228;225m')
    LAVENDER_BLUSH = PredefinedColor('\x1b[48;2;255;240;245m')
    LINEN = PredefinedColor('\x1b[48;2;250;240;230m')
    OLD_LACE = PredefinedColor('\x1b[48;2;253;245;230m')
    PAPAYA_WHIP = PredefinedColor('\x1b[48;2;255;239;213m')
    SEA_SHELL = PredefinedColor('\x1b[48;2;255;245;238m')

    # grays
    SLATE_GRAY = PredefinedColor('\x1b[48;2;112;128;144m')
    LIGHT_SLATE_GRAY = PredefinedColor('\x1b[48;2;119;136;153m')
    GAINSBORO = PredefinedColor('\x1b[48;2;220;220;220m')
    LIGHT_GRAY = PredefinedColor('\x1b[48;2;211;211;211m')
    SILVER = PredefinedColor('\x1b[48;2;192;192;192m')
    DARK_GRAY = PredefinedColor('\x1b[48;2;169;169;169m')
    GRAY = PredefinedColor('\x1b[48;2;128;128;128m')
    DIM_GRAY = PredefinedColor('\x1b[48;2;105;105;105m')
    BLACK = PredefinedColor('\x1b[48;2;0;0;0m')
