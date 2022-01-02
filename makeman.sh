#!/usr/bin/env bash

NAME='rxargs'
URL='https://www.github.com/dyeo/rxargs'
PYFILE='rxargs/__main__.py'
FUNCTION='parse_args'
AUTHOR='Dan Yeomans'
AUTHOR_EMAIL='dan@dyeo.net'
OUTPUT="./man/${NAME}.1"

argparse-manpage \
    --project-name "$NAME" \
    --url "$URL" \
    --pyfile "$PYFILE" \
    --function "$FUNCTION" \
    --author "$AUTHOR" \
    --author-email "$AUTHOR_EMAIL" \
    --output "$OUTPUT"
