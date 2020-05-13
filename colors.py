#!/usr/bin/env python3
"""Prints the 16 basic terminal colors"""
import os

COLORS = range(15)
BASE_CMD = "tput setab "
print("|", end="", flush=True)
for c in COLORS:
    os.system(BASE_CMD + str(c) + '; printf "  "; tput sgr0; printf "|"')
    os.system("tput sgr0")
print()
print("|", end="")
for c in COLORS:
    if len(str(c)) > 1:
        print(f"{c}|", end="")
    else:
        print(f" {c}|", end="")
print()
