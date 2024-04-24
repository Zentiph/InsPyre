from typing import List, Tuple, Union

from .__utils import (verify_cmyk_value, verify_hex_number_value,
                      verify_hsl_value, verify_hsv_value,
                      verify_rgb_number_value)

########## rgb to _ ##########


def rgb_to_hex(
    *rgb_value: Union[int, List[Union[int, float]], Tuple[Union[int, float]]],
    include_hashtag: bool = False
) -> str:
    """Converts an RGB color code to hexadecimal.

    :param rgb_value: The RGB value to convert. Accepts either three values or a single List or Tuple with three values.
    :type rgb_value: Union[int, List[Union[int, float]], Tuple[Union[int, float]]]
    :param include_hashtag: Determines whether to include the hashtag in the returned hex string or not, defaults to True.
    :type include_hashtag: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: The converted hexadecimal value.
    :rtype: str
    """

    # if rgb_value contains a single list or tuple
    if len(rgb_value) == 1 and (isinstance(rgb_value[0], list) or isinstance(rgb_value[0], tuple)) and len(rgb_value[0]) == 3:
        if isinstance(rgb_value[0][0], int):
            r = rgb_value[0][0]
        elif isinstance(rgb_value[0][0], float):
            r = int(rgb_value[0][0] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[0][1], int):
            g = rgb_value[0][1]
        elif isinstance(rgb_value[0][1], float):
            g = int(rgb_value[0][1] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[0][2], int):
            b = rgb_value[0][2]
        elif isinstance(rgb_value[0][2], float):
            b = int(rgb_value[0][2] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

    elif len(rgb_value) == 3:
        if isinstance(rgb_value[0], int):
            r = rgb_value[0]
        elif isinstance(rgb_value[0], float):
            r = int(rgb_value[0] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[1], int):
            g = rgb_value[1]
        elif isinstance(rgb_value[1], float):
            g = int(rgb_value[1] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[2], int):
            b = rgb_value[2]
        elif isinstance(rgb_value[2], float):
            b = int(rgb_value[2] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

    else:
        raise TypeError(
            "rgb_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(include_hashtag, bool):
        raise TypeError(
            "rgb_to_hex param 'include_hashtag' must be type 'bool'.")

    for color in (r, g, b):
        verify_rgb_number_value(color)

    if include_hashtag:
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    else:
        return '{:02x}{:02x}{:02x}'.format(r, g, b)
        # taken from educative.io:
        # https://www.educative.io/answers/how-to-convert-hex-to-rgb-and-rgb-to-hex-in-python


def rgb_to_hsl(
    *rgb_value: Union[int, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an RGB color code to HSL.

    :param rgb_value: The RGB color value to convert. Accepts either three values or a single List or Tuple with three values.

        - accepts:
        - int RGB values 0-255
        - float RGB values 0.0-1.0

    :type rgb_value: Union[int, List[Union[int, float]], Tuple[Union[int, float]]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: The converted HSL values.
    :rtype: Union[List[float], Tuple[float]]
    """

    # if rgb_value contains a single list or tuple
    if len(rgb_value) == 1 and (isinstance(rgb_value[0], list) or isinstance(rgb_value[0], tuple)) and len(rgb_value[0]) == 3:
        if isinstance(rgb_value[0][0], int):
            r = rgb_value[0][0]
        elif isinstance(rgb_value[0][0], float):
            r = int(rgb_value[0][0] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[0][1], int):
            g = rgb_value[0][1]
        elif isinstance(rgb_value[0][1], float):
            g = int(rgb_value[0][1] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[0][2], int):
            b = rgb_value[0][2]
        elif isinstance(rgb_value[0][2], float):
            b = int(rgb_value[0][2] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

    elif len(rgb_value) == 3:
        if isinstance(rgb_value[0], int):
            r = rgb_value[0]
        elif isinstance(rgb_value[0], float):
            r = int(rgb_value[0] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[1], int):
            g = rgb_value[1]
        elif isinstance(rgb_value[1], float):
            g = int(rgb_value[1] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[2], int):
            b = rgb_value[2]
        elif isinstance(rgb_value[2], float):
            b = int(rgb_value[2] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

    else:
        raise TypeError(
            "rgb_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    for color in (r, g, b):
        verify_rgb_number_value(color)

    r_prime = r / 255
    g_prime = g / 255
    b_prime = b / 255

    max_value = max(r_prime, g_prime, b_prime)
    min_value = min(r_prime, g_prime, b_prime)
    delta = max_value - min_value

    lightness = (max_value + min_value) / 2
    saturation = (delta) / (1 - abs(2 * lightness - 1))

    if delta == 0:
        hue = 0.0
    elif max_value == r_prime:
        hue = ((g_prime - b_prime) / delta % 6)
    elif max_value == g_prime:
        hue = ((b_prime - r_prime) / delta) + 2
    elif max_value == b_prime:
        hue = ((r_prime - g_prime) / delta) + 4

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
    *rgb_value: Union[int, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an RGB color code to HSV.

    :param rgb_value: The RGB color value to convert. Accepts either three values or a single List or Tuple with three values.

        - accepts:
        - int RGB values 0-255
        - float RGB values 0.0-1.0

    :type rgb_value: Union[int, List[Union[int, float]], Tuple[Union[int, float]]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: The converted HSV values.
    :rtype: Union[List[float], Tuple[float]]
    """

    # if rgb_value contains a single list or tuple
    if len(rgb_value) == 1 and (isinstance(rgb_value[0], list) or isinstance(rgb_value[0], tuple)) and len(rgb_value[0]) == 3:
        if isinstance(rgb_value[0][0], int):
            r = rgb_value[0][0]
        elif isinstance(rgb_value[0][0], float):
            r = int(rgb_value[0][0] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[0][1], int):
            g = rgb_value[0][1]
        elif isinstance(rgb_value[0][1], float):
            g = int(rgb_value[0][1] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[0][2], int):
            b = rgb_value[0][2]
        elif isinstance(rgb_value[0][2], float):
            b = int(rgb_value[0][2] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

    elif len(rgb_value) == 3:
        if isinstance(rgb_value[0], int):
            r = rgb_value[0]
        elif isinstance(rgb_value[0], float):
            r = int(rgb_value[0] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[1], int):
            g = rgb_value[1]
        elif isinstance(rgb_value[1], float):
            g = int(rgb_value[1] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[2], int):
            b = rgb_value[2]
        elif isinstance(rgb_value[2], float):
            b = int(rgb_value[2] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

    else:
        raise TypeError(
            "rgb_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    for color in (r, g, b):
        verify_rgb_number_value(color)

    r_prime = r / 255
    g_prime = g / 255
    b_prime = b / 255

    max_value = max(r_prime, g_prime, b_prime)
    min_value = min(r_prime, g_prime, b_prime)
    delta = max_value - min_value

    value = max_value
    saturation = delta / max_value

    if delta == 0:
        hue = 0.0
    elif max_value == r_prime:
        hue = ((g_prime - b_prime) / delta % 6)
    elif max_value == g_prime:
        hue = ((b_prime - r_prime) / delta) + 2
    elif max_value == b_prime:
        hue = ((r_prime - g_prime) / delta) + 4

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
    *rgb_value: Union[int, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an RGB color code to CMYK.

    :param rgb_value: The RGB color value to convert. Accepts either three values or a single List or Tuple with three values.

        - accepts:
        - int RGB values 0-255
        - float RGB values 0.0-1.0

    :type rgb_value: Union[int, List[Union[int, float]], Tuple[Union[int, float]]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
    """

    # if rgb_value contains a single list or tuple
    if len(rgb_value) == 1 and (isinstance(rgb_value[0], list) or isinstance(rgb_value[0], tuple)) and len(rgb_value[0]) == 3:
        if isinstance(rgb_value[0][0], int):
            r = rgb_value[0][0]
        elif isinstance(rgb_value[0][0], float):
            r = int(rgb_value[0][0] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[0][1], int):
            g = rgb_value[0][1]
        elif isinstance(rgb_value[0][1], float):
            g = int(rgb_value[0][1] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[0][2], int):
            b = rgb_value[0][2]
        elif isinstance(rgb_value[0][2], float):
            b = int(rgb_value[0][2] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

    elif len(rgb_value) == 3:
        if isinstance(rgb_value[0], int):
            r = rgb_value[0]
        elif isinstance(rgb_value[0], float):
            r = int(rgb_value[0] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[1], int):
            g = rgb_value[1]
        elif isinstance(rgb_value[1], float):
            g = int(rgb_value[1] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

        if isinstance(rgb_value[2], int):
            b = rgb_value[2]
        elif isinstance(rgb_value[2], float):
            b = int(rgb_value[2] * 255)
        else:
            raise TypeError(
                "Each R, G, and B value must be 'int' or 'float'.")

    else:
        raise TypeError(
            "rgb_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

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
    :param return_as_floats: Determines whether to return the RGB value as floats (0.0-1.0), defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
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
    :type rgb_value: str
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
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

    return rgb_to_hsl(r, g, b, decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hex_to_hsv(
    hex_: str,
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts a hex color code to HSV.

    :param hex_: The hex color value to convert.
    :type rgb_value: str
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
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

    return rgb_to_hsv(r, g, b, decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hex_to_cmyk(
    hex_: str,
    /,
    *,
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts a hex color code to CMYK.

    :param hex_: The hex color value to convert.
    :type rgb_value: str
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
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

    return rgb_to_cmyk(r, g, b, decimal_places=decimal_places, return_as_tuple=return_as_tuple)


########## hsl to _ ##########

def hsl_to_rgb(
    *hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts an HSL color code to RGB.

    :param hsl_value: The HSL color value to convert. Accepts either three separate values or a single List or Tuple with three values.

        - each value in hsl_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]
    :param return_as_floats: Determines whether to return the RGB value as floats (0.0-1.0), defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl_value are not valid H, S, or L values.
    :return: The converted RGB values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if len(hsl_value) == 1 and (isinstance(hsl_value[0], list) or isinstance(hsl_value[0], tuple)) and len(hsl_value[0]) == 3:
        for v in hsl_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and lightness value must be 'int' or 'float'.")
        h, s, l = hsl_value[0]
    elif len(hsl_value) == 3 and (all(isinstance(arg, int) for arg in hsl_value) or all(isinstance(arg, float) for arg in hsl_value)):
        h, s, l = hsl_value
    else:
        raise TypeError(
            "hsl_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(return_as_floats, bool):
        raise TypeError(
            "'return_as_floats' must be type 'bool'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    verify_hsl_value(h, s, l)

    h_prime = h / 60
    s_prime = s / 100
    l_prime = l / 100

    chroma = s_prime * (1 - abs(2 * l_prime - 1))
    middle_component = chroma * (1 - abs(h_prime % 2 - 1))
    adjustment_factor = l_prime - (chroma / 2)

    if 0.0 <= h_prime < 1.0:
        r_prime, g_prime, b_prime = chroma, middle_component, 0
    elif 1.0 <= h_prime < 2.0:
        r_prime, g_prime, b_prime = middle_component, chroma, 0
    elif 2.0 <= h_prime < 3.0:
        r_prime, g_prime, b_prime = 0, chroma, middle_component
    elif 3.0 <= h_prime < 4.0:
        r_prime, g_prime, b_prime = 0, middle_component, chroma
    elif 4.0 <= h_prime < 5.0:
        r_prime, g_prime, b_prime = middle_component, 0, chroma
    elif 5.0 <= h_prime < 6.0:
        r_prime, g_prime, b_prime = chroma, 0, middle_component

    r, g, b = [round((r_prime + adjustment_factor) * 255),
               round((g_prime + adjustment_factor) * 255),
               round((b_prime + adjustment_factor) * 255)]

    if return_as_floats:
        r = float(r / 255)
        g = float(g / 255)
        b = float(b / 255)

    if return_as_tuple:
        return (r, g, b)
    return [r, g, b]


def hsl_to_hex(
    *hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    include_hashtag: bool = False
) -> str:
    """Converts an HSL color code to RGB.

    :param hsl_value: The HSL color value to convert. Accepts either three separate values or a single List or Tuple with three values.

        - each value in hsl_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]
    :param include_hashtag: Determines whether to include the hashtag in the returned hex string or not, defaults to True.
    :type include_hashtag: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl_value are not valid H, S, or L values.
    :return: The converted hex value.
    :rtype: str
    """

    if len(hsl_value) == 1 and (isinstance(hsl_value[0], list) or isinstance(hsl_value[0], tuple)) and len(hsl_value[0]) == 3:
        for v in hsl_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and lightness value must be 'int' or 'float'.")
        h, s, l = hsl_value[0]
    elif len(hsl_value) == 3 and (all(isinstance(arg, int) for arg in hsl_value) or all(isinstance(arg, float) for arg in hsl_value)):
        h, s, l = hsl_value
    else:
        raise TypeError(
            "hsl_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(include_hashtag, bool):
        raise TypeError(
            "'include_hashtag' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    verify_hsl_value(h, s, l)

    r, g, b = hsl_to_rgb(hsl_value)

    return rgb_to_hex(r, g, b, include_hashtag=include_hashtag)


def hsl_to_hsv(
    *hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSL color code to HSV.

    :param hsl_value: The HSL color value to convert. Accepts either three separate values or a single List or Tuple with three values.

        - each value in hsl_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl_value are not valid H, S, or L values.
    :return: The converted HSV values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if len(hsl_value) == 1 and (isinstance(hsl_value[0], list) or isinstance(hsl_value[0], tuple)) and len(hsl_value[0]) == 3:
        for v in hsl_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and lightness value must be 'int' or 'float'.")
        h, s, l = hsl_value[0]
    elif len(hsl_value) == 3 and (all(isinstance(arg, int) for arg in hsl_value) or all(isinstance(arg, float) for arg in hsl_value)):
        h, s, l = hsl_value
    else:
        raise TypeError(
            "hsl_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    verify_hsl_value(h, s, l)

    r, g, b = hsl_to_rgb(h, s, l)
    return rgb_to_hsv(r, g, b, decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hsl_to_cmyk(
    *hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSL color code to CMYK.

    :param hsl_value: The HSL color value to convert. Accepts either three separate values or a single List or Tuple with three values.

        - each value in hsl_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl_value are not valid H, S, or L values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if len(hsl_value) == 1 and (isinstance(hsl_value[0], list) or isinstance(hsl_value[0], tuple)) and len(hsl_value[0]) == 3:
        for v in hsl_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and lightness value must be 'int' or 'float'.")
        h, s, l = hsl_value[0]
    elif len(hsl_value) == 3 and (all(isinstance(arg, int) for arg in hsl_value) or all(isinstance(arg, float) for arg in hsl_value)):
        h, s, l = hsl_value
    else:
        raise TypeError(
            "hsl_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    verify_hsl_value(h, s, l)

    r, g, b = hsl_to_rgb(h, s, l)
    return rgb_to_cmyk(r, g, b, decimal_places=decimal_places, return_as_tuple=return_as_tuple)


########## hsv to _ ##########

def hsv_to_rgb(
    *hsv_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts an HSV color code to RGB.

    :param hsv_value: The HSV color value to convert. Accepts either three separate values or a single List or Tuple with three values.

        - each value in hsv_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsv_value: Union[int, float, List[int, float], Tuple[int, float]
    :param return_as_floats: Determines whether to return the RGB value as floats (0.0-1.0), defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv_value are not valid H, S, or V values.
    :return: The converted RGB values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if len(hsv_value) == 1 and (isinstance(hsv_value[0], list) or isinstance(hsv_value[0], tuple)) and len(hsv_value[0]) == 3:
        for v in hsv_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and value values must be 'int' or 'float'.")
        h, s, v = hsv_value[0]
    elif len(hsv_value) == 3 and (all(isinstance(arg, int) for arg in hsv_value) or all(isinstance(arg, float) for arg in hsv_value)):
        h, s, v = hsv_value
    else:
        raise TypeError(
            "hsv_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(return_as_floats, bool):
        raise TypeError(
            "'return_as_floats' must be type 'bool'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError(
            "'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    v = float(v)
    verify_hsv_value(h, s, v)

    h_prime = h / 60
    s_prime = s / 100
    v_prime = v / 100

    chroma = v_prime * s_prime
    middle_component = chroma * (1 - abs(h_prime % 2 - 1))
    adjustment_factor = v_prime - chroma

    if 0.0 <= h_prime < 1.0:
        r_prime, g_prime, b_prime = chroma, middle_component, 0
    elif 1.0 <= h_prime < 2.0:
        r_prime, g_prime, b_prime = middle_component, chroma, 0
    elif 2.0 <= h_prime < 3.0:
        r_prime, g_prime, b_prime = 0, chroma, middle_component
    elif 3.0 <= h_prime < 4.0:
        r_prime, g_prime, b_prime = 0, middle_component, chroma
    elif 4.0 <= h_prime < 5.0:
        r_prime, g_prime, b_prime = middle_component, 0, chroma
    elif 5.0 <= h_prime < 6.0:
        r_prime, g_prime, b_prime = chroma, 0, middle_component

    r, g, b = [round((r_prime + adjustment_factor) * 255),
               round((g_prime + adjustment_factor) * 255),
               round((b_prime + adjustment_factor) * 255)]

    if return_as_floats:
        r = float(r / 255)
        g = float(g / 255)
        b = float(b / 255)

    if return_as_tuple:
        return (r, g, b)
    return [r, g, b]


def hsv_to_hex(
    *hsv_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    include_hashtag: bool = False
) -> str:
    """Converts an HSL color code to RGB.

    :param hsv_value: The HSL color value to convert. Accepts either three separate values or a single List or Tuple with three values.
    :type hsv_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]
    :param include_hashtag: Determines whether to include the hashtag in the returned hex string or not, defaults to True.
    :type include_hashtag: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv_value are not valid H, S, or V values.
    :return: The converted hex value.
    :rtype: str
    """

    if len(hsv_value) == 1 and (isinstance(hsv_value[0], list) or isinstance(hsv_value[0], tuple)) and len(hsv_value[0]) == 3:
        for v in hsv_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and value value must be 'int' or 'float'.")
        h, s, v = hsv_value[0]
    elif len(hsv_value) == 3 and (all(isinstance(arg, int) for arg in hsv_value) or all(isinstance(arg, float) for arg in hsv_value)):
        h, s, v = hsv_value
    else:
        raise TypeError(
            "hsv_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(include_hashtag, bool):
        raise TypeError(
            "'include_hashtag' must be type 'bool'.")

    h = float(h)
    s = float(s)
    v = float(v)
    verify_hsl_value(h, s, v)
    r, g, b = hsv_to_rgb(h, s, v)

    return rgb_to_hex(r, g, b, include_hashtag=include_hashtag)


def hsv_to_hsl(
    *hsv_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSV color code to HSL.

    :param hsv_value: The HSV color value to convert. Accepts either three separate values or a single List or Tuple with three values.

        - each value in hsv_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsv_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv_value are not valid H, S, or V values.
    :return: The converted HSL values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if len(hsv_value) == 1 and (isinstance(hsv_value[0], list) or isinstance(hsv_value[0], tuple)) and len(hsv_value[0]) == 3:
        for v in hsv_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and value value must be 'int' or 'float'.")
        h, s, v = hsv_value[0]
    elif len(hsv_value) == 3 and (all(isinstance(arg, int) for arg in hsv_value) or all(isinstance(arg, float) for arg in hsv_value)):
        h, s, v = hsv_value
    else:
        raise TypeError(
            "hsv_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    v = float(v)
    verify_hsv_value(h, s, v)

    r, g, b = hsv_to_rgb(h, s, v)
    return rgb_to_hsl(r, g, b, decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def hsv_to_cmyk(
    *hsv_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSV color code to CMYK.

    :param hsv_value: The HSV color value to convert. Accepts either three separate values or a single List or Tuple with three values.

        - each value in hsv_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type hsv_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv_value are not valid H, S, or L values.
    :return: The converted CMYK values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if len(hsv_value) == 1 and (isinstance(hsv_value[0], list) or isinstance(hsv_value[0], tuple)) and len(hsv_value[0]) == 3:
        for v in hsv_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and value value must be 'int' or 'float'.")
        h, s, l = hsv_value[0]
    elif len(hsv_value) == 3 and (all(isinstance(arg, int) for arg in hsv_value) or all(isinstance(arg, float) for arg in hsv_value)):
        h, s, l = hsv_value
    else:
        raise TypeError(
            "hsv_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    verify_hsv_value(h, s, l)

    r, g, b = hsv_to_rgb(h, s, l)
    return rgb_to_cmyk(r, g, b, decimal_places=decimal_places, return_as_tuple=return_as_tuple)


########## cmyk to _ ##########

def cmyk_to_rgb(
    *cmyk_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    return_as_floats: bool = False,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a CMYK color code to RGB.

    :param cmyk_value: The CMYK color value to convert. Accepts either four separate values or a single List or Tuple with four values.

        - each value in cmyk_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type cmyk_value: Union[int, float, List[int, float], Tuple[int, float]
    :param return_as_floats: Determines whether to return the RGB value as floats (0.0-1.0), defaults to False.
    :type return_as_floats: bool, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in cmyk_value are not valid H, S, or V values.
    :return: The converted RGB values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if len(cmyk_value) == 1 and (isinstance(cmyk_value[0], list) or isinstance(cmyk_value[0], tuple)) and len(cmyk_value[0]) == 4:
        for v in cmyk_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each cyan, magenta, yellow, and black value must be 'int' or 'float'.")
        c, m, y, k = cmyk_value[0]
    elif len(cmyk_value) == 4 and (all(isinstance(arg, int) for arg in cmyk_value) or all(isinstance(arg, float) for arg in cmyk_value)):
        c, m, y, k = cmyk_value
    else:
        raise TypeError(
            "cmyk_value accepts either four values or a single List or Tuple with four values.")

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
    *cmyk_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    include_hashtag: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a CMYK color code to hex.

    :param cmyk_value: The CMYK color value to convert. Accepts either four separate values or a single List or Tuple with four values.

        - each value in cmyk_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type cmyk_value: Union[int, float, List[int, float], Tuple[int, float]
    :param include_hashtag: Determines whether to include the hashtag in the returned hex string or not, defaults to True.
    :type include_hashtag: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in cmyk_value are not valid H, S, or V values.
    :return: The converted hex values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if len(cmyk_value) == 1 and (isinstance(cmyk_value[0], list) or isinstance(cmyk_value[0], tuple)) and len(cmyk_value[0]) == 4:
        for v in cmyk_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each cyan, magenta, yellow, and black value must be 'int' or 'float'.")
        c, m, y, k = cmyk_value[0]
    elif len(cmyk_value) == 4 and (all(isinstance(arg, int) for arg in cmyk_value) or all(isinstance(arg, float) for arg in cmyk_value)):
        c, m, y, k = cmyk_value
    else:
        raise TypeError(
            "cmyk_value accepts either four values or a single List or Tuple with four values.")

    if not isinstance(include_hashtag, bool):
        raise TypeError(
            "'include_hashtag' must be type 'bool'.")

    c = float(c)
    m = float(m)
    y = float(y)
    k = float(k)
    verify_cmyk_value(c, m, y, k)

    r, g, b = cmyk_to_rgb(c, m, y, k)
    return rgb_to_hex(r, g, b, include_hashtag=include_hashtag)


def cmyk_to_hsl(
    *cmyk_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a CMYK color code to HSL.

    :param cmyk_value: The CMYK color value to convert. Accepts either four separate values or a single List or Tuple with four values.

        - each value in cmyk_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type cmyk_value: Union[int, float, List[int, float], Tuple[int, float]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in cmyk_value are not valid H, S, or V values.
    :return: The converted HSL values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if len(cmyk_value) == 1 and (isinstance(cmyk_value[0], list) or isinstance(cmyk_value[0], tuple)) and len(cmyk_value[0]) == 4:
        for v in cmyk_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each cyan, magenta, yellow, and black value must be 'int' or 'float'.")
        c, m, y, k = cmyk_value[0]
    elif len(cmyk_value) == 4 and (all(isinstance(arg, int) for arg in cmyk_value) or all(isinstance(arg, float) for arg in cmyk_value)):
        c, m, y, k = cmyk_value
    else:
        raise TypeError(
            "cmyk_value accepts either four values or a single List or Tuple with four values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    c = float(c)
    m = float(m)
    y = float(y)
    k = float(k)
    verify_cmyk_value(c, m, y, k)

    r, g, b = cmyk_to_rgb(c, m, y, k)
    return rgb_to_hsl(r, g, b, decimal_places=decimal_places, return_as_tuple=return_as_tuple)


def cmyk_to_hsv(
    *cmyk_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_as_tuple: bool = False
) -> Union[List[Union[int, float]], Tuple[Union[int, float]]]:
    """Converts a CMYK color code to HSV.

    :param cmyk_value: The CMYK color value to convert. Accepts either four separate values or a single List or Tuple with four values.

        - each value in cmyk_value must be a percentage (e.g. 0.0-100.0, not 0.0-1.0)

    :type cmyk_value: Union[int, float, List[int, float], Tuple[int, float]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_as_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_as_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in cmyk_value are not valid H, S, or V values.
    :return: The converted HSV values.
    :rtype: Union[List[Union[int, float]], Tuple[Union[int, float]]]
    """

    if len(cmyk_value) == 1 and (isinstance(cmyk_value[0], list) or isinstance(cmyk_value[0], tuple)) and len(cmyk_value[0]) == 4:
        for v in cmyk_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each cyan, magenta, yellow, and black value must be 'int' or 'float'.")
        c, m, y, k = cmyk_value[0]
    elif len(cmyk_value) == 4 and (all(isinstance(arg, int) for arg in cmyk_value) or all(isinstance(arg, float) for arg in cmyk_value)):
        c, m, y, k = cmyk_value
    else:
        raise TypeError(
            "cmyk_value accepts either four values or a single List or Tuple with four values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_as_tuple, bool):
        raise TypeError("'return_as_tuple' must be type 'bool'.")

    c = float(c)
    m = float(m)
    y = float(y)
    k = float(k)
    verify_cmyk_value(c, m, y, k)

    r, g, b = cmyk_to_rgb(c, m, y, k)
    return rgb_to_hsv(r, g, b, decimal_places=decimal_places, return_as_tuple=return_as_tuple)
