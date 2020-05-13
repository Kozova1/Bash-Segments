#!/usr/bin/env python3
"""Creates a PS1 from a prompt.json file."""

import json
import os
import sys
from typing import Dict, List
from segment import Segment, swap, setcolor
from color import Color
from modules import parse_module


USE_DEBUG_CONFIG: bool = bool(os.getenv('BASH_SEGMENTS_DEBUG', False))


def set_sepcolor(color: Color) -> str:
    """Sets the color of the separator"""
    return setcolor(swap(color) if sep_inverse else color)


prompt_obj: Dict[str, any] = {}
try:
    s: str = ""
    base_conf_dir = os.getenv("XDG_CONFIG_HOME", "~/.config")
    file_path = './prompt.json'
    if not USE_DEBUG_CONFIG:
        file_path = os.path.join(base_conf_dir, "bash-segments", "prompt.json")
    with open(os.path.expanduser(file_path), "r") as f:
        s = f.read()
    prompt_obj = json.loads(s)
except ValueError:
    print(
        "JSON Decode error, verify that your prompt.json is valid json", file=sys.stderr
    )
    sys.exit(1)
except OSError:
    print(
        "File open error, verify that prompt.json exists and is readable",
        file=sys.stderr,
    )
    sys.exit(1)

segments: List[Segment] = []
obj_segs: List[any] = prompt_obj.get('segments', [])
separator: str = prompt_obj.get('separator', '|')
sep_inverse: bool = prompt_obj.get('separator_inverse', False)
IS_SPACE_END: bool = prompt_obj.get('space_at_end', True)
BCOLOR: int = prompt_obj.get('background_color', 0)
for seg in obj_segs:
    segments.append(parse_module(seg))

final_prompt: str = 'PS1="'
for i, seg in enumerate(segments):
    final_prompt += seg.draw()
    next_seg: Segment = None
    try:
        next_seg = segments[i + 1]
    except IndexError:
        pass
    new_color: Color = None
    if next_seg is None:
        new_color: Color = Color(seg.get_color().get_background(), BCOLOR)
    else:
        this_bg = seg.get_color().get_background()
        next_bg = next_seg.get_color().get_background()
        new_color: Color = Color(this_bg, next_bg)
    final_prompt += set_sepcolor(new_color) + separator

final_prompt += '$(tput sgr0)"'
if IS_SPACE_END:
    final_prompt += " "
print(final_prompt)
