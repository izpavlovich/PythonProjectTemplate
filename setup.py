import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import ppt_app


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


config = {
        "name": "ppt_app",
        "version": ppt_app.__version__,
        "author": "Igor Pavlovic",
        "author_email": "igor@pavlovic.me",
        "description": "Python Project Template",
        "long_description": read("README.rst"),
        "classifiers": [
            "Intended Audience :: Developers",
            "Intended Audience :: Information Technology",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7"
        ],
        "packages": ["ppt_app"],
        "entry_points":'''
            [console_scripts]
            ppt_app=ppt_app.cli.main:main
        '''
}


setup(**config)