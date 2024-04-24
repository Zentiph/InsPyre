"""
InsPyre.colorize.convert
------------------------

This package contains color conversion functions.
Supported colors:
    - RGB
    - hex
    - HSL
    - HSV
    - CMYK
"""

from .convert_to_cmyk import hex_to_cmyk, hsl_to_cmyk, hsv_to_cmyk, rgb_to_cmyk
from .convert_to_hex import cmyk_to_hex, hsl_to_hex, hsv_to_hex, rgb_to_hex
from .convert_to_hsl import cmyk_to_hsl, hex_to_hsl, hsv_to_hsl, rgb_to_hsl
from .convert_to_hsv import cmyk_to_hsv, hex_to_hsv, hsl_to_hsv, rgb_to_hsv
from .convert_to_rgb import cmyk_to_rgb, hex_to_rgb, hsl_to_rgb, hsv_to_rgb
