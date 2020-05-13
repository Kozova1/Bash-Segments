"""Provides the config from a file"""

import toml
import json
import sys
import os
from typing import Dict, Tuple

def get_toml(**kwargs) -> Tuple[Dict[str, any], bool]:
    file_path: str = ''
    if kwargs.get('debug', False):
        file_path = './prompt.toml'
    else:
        file_path = os.getenv('XDG_CONFIG_HOME', '~/.config')
        file_path = os.path.join(file_path, 'bash-segments', 'prompt.toml')
    file_path = os.path.expanduser(file_path)
    config: Dict[str, any] = {}
    try:
        with open(file_path, 'r') as f:
            config = toml.loads(f.read())
    except OSError:
        return {}, False
    except toml.TomlDecodeError:
        print('TOML parsing error. check ' + file_path, file=sys.stderr)
        sys.exit(1)
    return config, True

def get_json(**kwargs) -> Tuple[Dict[str, any], bool]:
    file_path: str = ''
    if kwargs.get('debug', False):
        file_path = './prompt.json'
    else:
        file_path = os.getenv('XDG_CONFIG_HOME', '~/.config')
        file_path = os.path.join(file_path, 'bash-segments', 'prompt.json')
    file_path = os.path.expanduser(file_path)
    config: Dict[str, any] = {}
    try:
        with open(file_path, 'r') as f:
            config = json.loads(f.read())
    except OSError:
        print('Could not open any config file.', file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print('JSON parsing error. check ' + file_path, file=sys.stderr)
        sys.exit(1)
    return config, True
