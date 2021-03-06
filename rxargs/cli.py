#!/usr/bin/python
"""
Interpret standard input using PATTERN, then execute COMMAND using the captures of that input.
"""

from .version import __version__

import argparse
import re
import subprocess
from sys import argv, stdin


epilog=\
"By default, this program will execute a separate command for each line received from STDIN.\n"\
"Use the --whole (-w) flag to run a single command from the entire input.\n\n"\
"This program exits upon the first command executed with a non-zero exit status.\n"\
"Use the --force (-f) flag to ignore this behaviour.\n\n"\
"This program will also exit upon the first non-match in stdin.\n"\
"Use the --ignore (-i) flag to ignore those inputs instead.\n\n"\
"This program uses python regular expression syntax.\n"\
"See <https://docs.python.org/3/library/re.html#regular-expression-syntax> for more info."


def parse_args():
    import argparse
    argp = argparse.ArgumentParser(
        prog="rxargs",
        usage='%(prog)s [options] [flags] PATTERN COMMAND',
        description=__doc__, 
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    opts = argp.add_argument_group("options")
    opts.add_argument('-f', '--force', dest='force', action='store_true', help='continue processing stdin even after a command returns a non-zero exit code')
    opts.add_argument('-i', '--ignore', dest='ignore', action='store_true', help='ignore invalid matches from stdin instead of terminating the program')
    opts.add_argument('-n', '--display', dest='display', action='store_true', help='display command result without running it')
    opts.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    opts.add_argument('-w', '--whole', dest='whole', action='store_true', help='process entire stdin instead of individual lines')
    
    flags = argp.add_argument_group("flags")
    flags.add_argument('-A', '--ascii', dest='ascii', action='store_true', help=r'make \w, \W, \b, \B, \d, \D, \s and \S perform ASCII-only matching instead of full Unicode matching')
    flags.add_argument('-I', '--ignorecase', dest='ignorecase', action='store_true', help='perform case-insensitive matching')
    flags.add_argument('-L', '--locale', dest='locale', action='store_true', help=r'make \w, \W, \b, \B and case-insensitive matching dependent on the current locale')
    flags.add_argument('-M', '--multiline', dest='multiline', action='store_true', help='when specified, the pattern character \'^\' matches at the beginning of the string and at the beginning of each line (immediately following each newline); and the pattern character \'$\' matches at the end of the string and at the end of each line (immediately preceding each newline)')
    flags.add_argument('-S', '--dotall', dest='dotall', action='store_true', help='make the \'.\' special character match any character at all, including a newline')
    
    argp.add_argument('pattern', metavar='PATTERN', type=re.compile, help='a string representing the pattern to parse from stdin')
    argp.add_argument('command', metavar='COMMAND', type=str, help='a string representing the command to execute using the regex substitution. use \\# or \\g<#> to capture a numbered group, or \\g<name> to capture a named group')
    
    return argp
    
def parse_flags(args):
    flags = 0
    flags |= re.A if args.ascii else 0
    flags |= re.I if args.ignorecase else 0
    flags |= re.L if args.locale else 0
    flags |= re.M if args.multiline else 0
    flags |= re.S if args.dotall else 0
    return flags
    
def main():
    args = parse_args().parse_args()
    flags = parse_flags(args)

    data = []
    if args.whole:
        data += [stdin.read()]
    else:
        data = [l for l in stdin]
    
    for text in data:
        text = text.rstrip('\r\n')
        match = args.pattern.match(text)
        if not match:
            if args.ignore:
                continue
            else:
                exit(1)
        cmd = match.expand(args.command)
        if args.display:
            print(f"'{text}' -> '{cmd}'")
        else:
            ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = ps.communicate()[0]
            if output:
                print(output.decode(), end='')
            if ps.returncode != 0 and not args.force:
                exit(1)
    exit(0)
