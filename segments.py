#!/usr/bin/env python3
"""Creates a PS1 from a prompt.json file."""

import sys
import os
import json
from typing import List, Dict

class Color():
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

def swap(color: Color):
    """Returns a color with the background and foreground swapped"""
    return Color(color.get_background(), color.get_foreground())

def setcolor(color: Color) -> str:
    """Generate tput command to set colors"""
    bg_col = color.get_background()
    fg_col = color.get_foreground()
    return f'\\[$(tput sgr0; tput setaf {fg_col}; tput setab {bg_col})\\]'

def set_sepcolor(color: Color) -> str:
    """Sets the color of the separator"""
    return setcolor(swap(color) if sep_inverse else color)

class Segment():
    """This class represents a single segment in the prompt"""
    def __init__(self, bgcol: int, fgcol: int, contents: str):
        self.color: Color = Color(fgcol, bgcol)
        self.contents: str = contents
    def draw(self) -> str:
        """Renders the Segment into bash syntax"""
        my_color = self.get_color()
        my_contents = self.get_contents()
        return setcolor(my_color) + my_contents + set_sepcolor(my_color) + separator
    def get_contents(self) -> str:
        """Returns the contents of the segment"""
        return self.contents
    def get_color(self) -> Color:
        """Returns the color of the segment"""
        return self.color

prompt_obj: Dict[str, any] = {}
try:
    s: str = ''
    base_conf_dir = os.getenv('XDG_CONFIG_HOME', '~/.config')
    file_path = os.path.join(base_conf_dir, 'bash-segments', 'prompt.json')
    with open(file_path, 'r') as f:
        s = f.read()
    prompt_obj = json.loads(s)
except ValueError:
    print('JSON Decode error, verify that your prompt.json is valid json')
    sys.exit(1)
except OSError:
    print('File open error, verify that prompt.json exists and is readable')
    sys.exit(1)

segments: List[Segment] = []
obj_segs: List[any] = []
separator: str = '|'
sep_inverse: bool = False
IS_SPACE_END: bool = True
try:
    obj_segs = prompt_obj['segments']
    separator = prompt_obj['separator']
    sep_inverse = prompt_obj['separator_inverse']
    IS_SPACE_END = prompt_obj['space_at_end']
except KeyError:
    pass
for seg in obj_segs:
    bg: int = 0
    fg: int = 1
    content: str = '?'
    try:
        bg, fg, content = seg['background'], seg['foreground'], seg['content']
    except KeyError:
        pass
    segments.append(Segment(bg, fg, content))

final_prompt: str = 'PS1="'
for seg in segments:
    final_prompt += seg.draw()
final_prompt += '$(tput sgr0)"'
if IS_SPACE_END:
    final_prompt += ' '
print(final_prompt)
