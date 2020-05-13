"""Provides the premade modules for modules.py"""

from typing import Dict


MODULE_CONTENTS: Dict[str, str] = {
    "date": "\\d",
    "hostname-short": "\\h",
    "hostname-full": "\\H",
    "jobs": "\\j",
    "term-name": "\\l",
    "shell-name": "\\s",
    "24time-withsecs": "\\t",
    "12time-withsecs": "\\T",
    "12time-am-pm": "\\@",
    "24time-nosecs": "\\A",
    "username": "\\u",
    "bash-version": "\\v",
    "bash-full-version": "\\V",
    "directory": "\\w",
    "directory-basename": "\\W",
    "history-number": "\\!",
    "command-number": "\\#",
    "root-sign": "\\$",
    "$": "\\$",
}
