"""
InsPyre.colorize
----------------

The colorize package contains various functions, classes, methods, and constants
pertaining to colorizing text in the terminal.
ATTENTION: This package utilizes ANSI escape codes to colorize and format text,
which may not work in all terminal settings.
"""

from . import convert
from .__classes import BGColors, PredefinedColor, TextColors
from .__colors import (colorize_by_cmyk, colorize_by_hex, colorize_by_hsl,
                       colorize_by_hsv, colorize_by_rgb, format_text,
                       get_colors, gradient, remove_formatting)
from .__constants import RESET
from .__styles import Styles
