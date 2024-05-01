"""__colors.py
Contains color related classes such as FGColors, BGColors, and AnsiFormat.
"""

from __future__ import annotations

from .__utils import find_ansi_codes as _find_ansi_codes
from .__utils import verify_ansi_code as _verify_ansi
from .convert import rgb_to_cmyk as _rgb_to_cmyk
from .convert import rgb_to_hex as _rgb_to_hex
from .convert import rgb_to_hsl as _rgb_to_hsl
from .convert import rgb_to_hsv as _rgb_to_hsv


# TODO: move these two to a new module/package
class AnsiCursor:
    """Base class for ANSI code classes.

    [NOTE]
    For:
        - Styling codes (such as bold), use the AnsiFormat class.
        - Color codes, use the AnsiColor class.
        - Cursor movement, use the AnsiCursor class.
        - Terminal modes, use the AnsiTermMode class.
    """


class AnsiTermMode:
    """Base class for ANSI code classes.

    [NOTE]
    For:
        - Styling codes (such as bold), use the AnsiFormat class.
        - Color codes, use the AnsiColor class.
        - Cursor movement, use the AnsiCursor class.
        - Terminal modes, use the AnsiTermMode class.
    """


END_FORMAT = '\x1b[0m'
"""Constant that should be placed at the end of each string with formatting
in order to end the formatting. If not used, the formatting will carry over
to the next lines in the terminal.
"""


class Styles:
    """Contains text styling options such as bold, italic, etc.
    NOTE: Support varies for formats between terminal emulators,
    so some may not work depending on the terminal they are running in.
    """

    # main codes
    BOLD = '\x1b[1m'
    ITALIC = '\x1b[3m'
    UNDERLINE = '\x1b[4m'
    SWAP = '\x1b[7m'
    """Swaps the foreground and background colors.
    """
    HIDE = '\x1b[8m'
    """Prevents the text from being visible, but it still takes up space.
    """
    STRIKETHROUGH = '\x1b[9m'

    # rarely supported codes
    FAINT = '\x1b[2m'
    """!!! Not widely supported. !!!
    """
    SLOW_BLINK = '\x1b[5m'
    """!!! Not widely supported. !!!
    """
    RAPID_BLINK = '\x1b[6m'
    """!!! Not widely supported. !!!
    """
    DOUBLE_UNDERLINE = '\x1b[21m'
    """!!! Not widely supported. !!!
    """
    FRAME = '\x1b[51m'
    """!!! Not widely supported. !!!
    """
    ENCIRCLE = '\x1b[52m'
    """!!! Not widely supported. !!!
    """
    OVERLINE = '\x1b[53m'
    """!!! Not widely supported. !!!
    """

    # fonts
    FONT1 = '\x1b[11m'
    """!!! Not widely supported. !!!
    """
    FONT2 = '\x1b[12m'
    """!!! Not widely supported. !!!
    """
    FONT3 = '\x1b[13m'
    """!!! Not widely supported. !!!
    """
    FONT4 = '\x1b[14m'
    """!!! Not widely supported. !!!
    """
    FONT5 = '\x1b[15m'
    """!!! Not widely supported. !!!
    """
    FONT6 = '\x1b[16m'
    """!!! Not widely supported. !!!
    """
    FONT7 = '\x1b[17m'
    """!!! Not widely supported. !!!
    """
    FONT8 = '\x1b[18m'
    """!!! Not widely supported. !!!
    """
    FONT9 = '\x1b[19m'
    """!!! Not widely supported. !!!
    """
    FRAKTUR = '\x1b[20m'
    """!!! Not widely supported. !!!
    """

    # end formats
    # (some codes are copied for better user readability)
    END_BOLD = '\x1b[22m'
    """Removes the bold or faint effect.
    """
    END_FAINT = '\x1b[22m'
    """Removes the bold or faint effect.
    """
    END_ITALIC = '\x1b[23m'
    """Removes the italic effect, or fraktur.
    """
    END_FRAKTUR = '\x1b[23m'
    """Removes the italic effect, or fraktur.
    """
    END_UNDERLINE = '\x1b[24m'
    """Removes the underline effect.
    """
    END_BLINK = '\x1b[25m'
    """Removes the blink effect.
    """
    END_SWAP = '\x1b[27m'
    """Removes the swap effect.
    """
    UNHIDE = '\x1b[28m'
    """Re-enables text visibility.
    """
    END_STRIKETHROUGH = '\x1b[29m'
    """Removes the strikethrough effect.
    """
    END_FRAME = '\x1b[54m'
    """!!! Not widely supported. !!!
    """
    END_ENCIRCLE = '\x1b[54m'
    """!!! Not widely supported. !!!
    """
    END_OVERLINE = '\x1b[55m'
    """!!! Not widely supported. !!!
    """


