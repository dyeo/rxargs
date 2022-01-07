from setuptools import setup
from rxargs.version import __version__

setup(
    name="rxargs",
    version=__version__,
    author='Dan Yeomans',
    author_email='dan@dyeo.net',
    url='https://github.com/dyeo/rxargs',
    download_url=f'https://github.com/dyeo/rxargs/archive/{__version__}.tar.gz',
    keywords=['cli', 'tools'],
    packages=["rxargs"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'rxargs = rxargs.cli:main',
        ],
    }
)
