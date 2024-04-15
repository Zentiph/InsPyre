from .__classes import PredefinedColor


class Styles:
    """
    Contains text styling options such as bold, italic, etc.
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
