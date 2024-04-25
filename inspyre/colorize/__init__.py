"""
InsPyre.colorize
----------------

The colorize package contains various functions, classes, methods, and constants
pertaining to colorizing text in the terminal.
ATTENTION: This package utilizes ANSI escape codes to colorize and format text,
which may not work in all terminal settings.
"""

from . import convert
from .__colors import (BGColors, TextColors, colorize_by_cmyk, colorize_by_hex,
                       colorize_by_hsl, colorize_by_hsv, colorize_by_rgb,
                       format_text)
from .__constants import RESET
from .__formatting import get_colors, gradient, remove_formatting
from .__styles import Styles
