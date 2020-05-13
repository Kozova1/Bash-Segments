"""Provides the config from a file"""

import json
import os
import sys
from typing import Dict, Tuple

import toml


def get_toml(**kwargs) -> Tuple[Dict[str, any], bool]:
    """Gets the config object from the TOML config file"""
    file_path: str = ""
    if kwargs.get("debug", False):
        file_path = "./prompt.toml"
    else:
        file_path = os.getenv("XDG_CONFIG_HOME", "~/.config")
        file_path = os.path.join(file_path, "bash-segments", "prompt.toml")
    file_path = os.path.expanduser(file_path)
    config: Dict[str, any] = {}
    try:
        with open(file_path, "r") as config_file:
            config = toml.loads(config_file.read())
    except OSError:
        return {}, False
    except toml.TomlDecodeError:
        print("TOML parsing error. check " + file_path, file=sys.stderr)
        sys.exit(1)
    return config, True


def get_json(**kwargs) -> Tuple[Dict[str, any], bool]:
    """Gets the config object from the JSON config file"""
    file_path: str = ""
    if kwargs.get("debug", False):
        file_path = "./prompt.json"
    else:
        file_path = os.getenv("XDG_CONFIG_HOME", "~/.config")
        file_path = os.path.join(file_path, "bash-segments", "prompt.json")
    file_path = os.path.expanduser(file_path)
    config: Dict[str, any] = {}
    try:
        with open(file_path, "r") as config_file:
            config = json.loads(config_file.read())
    except OSError:
        print("Could not open any config file.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("JSON parsing error. check " + file_path, file=sys.stderr)
        sys.exit(1)
    return config, True
