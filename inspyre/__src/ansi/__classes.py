from __future__ import annotations
from typing import List, Tuple, Union

from .__utils import verify_ansi_code


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
        return_tuple: bool = False
    ) -> Union[List[int], Tuple[int]]:
        """Get the RGB color code of the PredefinedColor.

        :param return_tuple: Determines whether to return a tuple or a list, defaults to False.
        :type return_tuple: bool, optional
        :raises ValueError: If self.__value is not a valid ANSI code.
        :return: The RGB color code of the PredefinedColor.
        :rtype: Union[List[int], Tuple[int]]
        """

        # ANSI code format: \x1b[38;2;r;g;bm
        # 38;2 for text, 48;2 for bg
        parts = str(self.__value).split(';')
        if len(parts) == 5:
            r, g, b = parts[2], parts[3], parts[4][:-1]  # removes the 'm'
            if not return_tuple:
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
        return f'PredefinedColor("{self.__value}")'
