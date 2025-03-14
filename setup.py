from setuptools import setup

setup(
    name = 'sandpiles',
    version = '0.0.0',
    packages = ['sandpiles'],
    entry_points = {
        'console_scripts': [
            'sandpiles = sandpiles.__main__:main'
        ]
    })