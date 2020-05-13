# Types of modules
All modules have a `type = "custom"` equivalent. The same as _ is to be used together with `type = "custom"`
- `username` - prints your username, as seen in `$USER`. Same as `content = "\\u"`.
- `hostname-short` - prints your hostname, without the .suffix. Same as `content = "\\h"`.
- `hostname-full` - prints your full hostname, including the .suffix. Same as `content = "\\H"`.
- `directory` - prints your full path, while abbreviating your home directory to `~`.  Same as `content = "\\w"`
- `directory-basename` - prints only the last directory in your path (the basename), such that when the path is `/home/user/Documents`, the prompt `Documents` is shown. Same as `content = "\\W"`.
- `root-sign` or `$` - Shows a `$` sign if running as a regular user, or a `#` sign if running as root. Same as `content = "\\$"`.
- `24time-withsecs` - Shows the time in 24-hour format with seconds: `HH:MM:SS`. Same as `content = "\\t"`.
- `12time-withsecs` - Shows the time in 12-hour format with seconds: `HH:MM:SS`. same as `content = "\\T"`.
- `12time-am-pm` - Shows the time in 12-hour format with AM/PM indicators: `HH:MM PM` or `HH:MM AM`. Same as `content = "\\@"`.
- `24time-nosecs` - Shows the time in 24-hour format without seconds: `HH:MM`.
- `bash-versiom` - Shows the current bash version, for example: `4.4`. Same as `content = "\\v"`.
- `bash-full-version` - Shows the current bash version and patch level, for example: `4.4.23`. Same as `content = "\\V"`.
- `history-number` - Shows the number of the current command in the history, for example: `511`. Same as `content = "\\!"`.
- `command-number` - Shows the number of the current command in the current shell, for example: `13`. Same as `content = "\\!"`.
- `jobs` - Shows the number of jobs in the current shell. Same as `content = "\\j"`.
- `term-name` - Shows the basename of the shell's terminal device name, for example: `2`. Same as `content = "\\l"`.
- `shell-name` - Shows the name of the shell, for example: `bash`. Same as `content = "\\s"`.
## Custom Date/time Format
To show a custom time format, use a segment with `type = "custom"` and `content = "\\D{F}"`. Replace F with a format string as specified in [strftime(3)](http://man7.org/linux/man-pages/man3/strftime.3.html).

With TOML:
```toml
...
[[segments]]
type = "custom"
content = "\\D{%c}"
...
```

With JSON:
```json
...
{
	"type": "custom",
	"content": "\\D{%c}",
	"background": 0,
	"foreground": 1
},
...
```
