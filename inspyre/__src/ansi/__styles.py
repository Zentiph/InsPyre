class Styles:
    """
    Contains text styling options such as bold, italic, etc.
    """

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

    CLEAR_BOLD = '\x1b[22m'
    """Removes the bold effect.
    """
    CLEAR_ITALIC = '\x1b[23m'
    """Removes the italic effect.
    """
    CLEAR_UNDERLINE = '\x1b[24m'
    """Removes the underline effect.
    """
    CLEAR_SWAP = '\x1b[27m'
    """Removes the swap effect.
    """
    UNHIDE = '\x1b[28m'
    """Re-enables text visibility.
    """
    CLEAR_STRIKETHROUGH = '\x1b[29m'
    """Removes the strikethrough effect.
    """
