#!/usr/bin/env python3
import os
COLORS = range(15)
BASE_CMD = 'tput setab '
for c in COLORS:
    os.system(BASE_CMD + str(c) + '; printf "  "; tput sgr0; printf " "')
    os.system('tput sgr0')
print()
for c in COLORS:
    print('{0:02d} '.format(c), end='')
print()
