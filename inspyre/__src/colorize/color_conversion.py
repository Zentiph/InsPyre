from typing import List, Tuple, Union

from .__utils import (verify_hex_number_value, verify_hsl_value,
                      verify_hsv_value, verify_rgb_number_value)

########## rgb to _ ##########


def rgb_to_hex(
    *rgb_value: Union[int, List[int], Tuple[int]],
    include_hashtag: bool = False
) -> str:
    """Converts an RGB color code to hexadecimal.

    :param rgb_value: The RGB value to convert. Accepts either three int values or a single List[int] or Tuple[int] with three values.
    :type rgb_value: Union[int, List[int], Tuple[int]]
    :param include_hashtag: Determines whether to include the hashtag in the returned hex string or not, defaults to True.
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
            "rgb_value accepts either three int values or a single List[int] or Tuple[int] with three values.")

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
    *rgb_value: Union[int, List[int], Tuple[int]],
    decimal_places: int = 2,
    return_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an RGB color code to HSL.

    :param rgb_value: The RGB color value to convert. Accepts either three int values or a single List[int] or Tuple[int] with three values.
    :type rgb_value: Union[int, List[int], Tuple[int]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: The converted HSL values.
    :rtype: Union[List[float], Tuple[float]]
    """

    # if rgb_value contains a single list with three ints
    if len(rgb_value) == 1 and (isinstance(rgb_value[0], list) or isinstance(rgb_value[0], tuple)) and len(rgb_value[0]) == 3 and all(isinstance(rgb_value[0][v], int) for v in range(len(rgb_value[0]))):
        r, g, b = rgb_value[0]
    # if rgb_value contains three ints
    elif len(rgb_value) == 3 and all(isinstance(arg, int) for arg in rgb_value):
        r, g, b = rgb_value
    else:
        raise TypeError(
            "rgb_value accepts either three int values or a single List[int] or Tuple[int] with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_tuple, bool):
        raise TypeError(
            "'return_tuple' must be type 'bool'.")

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

    if return_tuple:
        return (float(hue), float(saturation), float(lightness))
    return [float(hue), float(saturation), float(lightness)]


def rgb_to_hsv(
    *rgb_value: Union[int, List[int], Tuple[int]],
    decimal_places: int = 2,
    return_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an RGB color code to HSV.

    :param rgb_value: The RGB color value to convert. Accepts either three int values or a single List[int] or Tuple[int] with three values.
    :type rgb_value: Union[int, List[int], Tuple[int]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: The converted HSV values.
    :rtype: Union[List[float], Tuple[float]]
    """

    # if rgb_value contains a single list with three ints
    if len(rgb_value) == 1 and (isinstance(rgb_value[0], list) or isinstance(rgb_value[0], tuple)) and len(rgb_value[0]) == 3 and all(isinstance(rgb_value[0][v], int) for v in range(len(rgb_value[0]))):
        r, g, b = rgb_value[0]
    # if rgb_value contains three ints
    elif len(rgb_value) == 3 and all(isinstance(arg, int) for arg in rgb_value):
        r, g, b = rgb_value
    else:
        raise TypeError(
            "rgb_value accepts either three int values or a single List[int] or Tuple[int] with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_tuple, bool):
        raise TypeError(
            "'return_tuple' must be type 'bool'.")

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

    if return_tuple:
        return (float(hue), float(saturation), float(value))
    return [float(hue), float(saturation), float(value)]


########## hex to _ ##########

def hex_to_rgb(
    hex_: str,
    /,
    *,
    return_tuple: bool = False
) -> Union[List[int], Tuple[int]]:
    """Converts a hexadecimal color code to RGB.

    :param hex_: The hexadecimal color value to convert.
    :type hex_: str
    :param return_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
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

    verify_hex_number_value(hex_)

    if return_tuple:
        return tuple(int(hex_.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    return list(int(hex_.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    # taken from John1024 on stackoverflow:
    # https://stackoverflow.com/a/29643643/23745768


def hex_to_hsl(
    hex_: str,
    /,
    *,
    decimal_places: int = 2,
    return_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts a hex color code to HSL.

    :param hex_: The hex color value to convert.
    :type rgb_value: str
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: The converted HSL values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if not isinstance(hex_, str):
        raise TypeError("'hex_' must be type 'str'.")
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_tuple, bool):
        raise TypeError("'return_tuple' must be type 'bool'.")

    verify_hex_number_value(hex_)
    r, g, b = hex_to_rgb(hex_)

    return rgb_to_hsl(r, g, b)


def hex_to_hsv(
    hex_: str,
    /,
    *,
    decimal_places: int = 2,
    return_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts a hex color code to HSV.

    :param hex_: The hex color value to convert.
    :type rgb_value: str
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in rgb_value are not valid R, G, or B values.
    :return: The converted HSV values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if not isinstance(hex_, str):
        raise TypeError("'hex_' must be type 'str'.")
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_tuple, bool):
        raise TypeError("'return_tuple' must be type 'bool'.")

    verify_hex_number_value(hex_)
    r, g, b = hex_to_rgb(hex_)

    return rgb_to_hsv(r, g, b)


########## hsl to _ ##########

def hsl_to_rgb(
    *hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    return_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSL color code to RGB.

    :param hsl_value: The HSL color value to convert. Accepts either three separate values or a single List or Tuple with three values.
    :type hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]
    :param return_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsl_value are not valid H, S, or L values.
    :return: The converted RGB values.
    :rtype: Union[List[int], Tuple[int]]
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

    if not isinstance(return_tuple, bool):
        raise TypeError(
            "'return_tuple' must be type 'bool'.")

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

    if return_tuple:
        return (r, g, b)
    return [r, g, b]


def hsl_to_hex(
    *hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    include_hashtag: bool = False
) -> str:
    """Converts an HSL color code to RGB.

    :param hsl_value: The HSL color value to convert. Accepts either three separate values or a single List or Tuple with three values.
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

    if include_hashtag:
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    else:
        return '{:02x}{:02x}{:02x}'.format(r, g, b)


def hsl_to_hsv(
    *hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSL color code to HSV.

    :param hsl_value: The HSL color value to convert. Accepts either three separate values or a single List or Tuple with three values.
    :type hsl_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_tuple: bool, optional
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
    if not isinstance(return_tuple, bool):
        raise TypeError("'return_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    l = float(l)
    verify_hsl_value(h, s, l)

    s_prime = s / 100
    l_prime = l / 100

    value = l_prime + s_prime * min(l_prime, 1 - l_prime)

    if value == 0:
        saturation = 0
    else:
        saturation = 2 * (1 - l_prime / value)

    value *= 100
    saturation *= 100

    if return_tuple:
        return (round(h, decimal_places),
                round(float(saturation), decimal_places),
                round(float(value), decimal_places))
    return [round(h, decimal_places),
            round(float(saturation), decimal_places),
            round(float(value), decimal_places)]


########## hsv to _ ##########

def hsv_to_rgb(
    *hsv_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    return_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSV color code to RGB.

    :param hsv_value: The HSV color value to convert. Accepts either three separate values or a single List or Tuple with three values.
    :type hsv_value: Union[int, float, List[int, float], Tuple[int, float]
    :param return_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv_value are not valid H, S, or V values.
    :return: The converted RGB values.
    :rtype: Union[List[int], Tuple[int]]
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

    if not isinstance(return_tuple, bool):
        raise TypeError(
            "'return_tuple' must be type 'bool'.")

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

    if return_tuple:
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
                    "Each hue, saturation, and lightness value must be 'int' or 'float'.")
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

    if include_hashtag:
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    else:
        return '{:02x}{:02x}{:02x}'.format(r, g, b)


def hsv_to_hsl(
    *hsv_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]],
    decimal_places: int = 2,
    return_tuple: bool = False
) -> Union[List[float], Tuple[float]]:
    """Converts an HSV color code to HSL.

    :param hsv_value: The HSV color value to convert. Accepts either three separate values or a single List or Tuple with three values.
    :type hsv_value: Union[int, float, List[Union[int, float]], Tuple[Union[int, float]]
    :param decimal_places: The number of decimal places to round to, defaults to 2.
    :type decimal_places: int, optional
    :param return_tuple: Determines whether to return the colors as a tuple or a list, defaults to False.
    :type return_tuple: bool, optional
    :raises TypeError: If any of the arguments are not of the correct type.
    :raises ValueError: If any of the values in hsv_value are not valid H, S, or V values.
    :return: The converted HSL values.
    :rtype: Union[List[float], Tuple[float]]
    """

    if len(hsv_value) == 1 and (isinstance(hsv_value[0], list) or isinstance(hsv_value[0], tuple)) and len(hsv_value[0]) == 3:
        for v in hsv_value[0]:
            if not isinstance(v, int) and not isinstance(v, float):
                raise TypeError(
                    "Each hue, saturation, and lightness value must be 'int' or 'float'.")
        h, s, v = hsv_value[0]
    elif len(hsv_value) == 3 and (all(isinstance(arg, int) for arg in hsv_value) or all(isinstance(arg, float) for arg in hsv_value)):
        h, s, v = hsv_value
    else:
        raise TypeError(
            "hsv_value accepts either three values or a single List or Tuple with three values.")

    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be type 'int'.")
    if not isinstance(return_tuple, bool):
        raise TypeError("'return_tuple' must be type 'bool'.")

    h = float(h)
    s = float(s)
    v = float(v)
    verify_hsv_value(h, s, v)

    s_prime = s / 100
    v_prime = v / 100

    lightness = v_prime * (1 - s_prime / 2)
    if lightness in (0, 1):
        saturation = 0
    else:
        saturation = (v_prime - lightness) / min(lightness, 1 - lightness)

    lightness *= 100
    saturation *= 100

    if return_tuple:
        return (round(h, decimal_places),
                round(float(saturation), decimal_places),
                round(float(lightness), decimal_places))
    return [round(h, decimal_places),
            round(float(saturation), decimal_places),
            round(float(lightness), decimal_places)]
