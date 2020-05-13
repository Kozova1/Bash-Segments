"""Provides the Color class"""


class Color:
    """This class stores a terminal color - foreground and background are each 0-255"""

    def __init__(self, foreground: int, background: int):
        self.foreground: int = foreground
        self.background: int = background

    def get_background(self) -> int:
        """Returns the background color"""
        return self.background

    def get_foreground(self) -> int:
        """Returns the foreground color"""
        return self.foreground
