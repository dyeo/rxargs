from setuptools import setup
from rxargs import __version__

setup(
    name="rxargs",
    version=__version__,
    description="Regex argument substitution for command-line wizardry",
    author="Dan Yeomans",
    author_email="dan@dyeo.net",
    url="https://github.com/dyeo/rxargs",
    download_url=f"https://github.com/dyeo/rxargs/archive/{__version__}.tar.gz",
    keywords=["cli", "tools"],
    py_modules=["rxargs"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "rxargs = rxargs:main",
        ],
    }
)