class ColorLib:
    """Parent class for color library classes.
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
                    f'{getattr(self.__class__, color_name)}{msg.format(color=color)}{END_FORMAT}')
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


class FGColors(ColorLib):
    """Text color library class. Child of ColorLib.
    """

    # reds
    MAROON = '\x1b[38;2;128;0;0m'
    DARK_RED = '\x1b[38;2;139;0;0m'
    BROWN = '\x1b[38;2;165;42;42m'
    FIREBRICK = '\x1b[38;2;178;34;34m'
    CRIMSON = '\x1b[38;2;220;20;60m'
    RED = '\x1b[38;2;255;0;0m'
    TOMATO = '\x1b[38;2;255;99;71m'
    CORAL = '\x1b[38;2;255;127;80m'
    INDIAN_RED = '\x1b[38;2;205;92;92m'
    LIGHT_CORAL = '\x1b[38;2;240;128;128m'
    DARK_SALMON = '\x1b[38;2;233;150;122m'
    SALMON = '\x1b[38;2;250;128;114m'
    LIGHT_SALMON = '\x1b[38;2;255;160;122m'

    # oranges
    ORANGE_RED = '\x1b[38;2;255;69;0m'
    DARK_ORANGE = '\x1b[38;2;255;140;0m'
    ORANGE = '\x1b[38;2;255;165;0m'

    # yellows
    GOLD = '\x1b[38;2;255;215;0m'
    DARK_GOLDEN_ROD = '\x1b[38;2;184;134;11m'
    GOLDEN_ROD = '\x1b[38;2;218;165;32m'
    PALE_GOLDEN_ROD = '\x1b[38;2;238;232;170m'
    DARK_KHAKI = '\x1b[38;2;189;183;107m'
    KHAKI = '\x1b[38;2;240;230;140m'
    OLIVE = '\x1b[38;2;128;128;0m'
    YELLOW = '\x1b[38;2;255;255;0m'

    # greens
    YELLOW_GREEN = '\x1b[38;2;154;205;50m'
    DARK_OLIVE_GREEN = '\x1b[38;2;85;107;47m'
    OLIVE_DRAB = '\x1b[38;2;107;142;35m'
    LAWN_GREEN = '\x1b[38;2;124;252;0m'
    CHARTREUSE = '\x1b[38;2;127;255;0m'
    GREEN_YELLOW = '\x1b[38;2;173;255;47m'
    DARK_GREEN = '\x1b[38;2;0;100;0m'
    GREEN = '\x1b[38;2;0;128;0m'
    FOREST_GREEN = '\x1b[38;2;34;139;34m'
    LIME = '\x1b[38;2;0;255;0m'
    LIME_GREEN = '\x1b[38;2;50;205;50m'
    LIGHT_GREEN = '\x1b[38;2;144;238;144m'
    PALE_GREEN = '\x1b[38;2;152;251;152m'
    DARK_SEA_GREEN = '\x1b[38;2;143;188;143m'
    MEDIUM_SPRING_GREEN = '\x1b[38;2;0;250;154m'
    SPRING_GREEN = '\x1b[38;2;0;255;127m'
    SEA_GREEN = '\x1b[38;2;46;139;87m'
    MEDIUM_SEA_GREEN = '\x1b[38;2;60;179;113m'
    MINT_CREAM = '\x1b[38;2;245;255;250m'
    HONEYDEW = '\x1b[38;2;240;255;240m'

    # blues
    MEDIUM_AQUA_MARINE = '\x1b[38;2;102;205;170m'
    LIGHT_SEA_GREEN = '\x1b[38;2;32;178;170m'
    DARK_SLATE_GRAY = '\x1b[38;2;47;79;79m'
    TEAL = '\x1b[38;2;0;128;128m'
    DARK_CYAN = '\x1b[38;2;0;139;139m'
    AQUA = '\x1b[38;2;0;255;255m'
    CYAN = '\x1b[38;2;0;255;255m'
    LIGHT_CYAN = '\x1b[38;2;224;255;255m'
    DARK_TURQUOISE = '\x1b[38;2;0;206;209m'
    TURQUOISE = '\x1b[38;2;64;224;208m'
    MEDIUM_TURQUOISE = '\x1b[38;2;72;209;204m'
    PALE_TURQUOISE = '\x1b[38;2;175;238;238m'
    AQUA_MARINE = '\x1b[38;2;127;255;212m'
    POWDER_BLUE = '\x1b[38;2;176;224;230m'
    CADET_BLUE = '\x1b[38;2;95;158;160m'
    STEEL_BLUE = '\x1b[38;2;70;130;180m'
    CORN_FLOWER_BLUE = '\x1b[38;2;100;149;237m'
    DEEP_SKY_BLUE = '\x1b[38;2;0;191;255m'
    DODGER_BLUE = '\x1b[38;2;30;144;255m'
    LIGHT_BLUE = '\x1b[38;2;173;216;230m'
    SKY_BLUE = '\x1b[38;2;135;206;235m'
    LIGHT_SKY_BLUE = '\x1b[38;2;135;206;250m'
    MIDNIGHT_BLUE = '\x1b[38;2;25;25;112m'
    NAVY = '\x1b[38;2;0;0;128m'
    DARK_BLUE = '\x1b[38;2;0;0;139m'
    MEDIUM_BLUE = '\x1b[38;2;0;0;205m'
    BLUE = '\x1b[38;2;0;0;255m'
    ROYAL_BLUE = '\x1b[38;2;65;105;225m'
    LIGHT_STEEL_BLUE = '\x1b[38;2;176;196;222m'
    ALICE_BLUE = '\x1b[38;2;240;248;255m'
    AZURE = '\x1b[38;2;240;255;255m'

    # purples
    BLUE_VIOLET = '\x1b[38;2;138;43;226m'
    INDIGO = '\x1b[38;2;75;0;130m'
    DARK_SLATE_BLUE = '\x1b[38;2;72;61;139m'
    SLATE_BLUE = '\x1b[38;2;106;90;205m'
    MEDIUM_SLATE_BLUE = '\x1b[38;2;123;104;238m'
    MEDIUM_PURPLE = '\x1b[38;2;147;112;219m'
    DARK_MAGENTA = '\x1b[38;2;139;0;139m'
    DARK_VIOLET = '\x1b[38;2;148;0;211m'
    DARK_ORCHID = '\x1b[38;2;153;50;204m'
    MEDIUM_ORCHID = '\x1b[38;2;186;85;211m'
    PURPLE = '\x1b[38;2;128;0;128m'
    LAVENDER = '\x1b[38;2;0;0;0m'

    # pinks
    THISTLE = '\x1b[38;2;216;191;216m'
    PLUM = '\x1b[38;2;221;160;221m'
    VIOLET = '\x1b[38;2;238;130;238m'
    MAGENTA = '\x1b[38;2;255;0;255m'
    FUCHSIA = '\x1b[38;2;255;0;255m'
    ORCHID = '\x1b[38;2;218;112;214m'
    MEDIUM_VIOLET_RED = '\x1b[38;2;199;21;133m'
    PALE_VIOLET_RED = '\x1b[38;2;219;112;147m'
    DEEP_PINK = '\x1b[38;2;255;20;147m'
    HOT_PINK = '\x1b[38;2;255;105;180m'
    LIGHT_PINK = '\x1b[38;2;255;182;193m'
    PINK = '\x1b[38;2;255;192;203m'

    # whites
    ANTIQUE_WHITE = '\x1b[38;2;250;235;215m'
    BEIGE = '\x1b[38;2;245;245;220m'
    BISQUE = '\x1b[38;2;255;228;196m'
    BLANCHED_ALMOND = '\x1b[38;2;255;235;205m'
    WHEAT = '\x1b[38;2;245;222;179m'
    CORN_SILK = '\x1b[38;2;255;248;220m'
    LEMON_CHIFFON = '\x1b[38;2;255;250;205m'
    LIGHT_GOLDEN_ROD_YELLOW = '\x1b[38;2;250;250;210m'
    LIGHT_YELLOW = '\x1b[38;2;255;255;224m'
    FLORAL_WHITE = '\x1b[38;2;255;250;240m'
    GHOST_WHITE = '\x1b[38;2;248;248;255m'
    IVORY = '\x1b[38;2;255;255;240m'
    SNOW = '\x1b[38;2;255;250;250m'
    WHITE = '\x1b[38;2;255;255;255m'
    WHITE_SMOKE = '\x1b[38;2;245;245;245m'

    # brown
    SADDLE_BROWN = '\x1b[38;2;139;69;19m'
    SIENNA = '\x1b[38;2;160;82;45m'
    CHOCOLATE = '\x1b[38;2;210;105;30m'
    PERU = '\x1b[38;2;205;133;63m'
    SANDY_BROWN = '\x1b[38;2;244;164;96m'
    BURLY_WOOD = '\x1b[38;2;222;184;135m'
    TAN = '\x1b[38;2;210;180;140m'
    ROSY_BROWN = '\x1b[38;2;188;143;143m'
    MOCCASIN = '\x1b[38;2;255;228;181m'
    NAVAJO_WHITE = '\x1b[38;2;255;222;173m'
    PEACH_PUFF = '\x1b[38;2;255;218;185m'
    MISTY_ROSE = '\x1b[38;2;255;228;225m'
    LAVENDER_BLUSH = '\x1b[38;2;255;240;245m'
    LINEN = '\x1b[38;2;250;240;230m'
    OLD_LACE = '\x1b[38;2;253;245;230m'
    PAPAYA_WHIP = '\x1b[38;2;255;239;213m'
    SEA_SHELL = '\x1b[38;2;255;245;238m'

    # grays
    SLATE_GRAY = '\x1b[38;2;112;128;144m'
    LIGHT_SLATE_GRAY = '\x1b[38;2;119;136;153m'
    GAINSBORO = '\x1b[38;2;220;220;220m'
    LIGHT_GRAY = '\x1b[38;2;211;211;211m'
    SILVER = '\x1b[38;2;192;192;192m'
    DARK_GRAY = '\x1b[38;2;169;169;169m'
    GRAY = '\x1b[38;2;128;128;128m'
    DIM_GRAY = '\x1b[38;2;105;105;105m'
    BLACK = '\x1b[38;2;0;0;0m'


class BGColors(ColorLib):
    """Background color library class. Child of ColorLib.
    """

    # reds
    MAROON = '\x1b[48;2;128;0;0m'
    DARK_RED = '\x1b[48;2;139;0;0m'
    BROWN = '\x1b[48;2;165;42;42m'
    FIREBRICK = '\x1b[48;2;178;34;34m'
    CRIMSON = '\x1b[48;2;220;20;60m'
    RED = '\x1b[48;2;255;0;0m'
    TOMATO = '\x1b[48;2;255;99;71m'
    CORAL = '\x1b[48;2;255;127;80m'
    INDIAN_RED = '\x1b[48;2;205;92;92m'
    LIGHT_CORAL = '\x1b[48;2;240;128;128m'
    DARK_SALMON = '\x1b[48;2;233;150;122m'
    SALMON = '\x1b[48;2;250;128;114m'
    LIGHT_SALMON = '\x1b[48;2;255;160;122m'

    # oranges
    ORANGE_RED = '\x1b[48;2;255;69;0m'
    DARK_ORANGE = '\x1b[48;2;255;140;0m'
    ORANGE = '\x1b[48;2;255;165;0m'

    # yellows
    GOLD = '\x1b[48;2;255;215;0m'
    DARK_GOLDEN_ROD = '\x1b[48;2;184;134;11m'
    GOLDEN_ROD = '\x1b[48;2;218;165;32m'
    PALE_GOLDEN_ROD = '\x1b[48;2;238;232;170m'
    DARK_KHAKI = '\x1b[48;2;189;183;107m'
    KHAKI = '\x1b[48;2;240;230;140m'
    OLIVE = '\x1b[48;2;128;128;0m'
    YELLOW = '\x1b[48;2;255;255;0m'

    # greens
    YELLOW_GREEN = '\x1b[48;2;154;205;50m'
    DARK_OLIVE_GREEN = '\x1b[48;2;85;107;47m'
    OLIVE_DRAB = '\x1b[48;2;107;142;35m'
    LAWN_GREEN = '\x1b[48;2;124;252;0m'
    CHARTREUSE = '\x1b[48;2;127;255;0m'
    GREEN_YELLOW = '\x1b[48;2;173;255;47m'
    DARK_GREEN = '\x1b[48;2;0;100;0m'
    GREEN = '\x1b[48;2;0;128;0m'
    FOREST_GREEN = '\x1b[48;2;34;139;34m'
    LIME = '\x1b[48;2;0;255;0m'
    LIME_GREEN = '\x1b[48;2;50;205;50m'
    LIGHT_GREEN = '\x1b[48;2;144;238;144m'
    PALE_GREEN = '\x1b[48;2;152;251;152m'
    DARK_SEA_GREEN = '\x1b[48;2;143;188;143m'
    MEDIUM_SPRING_GREEN = '\x1b[48;2;0;250;154m'
    SPRING_GREEN = '\x1b[48;2;0;255;127m'
    SEA_GREEN = '\x1b[48;2;46;139;87m'
    MEDIUM_SEA_GREEN = '\x1b[48;2;60;179;113m'
    MINT_CREAM = '\x1b[48;2;245;255;250m'
    HONEYDEW = '\x1b[48;2;240;255;240m'

    # blues
    MEDIUM_AQUA_MARINE = '\x1b[48;2;102;205;170m'
    LIGHT_SEA_GREEN = '\x1b[48;2;32;178;170m'
    DARK_SLATE_GRAY = '\x1b[48;2;47;79;79m'
    TEAL = '\x1b[48;2;0;128;128m'
    DARK_CYAN = '\x1b[48;2;0;139;139m'
    AQUA = '\x1b[48;2;0;255;255m'
    CYAN = '\x1b[48;2;0;255;255m'
    LIGHT_CYAN = '\x1b[48;2;224;255;255m'
    DARK_TURQUOISE = '\x1b[48;2;0;206;209m'
    TURQUOISE = '\x1b[48;2;64;224;208m'
    MEDIUM_TURQUOISE = '\x1b[48;2;72;209;204m'
    PALE_TURQUOISE = '\x1b[48;2;175;238;238m'
    AQUA_MARINE = '\x1b[48;2;127;255;212m'
    POWDER_BLUE = '\x1b[48;2;176;224;230m'
    CADET_BLUE = '\x1b[48;2;95;158;160m'
    STEEL_BLUE = '\x1b[48;2;70;130;180m'
    CORN_FLOWER_BLUE = '\x1b[48;2;100;149;237m'
    DEEP_SKY_BLUE = '\x1b[48;2;0;191;255m'
    DODGER_BLUE = '\x1b[48;2;30;144;255m'
    LIGHT_BLUE = '\x1b[48;2;173;216;230m'
    SKY_BLUE = '\x1b[48;2;135;206;235m'
    LIGHT_SKY_BLUE = '\x1b[48;2;135;206;250m'
    MIDNIGHT_BLUE = '\x1b[48;2;25;25;112m'
    NAVY = '\x1b[48;2;0;0;128m'
    DARK_BLUE = '\x1b[48;2;0;0;139m'
    MEDIUM_BLUE = '\x1b[48;2;0;0;205m'
    BLUE = '\x1b[48;2;0;0;255m'
    ROYAL_BLUE = '\x1b[48;2;65;105;225m'
    LIGHT_STEEL_BLUE = '\x1b[48;2;176;196;222m'
    ALICE_BLUE = '\x1b[48;2;240;248;255m'
    AZURE = '\x1b[48;2;240;255;255m'

    # purples
    BLUE_VIOLET = '\x1b[48;2;138;43;226m'
    INDIGO = '\x1b[48;2;75;0;130m'
    DARK_SLATE_BLUE = '\x1b[48;2;72;61;139m'
    SLATE_BLUE = '\x1b[48;2;106;90;205m'
    MEDIUM_SLATE_BLUE = '\x1b[48;2;123;104;238m'
    MEDIUM_PURPLE = '\x1b[48;2;147;112;219m'
    DARK_MAGENTA = '\x1b[48;2;139;0;139m'
    DARK_VIOLET = '\x1b[48;2;148;0;211m'
    DARK_ORCHID = '\x1b[48;2;153;50;204m'
    MEDIUM_ORCHID = '\x1b[48;2;186;85;211m'
    PURPLE = '\x1b[48;2;128;0;128m'
    LAVENDER = '\x1b[48;2;0;0;0m'

    # pinks
    THISTLE = '\x1b[48;2;216;191;216m'
    PLUM = '\x1b[48;2;221;160;221m'
    VIOLET = '\x1b[48;2;238;130;238m'
    MAGENTA = '\x1b[48;2;255;0;255m'
    FUCHSIA = '\x1b[48;2;255;0;255m'
    ORCHID = '\x1b[48;2;218;112;214m'
    MEDIUM_VIOLET_RED = '\x1b[48;2;199;21;133m'
    PALE_VIOLET_RED = '\x1b[48;2;219;112;147m'
    DEEP_PINK = '\x1b[48;2;255;20;147m'
    HOT_PINK = '\x1b[48;2;255;105;180m'
    LIGHT_PINK = '\x1b[48;2;255;182;193m'
    PINK = '\x1b[48;2;255;192;203m'

    # whites
    ANTIQUE_WHITE = '\x1b[48;2;250;235;215m'
    BEIGE = '\x1b[48;2;245;245;220m'
    BISQUE = '\x1b[48;2;255;228;196m'
    BLANCHED_ALMOND = '\x1b[48;2;255;235;205m'
    WHEAT = '\x1b[48;2;245;222;179m'
    CORN_SILK = '\x1b[48;2;255;248;220m'
    LEMON_CHIFFON = '\x1b[48;2;255;250;205m'
    LIGHT_GOLDEN_ROD_YELLOW = '\x1b[48;2;250;250;210m'
    LIGHT_YELLOW = '\x1b[48;2;255;255;224m'
    FLORAL_WHITE = '\x1b[48;2;255;250;240m'
    GHOST_WHITE = '\x1b[48;2;248;248;255m'
    IVORY = '\x1b[48;2;255;255;240m'
    SNOW = '\x1b[48;2;255;250;250m'
    WHITE = '\x1b[48;2;255;255;255m'
    WHITE_SMOKE = '\x1b[48;2;245;245;245m'

    # browns
    SADDLE_BROWN = '\x1b[48;2;139;69;19m'
    SIENNA = '\x1b[48;2;160;82;45m'
    CHOCOLATE = '\x1b[48;2;210;105;30m'
    PERU = '\x1b[48;2;205;133;63m'
    SANDY_BROWN = '\x1b[48;2;244;164;96m'
    BURLY_WOOD = '\x1b[48;2;222;184;135m'
    TAN = '\x1b[48;2;210;180;140m'
    ROSY_BROWN = '\x1b[48;2;188;143;143m'
    MOCCASIN = '\x1b[48;2;255;228;181m'
    NAVAJO_WHITE = '\x1b[48;2;255;222;173m'
    PEACH_PUFF = '\x1b[48;2;255;218;185m'
    MISTY_ROSE = '\x1b[48;2;255;228;225m'
    LAVENDER_BLUSH = '\x1b[48;2;255;240;245m'
    LINEN = '\x1b[48;2;250;240;230m'
    OLD_LACE = '\x1b[48;2;253;245;230m'
    PAPAYA_WHIP = '\x1b[48;2;255;239;213m'
    SEA_SHELL = '\x1b[48;2;255;245;238m'

    # grays
    SLATE_GRAY = '\x1b[48;2;112;128;144m'
    LIGHT_SLATE_GRAY = '\x1b[48;2;119;136;153m'
    GAINSBORO = '\x1b[48;2;220;220;220m'
    LIGHT_GRAY = '\x1b[48;2;211;211;211m'
    SILVER = '\x1b[48;2;192;192;192m'
    DARK_GRAY = '\x1b[48;2;169;169;169m'
    GRAY = '\x1b[48;2;128;128;128m'
    DIM_GRAY = '\x1b[48;2;105;105;105m'
    BLACK = '\x1b[48;2;0;0;0m'
