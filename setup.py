#!/usr/bin/python
import os
from setuptools import Extension
from setuptools import setup
from Cython.Distutils import build_ext


my_dir = os.path.dirname(os.path.abspath(__file__))   # setup.py dir
include_dirs = [os.path.join(my_dir, "c_header")]       # .h dir

sources = [os.path.join(my_dir, "c_code", "mymax.c"), # .c
           os.path.join(my_dir, "c_code", "hello.c"), # .c
           os.path.join(my_dir, "mymax.pyx"),        # .pyx  
           ]

cy_mod=Extension("mymax",                 # module name ('from mymax import pymax, pyhello')
                 sources=sources,
                 language="c",
                 include_dirs=include_dirs,
                 )

setup(name="pymymax",           # project name, used for example when uninstalling with `pip uninstall pymymax`
      ext_modules=[cy_mod],
      cmdclass={'build_ext': build_ext},)
