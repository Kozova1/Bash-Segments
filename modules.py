"""Converts the new module system to the old content system."""

from typing import Dict
from segment import Segment
from defined_modules import MODULE_CONTENTS


def parse_module(module: Dict[str, any]) -> str:
    """Converts a new module to an old module"""
    contents: str = ""
    background: int = module.get("background", 0)
    foreground: int = module.get("foreground", 1)
    module_contents: int = module.get("content", "?")
    module_type: int = module.get("type", "custom")
    if module_type != "custom":
        contents = MODULE_CONTENTS.get(module_type, "?")
    else:
        contents = module_contents
    return Segment(background, foreground, contents)
