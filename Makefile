.PHONY: man

build:
	python setup.py build

install:
	python setup.py install --root="${pkgdir}" --optimize=1 --skip-build

man:
	argparse-manpage \
	    --project-name "rxargs" \
	    --url "https://www.github.com/dyeo/rxargs" \
	    --pyfile "rxargs.py" \
	    --function "parse_args" \
	    --author "Dan Yeomans" \
	    --author-email "dan@dyeo.net" \
	    --output "./man/rxargs.1"
