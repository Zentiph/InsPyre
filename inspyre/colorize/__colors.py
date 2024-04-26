from __future__ import annotations

from typing import List, Tuple, Union

from .__utils import verify_ansi_code

END_FORMAT = '\x1b[0m'
"""Constant that should be placed at the end of each string with formatting in order to end the formatting. If not used, the formatting will carry over to the next lines in the terminal.
"""


class PredefinedColor:
    """Internal class used to create predefined colors. Main purpose is to allow the user to get the rgb and hex values of the color.
    """

    def __init__(self, value: str) -> None:
        # value checks
        if not isinstance(value, str):
            raise TypeError(
                f"PredefinedColor param 'value' must be type 'str'.")
        # verify_ansi_code(value)

        self.__value = value
        self.__prev_value = value
        self.__original_value = value

    @property
    def value(self) -> str:  # makes self.__value "immutable"
        return self.__value

    @property
    def previous_value(self) -> str:
        return self.__prev_value

    @property
    def original_value(self) -> str:
        return self.__original_value

    def revert_change(self) -> None:
        """Reverts the previous change made to the PredefinedColor instance.
        """

        prev = self.__value
        self.__value = self.__prev_value
        self.__prev_value = prev

    def revert_to_original(self) -> None:
        """Reverts the PredefinedColor instance's value to its original value on creation.
        """

        self.__prev_value = self.__value
        self.__value = self.__original_value

    def get_rgb(
        self,
        *,
        return_as_floats: bool = False,
        return_as_tuple: bool = False
    ) -> Union[List[int], Tuple[int]]:
        """Get the RGB color code of the PredefinedColor.

        :param return_as_floats: Determines whether to return the colors as floats or ints, defaults to False.
        :type return_as_floats: bool, optional
        :param return_as_tuple: Determines whether to return a tuple or a list, defaults to False.
        :type return_as_tuple: bool, optional
        :raises ValueError: If self.__value is not a valid ANSI code.
        :return: The RGB color code of the PredefinedColor.
        :rtype: Union[List[int], Tuple[int]]
        """

        # ANSI code format: \x1b[38;2;r;g;bm
        # 38;2 for text, 48;2 for bg
        parts = str(self.__value).split(';')
        if len(parts) == 5:
            r, g, b = parts[2], parts[3], parts[4][:-1]  # removes the 'm'

            if return_as_floats:
                r = float(r) / 255
                g = float(g) / 255
                b = float(b) / 255

            if not return_as_tuple:
                return [int(r), int(g), int(b)]
            return int(r), int(g), int(b)
        else:
            raise ValueError(
                f"Invalid color code format for {self!r}.value: {self.__value!r}. Expected format: '\\x1b[(3/4)8;2;r;g;bm'.")

    def get_hex(
        self,
        *,
        include_hashtag: bool = True
    ) -> str:
        """Get the hex color code of the PredefinedColor.

        :param include_hashtag: Determines whether to include the hashtag in the returned hex string or not, defaults to True.
        :type include_hashtag: bool, optional
        :raises ValueError: If self.__value is not a valid ANSI code.
        :return: The hex color code of the PredefinedColor.
        :rtype: str
        """

        # makeshift rgb_to_hex to prevent circular import between classes.py and funcs.py
        r, g, b = self.get_rgb()

        if include_hashtag:
            # taken from educative.io
            return '#{:02x}{:02x}{:02x}'.format(r, g, b)
        return '{:02x}{:02x}{:02x}'.format(r, g, b)

    def change_brightness(
        self,
        percentage: float
    ) -> None:
        """Adjust the brightness of the color by a specified percentage. Positive percentage increases the brightness, while negative percentage decreases it.

        :param percentage: The percentage to adjust the brightness by.

            - if percentage > 0: brightness increases
            - if percentage < 0: brightness decreases
            - if percentage == 0: brightness will not change 

        :type percentage: float
        :raises TypeError: If the argument is not of the correct type.
        """

        if not isinstance(percentage, float):
            raise TypeError(
                "PredefinedColor.change_brightness only accepts percentages of type 'float'.")

        if "38" in self.__value:
            color_type = "38"
        elif "48" in self.__value:
            color_type = "48"

        r, g, b = self.get_rgb()
        adjustment_factor = 1 + (percentage / 100.0)

        # using mins and maxes to stop the values from exceeding the regular RGB range (0-255)
        r = min(max(int(r * adjustment_factor), 0), 255)
        g = min(max(int(g * adjustment_factor), 0), 255)
        b = min(max(int(b * adjustment_factor), 0), 255)

        new_ansi_code = f"\x1b[{color_type};2;{r};{g};{b}m"

        self.__prev_value = self.__value
        self.__value = new_ansi_code

    # other can also be PredefinedColor but can't put it in type hints without raising an exception
    def __add__(
        self,
        other: Union[str, PredefinedColor]
    ) -> Union[str, PredefinedColor]:
        """Handle cases where a string or PredefinedColor is added to the PredefinedColor instance.

        :param other: The object being added to the PredefinedColor instance.
        :type other: Union[str, PredefinedColor]
        :raises TypeError: If the object being added is not of the correct type.
        :return: The new str or PredefinedColor instance after addition.
        :rtype: Union[str, PredefinedColor]
        """

        if isinstance(other, str):
            # if other is a str, concatenate it with the PredefinedColor's ANSI value
            return self.__value + other
        elif isinstance(other, PredefinedColor):
            # if other is a PredefinedColor, concatenate the ANSI values and return a new PredefinedColor
            return PredefinedColor(self.__value + other.__value)
        else:
            raise TypeError(
                "PredefinedColor can only be added to strings or other PredefinedColors.")

    def __radd__(
        self,
        other: Union[str, PredefinedColor]
    ) -> Union[str, PredefinedColor]:
        """Handle cases where a PredefinedColor instance is added to a string or PredefinedColor.

        :param other: The object being added to the PredefinedColor instance.
        :type other: Union[str, PredefinedColor]
        :raises TypeError: If the object being added is not of the correct type.
        :return: The new str or PredefinedColor instance after addition.
        :rtype: Union[str, PredefinedColor]
        """

        if isinstance(other, str):
            return other + self.__value
        elif isinstance(other, PredefinedColor):
            return PredefinedColor(other.__value + self.__value)
        else:
            raise TypeError(
                "PredefinedColor can only be added to strings or other PredefinedColors.")

    def __str__(self) -> str:
        return self.__value

    def __repr__(self) -> str:
        return f'PredefinedColor("{repr(self.__value)}")'


