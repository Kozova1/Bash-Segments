# Bash-Segments - Another bash prompt framework
Bash-Segments is a small (less than 100 python lines of code) framework for customizing bash prompts. It reads a configuration from a JSON file and creates a prompt based on it. 
## Installation
1. Clone the git repository and make sure you have python 3 installed:
```bash
git clone https://github.com/Kozova1/Bash-Segments ~/.local/share/bash-segments
```
2. Create a new config in `$XDG_CONFIG_HOME/bash-segments/prompt.json or ~/.config/prompt.json` or copy the example one to there.
3. Add execution permissions to `~/.local/share/bash-segments/segments.py` by running `chmod +x ~/.local/share/bash-segments/segments.py`.
4. Add the following line to your bashrc and restart your shell (or source the bashrc again):
```bash
eval $(~/.local/share/bash-segments/segments.py)
```
## Configuration
The configuration is entirely in JSON.  
There is some top level config:
- separator - (string, default: "|") A character that acts as a separator between segments.
- separator\_inverse - (boolean, default: false) Whether to swap between the foreground and background color of the separator - required for some powerline symbols to render correctly.
- space\_at\_end - (boolean, default: true) Whether to add a space after the prompt.
- segments - (list of segments, default: []) What segments to put in the prompt.
### Segments
The segments consist of 3 values:
- background - (int, default: 0) The background color of the segment (and separator).
- foreground - (int, default: 1) The foreground color of the segment (and separator).
- content - (string, default: "?") The contents of the segment. can include bash escape sequences, as described in [this section in the bash manual.](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#index-prompting) Do not forget to escape these sequences so that your JSON doesn't get messed up.
The segments are drawn in the order that they appear in the JSON file.

[Example Config](./prompt.json)
