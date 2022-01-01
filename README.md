# rxargs
Regex argument substitution for command-line wizardry

```
usage: rxargs [-h] [-n, --display] [-v] PATTERN COMMAND

Interpret standard input using PATTERN, then execute COMMAND as a substitution of that input. Note that this program uses python regular expressions. See <https://docs.python.org/3/library/re.html#regular-expression-syntax> for more info.

positional arguments:
  PATTERN        the pattern to parse from stdin
  COMMAND        the command to execute using the regex substitution

options:
  -h, --help     show this help message and exit
  -n, --display  display command result without running it
  -v, --version  show program's version number and exit
```
