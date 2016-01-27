# -*- coding: utf-8 -*-
from setuptools import setup

import os


try:
    from pypandoc import convert

    def read_md(f):
        return convert(f, 'rst')

except ImportError:
    convert = None
    print(
        "warning: pypandoc module not found, could not convert Markdown to RST"
    )

    def read_md(f):
        return open(f, 'r').read()  # noqa

README = os.path.join(os.path.dirname(__file__), 'README.md')


setup(
    name='mcok',
    version="0.0.1",
    author='Michał Jaworski',
    author_email='swistakm@gmail.com',
    description="Mock mock's Mock",
    long_description=read_md(README),
    url='https://github.com/pylola/mcok',
    include_package_data=True,
    install_requires=[],
    zip_safe=True,

    license="BSD",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
