#! /usr/bin/env python

from distutils.core import setup, Extension

setup(name = "sigblock",
        version = "1.0",
        ext_modules = [Extension("sigblock", ["sigblock.c"])])
