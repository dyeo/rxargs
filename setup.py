from setuptools import setup

setup(
    name="rxargs",
    version="0.1.0",
    author='Dan Yeomans',
    author_email='dan@dyeo.net',
    url='https://github.com/dyeo/rxargs',
    download_url='https://github.com/dyeo/rxargs/archive/0.1.0.tar.gz',
    keywords=['cli', 'tools'],
    packages=["rxargs"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'rxargs = rxargs.__main__:run',
        ],
    }
)