class Styles:
    """Contains text styling options such as bold, italic, etc.
    """

    BOLD = PredefinedColor('\x1b[1m')
    ITALIC = PredefinedColor('\x1b[3m')
    UNDERLINE = PredefinedColor('\x1b[4m')
    SWAP = PredefinedColor('\x1b[7m')
    """Swaps the foreground and background colors.
    """
    HIDE = PredefinedColor('\x1b[8m')
    """Prevents the text from being visible, but it still takes up space.
    """
    STRIKETHROUGH = PredefinedColor('\x1b[9m')

    CLEAR_BOLD = PredefinedColor('\x1b[22m')
    """Removes the bold effect.
    """
    CLEAR_ITALIC = PredefinedColor('\x1b[23m')
    """Removes the italic effect.
    """
    CLEAR_UNDERLINE = PredefinedColor('\x1b[24m')
    """Removes the underline effect.
    """
    CLEAR_SWAP = PredefinedColor('\x1b[27m')
    """Removes the swap effect.
    """
    UNHIDE = PredefinedColor('\x1b[28m')
    """Re-enables text visibility.
    """
    CLEAR_STRIKETHROUGH = PredefinedColor('\x1b[29m')
    """Removes the strikethrough effect.
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


class TextColors(ColorLib):
    """Text color library class. Child of ColorLib.
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
    """Background color library class. Child of ColorLib.
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
