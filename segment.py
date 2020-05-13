"""Provides the Segment class"""
from color import Color


class Segment:
    """This class represents a single segment in the prompt"""

    def __init__(self, bgcol: int, fgcol: int, contents: str):
        self.color: Color = Color(fgcol, bgcol)
        self.contents: str = contents

    def draw(self) -> str:
        """Renders the Segment into bash syntax"""
        my_color = self.get_color()
        my_contents = self.get_contents()
        return setcolor(my_color) + my_contents

    def get_contents(self) -> str:
        """Returns the contents of the segment"""
        return self.contents

    def get_color(self) -> Color:
        """Returns the color of the segment"""
        return self.color


def swap(color: Color):
    """Returns a color with the background and foreground swapped"""
    return Color(color.get_background(), color.get_foreground())


def setcolor(color: Color) -> str:
    """Generate tput command to set colors"""
    bg_col = color.get_background()
    fg_col = color.get_foreground()
    return f"\\[$(tput sgr0; tput setaf {fg_col}; tput setab {bg_col})\\]"
