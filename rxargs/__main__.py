#!/usr/bin/python
"""
Interpret standard input using PATTERN, then execute COMMAND as a substitution of that input.
"""

import argparse
import re
from os import popen
from sys import argv, stdin

__version__="0.1.0"

__epilog__="""
This program uses python regular expressions.
See <https://docs.python.org/3/library/re.html#regular-expression-syntax> for more info.
"""


def parse_args():
    argp = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog="rxargs",
        description=__doc__, 
        epilog=__epilog__
    )
    argp.add_argument('pattern', metavar='PATTERN', type=re.compile, help='the pattern to parse from stdin')
    argp.add_argument('command', metavar='COMMAND', type=str, help='the command to execute using the regex substitution')
    argp.add_argument('-n, --display', dest='display', action='store_true', help='display command result without running it')
    argp.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    args = argp.parse_args()
    return args
    
def run():
    args = parse_args()
    for line in stdin:
        line = line.rstrip('\r\n')
        cmd = args.pattern.sub(args.command, line).rstrip('\r\n')
        if args.display:
            print(f"'{line.strip()}' -> '{cmd}'")
        else:
            stm = popen(cmd)
            for l in stm.readlines():
                print(l, end='')

if __name__ == "__main__":
    run()    
