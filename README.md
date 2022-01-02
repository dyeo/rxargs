# rxargs
Regex argument substitution for command-line wizardry

```
usage: rxargs [options] [flags] PATTERN COMMAND

Interpret standard input using PATTERN, then execute COMMAND as a regex substitution of that input.

positional arguments:
  PATTERN           a string representing the pattern to parse from stdin
  COMMAND           a string representing the command to execute using the
                    regex substitution

options:
  -h, --help        show this help message and exit
  -f, --force       continue processing stdin even after a command returns a
                    non-zero exit code
  -n, --display     display command result without running it
  -v, --version     show program's version number and exit
  -w, --whole       process entire stdin instead of individual lines

flags:
  -A, --ascii       make \w, \W, \b, \B, \d, \D, \s and \S perform ASCII-only
                    matching instead of full Unicode matching
  -I, --ignorecase  perform case-insensitive matching
  -L, --locale      make \w, \W, \b, \B and case-insensitive matching
                    dependent on the current locale
  -M, --multiline   when specified, the pattern character '^' matches at the
                    beginning of the string and at the beginning of each line
                    (immediately following each newline); and the pattern
                    character '$' matches at the end of the string and at the
                    end of each line (immediately preceding each newline)
  -S, --dotall      make the '.' special character match any character at all,
                    including a newline

By default, this program exits upon the first command with a non-zero exit status.
Use the --force (-f) flag to ignore this behaviour

By default, this program will execute a separate command for each line received from STDIN.
Use the --whole (-w) flag to run a single command from the entire input.

This program uses python regular expressions.
See <https://docs.python.org/3/library/re.html#regular-expression-syntax> for more info.
```
