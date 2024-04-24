"""
InsPyre.colorize.convert
------------------------

The convert module contains various functions used to convert between color codes.
Supported color codes:

    - RGB
    - hex
    - HSL
    - HSV
    - CMYK
"""

from typing import List, Tuple, Union  # pylint: disable=too-many-lines

from .__utils import (verify_cmyk_value, verify_hex_number_value,
                      verify_hsl_value, verify_hsv_value,
                      verify_rgb_number_value)


########## helper funcs ##########

def __normalize_rgb(
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


def __hue_to_rgb(h: float, c: float, x: float):
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


########## rgb to _ ##########

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

    r, g, b = __normalize_rgb(rgb)

    for color in (r, g, b):
        verify_rgb_number_value(color)

    if include_hashtag:
        return f'{r:02x}{g:02x}{b:02x}'
    return f'{r:02x}{g:02x}{b:02x}'
    # taken from educative.io:
    # https://www.educative.io/answers/how-to-convert-hex-to-rgb-and-rgb-to-hex-in-python


def rgb_to_hsl(
    rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an RGB color code to HSL.

    :param rgb: The RGB color value to convert. Accepts either a List or Tuple with three values.

        - accepts:
        - int RGB values 0-255
        - float RGB values 0.0-1.0

    :type rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb are not valid R, G, or B values.
    :return: The converted HSL values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if not (len(rgb) == 3 and isinstance(rgb, (list, tuple))):
        raise TypeError(
            "rgb accepts either a List or Tuple with three values.")
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    r, g, b = __normalize_rgb(rgb)

    for color in (r, g, b):
        verify_rgb_number_value(color)

    r = r / 255
    g = g / 255
    b = b / 255

    max_value = max(r, g, b)
    min_value = min(r, g, b)
    delta = max_value - min_value

    lightness = (max_value + min_value) / 2
    saturation = (delta) / (1 - abs(2 * lightness - 1))

    if delta == 0:
        hue = 0.0
    elif max_value == r:
        hue = (g - b) / delta % 6
    elif max_value == g:
        hue = ((b - r) / delta) + 2
    elif max_value == b:
        hue = ((r - g) / delta) + 4

    hue *= 60

    if hue < 0:
        hue += 360.0

    hue = round(hue, decimal_places)
    saturation = round(saturation * 100, decimal_places)
    lightness = round(lightness * 100, decimal_places)

    if return_as_tuple:
        return (float(hue), float(saturation), float(lightness))
    return [float(hue), float(saturation), float(lightness)]


def rgb_to_hsv(
    rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an RGB color code to HSV.

    :param rgb: The RGB color value to convert. Accepts either a List or Tuple with three values.

        - accepts:
        - int RGB values 0-255
        - float RGB values 0.0-1.0

    :type rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb are not valid R, G, or B values.
    :return: The converted HSV values.
    :rtype: Union[List[float], Tuple[float]]
    """

    # if rgb contains a single list or tuple
    if not (len(rgb) == 3 and isinstance(rgb, (list, tuple))):
        raise TypeError(
            "rgb accepts either a List or Tuple with three values.")
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    r, g, b = __normalize_rgb(rgb)

    for color in (r, g, b):
        verify_rgb_number_value(color)

    r = r / 255
    g = g / 255
    b = b / 255

    max_value = max(r, g, b)
    min_value = min(r, g, b)
    delta = max_value - min_value

    value = max_value
    saturation = delta / max_value

    if delta == 0:
        hue = 0.0
    elif max_value == r:
        hue = (g - b) / delta % 6
    elif max_value == g:
        hue = ((b - r) / delta) + 2
    elif max_value == b:
        hue = ((r - g) / delta) + 4

    hue *= 60

    if hue < 0:
        hue += 360.0

    hue = round(hue, decimal_places)
    saturation = round(saturation * 100, decimal_places)
    value = round(value * 100, decimal_places)

    if return_as_tuple:
        return (float(hue), float(saturation), float(value))
    return [float(hue), float(saturation), float(value)]


def rgb_to_cmyk(
    rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an RGB color code to CMYK.

    :param rgb: The RGB color value to convert. Accepts either a List or Tuple with three values.

        - accepts:
        - int RGB values 0-255
        - float RGB values 0.0-1.0

    :type rgb: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb are not valid R, G, or B values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
    """

    # if rgb contains a single list or tuple
    if not (len(rgb) == 3 and isinstance(rgb, (list, tuple))):
        raise TypeError(
            "rgb accepts either a List or Tuple with three values.")
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    r, g, b = __normalize_rgb(rgb)

    for color in (r, g, b):
        verify_rgb_number_value(color)

    r_prime = r / 255
    g_prime = g / 255
    b_prime = b / 255

    k = 1 - max(r_prime, g_prime, b_prime)
    c = (1 - r_prime - k) / (1 - k)
    m = (1 - g_prime - k) / (1 - k)
    y = (1 - b_prime - k) / (1 - k)

    c *= 100
    m *= 100
    y *= 100
    k *= 100

    if return_as_tuple:
        return (float(round(c, decimal_places)),
                float(round(m, decimal_places)),
                float(round(y, decimal_places)),
                float(round(k, decimal_places)))
    return [float(round(c, decimal_places)),
            float(round(m, decimal_places)),
            float(round(y, decimal_places)),
            float(round(k, decimal_places))]


########## hex to _ ##########

def hex_to_rgb(
    hex_: str,
    /,
    *,
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a hexadecimal color code to RGB.

    :param hex_: The hexadecimal color value to convert.
    :type hex_: str
    :param return_as_floats: Decides if the RGB value is returned as floats, defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If hex_ is not a valid hex value.
    :return: The converted RBG values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if not isinstance(hex_, str):
        raise TypeError("hex_to_rgb param 'hex_' must be type 'str'.")
    if not isinstance(return_as_floats, bool):
        raise TypeError(
            "'return_as_floats' must be type 'bool'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "hex_to_rgb param 'return_as_tuple' must be type 'bool'.")

    verify_hex_number_value(hex_)

    hex_ = hex_.lstrip('#')
    r = int(hex_[:2], 16)
    g = int(hex_[2:4], 16)
    b = int(hex_[4:], 16)

    if return_as_floats:
        r = float(r / 255)
        g = float(g / 255)
        b = float(b / 255)

    if return_as_tuple:
        return (r, g, b)
    return [r, g, b]


def hex_to_hsl(
    hex_: str,
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts a hex color code to HSL.

    :param hex_: The hex color value to convert.
    :type rgb: str
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb are not valid R, G, or B values.
    :return: The converted HSL values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if not isinstance(hex_, str):
        raise TypeError("'hex_' must be type 'str'.")
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    verify_hex_number_value(hex_)
    r, g, b = hex_to_rgb(hex_)

    return rgb_to_hsl([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hex_to_hsv(
    hex_: str,
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts a hex color code to HSV.

    :param hex_: The hex color value to convert.
    :type rgb: str
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb are not valid R, G, or B values.
    :return: The converted HSV values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if not isinstance(hex_, str):
        raise TypeError("'hex_' must be type 'str'.")
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    verify_hex_number_value(hex_)
    r, g, b = hex_to_rgb(hex_)

    return rgb_to_hsv([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hex_to_cmyk(
    hex_: str,
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts a hex color code to CMYK.

    :param hex_: The hex color value to convert.
    :type rgb: str
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb are not valid R, G, or B values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if not isinstance(hex_, str):
        raise TypeError("'hex_' must be type 'str'.")
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    verify_hex_number_value(hex_)
    r, g, b = hex_to_rgb(hex_)

    return rgb_to_cmyk([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


########## hsl to _ ##########

def hsl_to_rgb(
    hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts an HSL color code to RGB.

    :param hsl: The HSL color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsl must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param return_as_floats: Decides if the RGB value is returned as floats, defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl are not valid H, S, or L values.
    :return: The converted RGB values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
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

    if not isinstance(return_as_floats, bool):
        raise TypeError(
            "'return_as_floats' must be type 'bool'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    h = float(h) / 60
    s = float(s) / 100
    l = float(l) / 100
    verify_hsl_value(h, s, l)

    chroma = s * (1 - abs(2 * l - 1))
    middle_component = chroma * (1 - abs(h % 2 - 1))
    adjustment_factor = l - (chroma / 2)

    r, g, b = __hue_to_rgb(h, chroma, middle_component)

    r, g, b = [round((r + adjustment_factor) * 255),
               round((g + adjustment_factor) * 255),
               round((b + adjustment_factor) * 255)]

    if return_as_floats:
        r = float(r / 255)
        g = float(g / 255)
        b = float(b / 255)

    if return_as_tuple:
        return (r, g, b)
    return [r, g, b]


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
    verify_hsl_value(h, s, l)

    r, g, b = hsl_to_rgb(hsl)

    return rgb_to_hex([r, g, b], include_hashtag=include_hashtag)


def hsl_to_hsv(
    hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSL color code to HSV.

    :param hsl: The HSL color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsl must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl are not valid H, S, or L values.
    :return: The converted HSV values.
    :rtype: Union[List[float], Tuple[float]]
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

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    verify_hsl_value(h, s, l)

    r, g, b = hsl_to_rgb([h, s, l])
    return rgb_to_hsv([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hsl_to_cmyk(
    hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSL color code to CMYK.

    :param hsl: The HSL color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsl must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl are not valid H, S, or L values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
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

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    verify_hsl_value(h, s, l)

    r, g, b = hsl_to_rgb([h, s, l])
    return rgb_to_cmyk([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


########## hsv to _ ##########

def hsv_to_rgb(
    hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts an HSV color code to RGB.

    :param hsv: The HSV color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsv must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param return_as_floats: Decides if the RGB value is returned as floats, defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv are not valid H, S, or V values.
    :return: The converted RGB values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if not (len(hsv) == 3 and isinstance(hsv, (list, tuple))):
        raise TypeError(
            "hsv accepts either a List or Tuple with three values.")
    if not isinstance(return_as_floats, bool):
        raise TypeError(
            "'return_as_floats' must be type 'bool'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    for v in hsv:
        if not isinstance(v, int) and not isinstance(v, float):
            raise TypeError(
                "Each hue, saturation, and value values must be 'int' or 'float'.")
    h, s, v = hsv

    h = float(h) / 60
    s = float(s) / 100
    v = float(v) / 100
    verify_hsv_value(h, s, v)

    chroma = v * s
    middle_component = chroma * (1 - abs(h % 2 - 1))
    adjustment_factor = v - chroma

    r, g, b = __hue_to_rgb(h, chroma, middle_component)

    r, g, b = [round((r + adjustment_factor) * 255),
               round((g + adjustment_factor) * 255),
               round((b + adjustment_factor) * 255)]

    if return_as_floats:
        r = float(r / 255)
        g = float(g / 255)
        b = float(b / 255)

    if return_as_tuple:
        return (r, g, b)
    return [r, g, b]


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
    verify_hsl_value(h, s, v)
    r, g, b = hsv_to_rgb([h, s, v])

    return rgb_to_hex([r, g, b], include_hashtag=include_hashtag)


def hsv_to_hsl(
    hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSV color code to HSL.

    :param hsv: The HSV color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsv must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv are not valid H, S, or V values.
    :return: The converted HSL values.
    :rtype: Union[List[float], Tuple[float]]
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

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    v = float(v)
    verify_hsv_value(h, s, v)

    r, g, b = hsv_to_rgb([h, s, v])
    return rgb_to_hsl([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hsv_to_cmyk(
    hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSV color code to CMYK.

    :param hsv: The HSV color value to convert. Accepts either a List or Tuple with three values.

        - each value in hsv must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsv: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv are not valid H, S, or L values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if len(hsv) == 3 and isinstance(hsv, (list, tuple)):
        for v in hsv:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and value value must be 'int' or 'float'.")
        h, s, l = hsv
    else:
        raise TypeError(
            "hsv accepts either a List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    verify_hsv_value(h, s, l)

    r, g, b = hsv_to_rgb([h, s, l])
    return rgb_to_cmyk([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


########## cmyk to _ ##########

def cmyk_to_rgb(
    cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a CMYK color code to RGB.

    :param cmyk: The CMYK color value to convert. Accepts either a List or Tuple with four values.

        - each value in cmyk must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param return_as_floats: Decides if the RGB value is returned as floats, defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in cmyk are not valid H, S, or V values.
    :return: The converted RGB values.
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

    if not isinstance(return_as_floats, bool):
        raise TypeError(
            "'return_as_floats' must be type 'bool'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    c = float(c)
    m = float(m)
    y = float(y)
    k = float(k)
    verify_cmyk_value(c, m, y, k)

    c_prime = c / 100
    m_prime = m / 100
    y_prime = y / 100
    k_prime = k / 100

    r = round(255 * (1 - c_prime) * (1 - k_prime))
    g = round(255 * (1 - m_prime) * (1 - k_prime))
    b = round(255 * (1 - y_prime) * (1 - k_prime))

    if return_as_floats:
        r = float(r / 255)
        g = float(g / 255)
        b = float(b / 255)

    if return_as_tuple:
        return (int(r), int(g), int(b))
    return [int(r), int(g), int(b)]


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
    verify_cmyk_value(c, m, y, k)

    r, g, b = cmyk_to_rgb([c, m, y, k])
    return rgb_to_hex([r, g, b], include_hashtag=include_hashtag)


def cmyk_to_hsl(
    cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a CMYK color code to HSL.

    :param cmyk: The CMYK color value to convert. Accepts either a List or Tuple with four values.

        - each value in cmyk must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in cmyk are not valid H, S, or V values.
    :return: The converted HSL values.
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

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    c = float(c)
    m = float(m)
    y = float(y)
    k = float(k)
    verify_cmyk_value(c, m, y, k)

    r, g, b = cmyk_to_rgb([c, m, y, k])
    return rgb_to_hsl([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def cmyk_to_hsv(
    cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]],
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a CMYK color code to HSV.

    :param cmyk: The CMYK color value to convert. Accepts either a List or Tuple with four values.

        - each value in cmyk must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type cmyk: Union[List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines if the colors are returned in a tuple, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in cmyk are not valid H, S, or V values.
    :return: The converted HSV values.
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

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    c = float(c)
    m = float(m)
    y = float(y)
    k = float(k)
    verify_cmyk_value(c, m, y, k)

    r, g, b = cmyk_to_rgb([c, m, y, k])
    return rgb_to_hsv([r, g, b], decimal_places=decimal_places, return_as_tuple=return_as_tuple)
