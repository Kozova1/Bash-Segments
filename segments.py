#!/usr/bin/env python3
"""Creates a PS1 from a prompt.json file."""

import os
from typing import Dict, List
from classes import Segment, swap, setcolor, Color
from modules import parse_module
from config_file import get_json, get_toml


USE_DEBUG_CONFIG: bool = bool(os.getenv("BASH_SEGMENTS_DEBUG", None))


def set_sepcolor(color: Color) -> str:
    """Sets the color of the separator"""
    return setcolor(swap(color) if sep_inverse else color)


prompt_obj: Dict[str, any] = {}

prompt_obj, toml_ok = get_toml(debug=USE_DEBUG_CONFIG)
if not toml_ok:
    prompt_obj, json_ok = get_json(debug=USE_DEBUG_CONFIG)

segments: List[Segment] = []
obj_segs: List[any] = prompt_obj.get("segments", [])
separator: str = prompt_obj.get("separator", "|")
sep_inverse: bool = prompt_obj.get("separator_inverse", False)
IS_SPACE_END: bool = prompt_obj.get("space_at_end", True)
BCOLOR: int = prompt_obj.get("background_color", 0)
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
